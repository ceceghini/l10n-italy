# -*- coding: utf-8 -*-
# Author: Andrea Gallina
# ©  2015 Apulia Software srl
# Copyright (C) 2017 Lorenzo Battistini - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os
from . import riba_common
from odoo.report import render_report
from odoo.tools import config


class TestInvoiceDueCost(riba_common.TestRibaCommon):

    def setUp(self):
        super(TestInvoiceDueCost, self).setUp()

    def test_add_due_cost(self):
        # ---- Set Service in Company Config
        self.invoice.company_id.due_cost_service_id = self.service_due_cost.id
        # ---- Validate Invoice
        self.invoice.action_invoice_open()
        # ---- Test Invoice has 2 line
        self.assertEquals(len(self.invoice.invoice_line_ids), 3)
        # ---- Test Invoice Line for service cost
        self.assertEqual(self.invoice.invoice_line_ids[1].product_id.id,
                         self.service_due_cost.id)
        # ---- Test Invoice Line for service cost
        self.assertEqual(self.invoice.invoice_line_ids[2].product_id.id,
                         self.service_due_cost.id)
        # ---- Test Cost line is equal to 10.00
        self.assertEqual(
            (self.invoice.invoice_line_ids[1].price_unit +
             self.invoice.invoice_line_ids[2].price_unit), 10.00)
        # TODO: Test fails with error:
        # `AttributeError: 'list' object has no attribute 'invoice_line_ids'`
        # new_inv = self.invoice.copy()
        # self.assertEqual(len(new_inv.invoice_line_ids), 1)

    def test_not_add_due_cost(self):
        # create 2 invoice for partner in same month on the second one no
        # due cost line expected
        # ---- Set Service in Company Config
        self.invoice.company_id.due_cost_service_id = self.service_due_cost.id
        # ---- Validate Invoice
        self.invoice.action_invoice_open()

        self.invoice2.payment_term_id = self.payment_term2
        self.invoice2.action_invoice_open()
        # ---- Test Invoice has 1 line, no due cost add because it's add on
        # ---- firts due for partner
        self.assertEquals(len(self.invoice2.invoice_line_ids), 1)

    def test_delete_due_cost_line(self):
        # ---- Set Service in Company Config
        self.invoice.company_id.due_cost_service_id = self.service_due_cost.id
        # ---- Set allow cancel on invoice Journal
        self.invoice.journal_id.update_posted = True
        # ---- Validate Invoice
        self.invoice.action_invoice_open()
        # ---- Cancel Invoice
        self.invoice.action_invoice_cancel()
        self.invoice.action_invoice_draft()
        # ---- Set to Draft
        # Due Cost line has been unlink
        self.assertEqual(len(self.invoice.invoice_line_ids), 1)

    def test_riba_flow(self):
        recent_date = self.env['account.invoice'].search(
            [('date_invoice', '!=', False)], order='date_invoice desc',
            limit=1).date_invoice
        invoice = self.env['account.invoice'].create({
            'date_invoice': recent_date,
            'journal_id': self.sale_journal.id,
            'partner_id': self.partner.id,
            'payment_term_id': self.account_payment_term_riba.id,
            'account_id': self.account_rec1_id.id,
            'invoice_line_ids': [(
                0, 0, {
                    'name': 'product1',
                    'product_id': self.product1.id,
                    'quantity': 1.0,
                    'price_unit': 450.00,
                    'account_id': self.sale_account.id
                }
            )]
        })
        invoice.action_invoice_open()
        riba_move_line_id = False
        for move_line in invoice.move_id.line_ids:
            if move_line.account_id.id == self.account_rec1_id.id:
                riba_move_line_id = move_line.id
                line_ids = self.move_line_model.search([
                    '&',
                    '|',
                    ('riba', '=', 'True'),
                    ('unsolved_invoice_ids', '!=', False),
                    ('account_id.internal_type', '=', 'receivable'),
                    ('reconciled', '=', False),
                    ('distinta_line_ids', '=', False)
                ])
                self.assertEqual(len(line_ids), 1)
                self.assertEqual(line_ids[0].id, move_line.id)
        self.assertTrue(riba_move_line_id)

        # issue wizard
        wizard_riba_issue = self.env['riba.issue'].create({
            'configuration_id': self.riba_config.id
        })
        action = wizard_riba_issue.with_context(
            {'active_ids': [riba_move_line_id]}
        ).create_list()
        riba_list_id = action and action['res_id'] or False
        riba_list = self.distinta_model.browse(riba_list_id)
        riba_list.confirm()
        self.assertEqual(riba_list.state, 'accepted')
        self.assertEqual(invoice.state, 'paid')
        self.assertEqual(len(riba_list.acceptance_move_ids), 1)
        self.assertEqual(len(riba_list.payment_ids), 0)
        riba_list.acceptance_move_ids[0].assert_balanced()

        # I print the distina report
        data, format = render_report(
            self.env.cr, self.env.uid, riba_list.ids,
            'l10n_it_ricevute_bancarie.distinta_qweb', {}, {})
        if config.get('test_report_directory'):
            file(os.path.join(
                config['test_report_directory'], 'riba-list.' + format
            ), 'wb+').write(data)

        # accreditation wizard
        wiz_accreditation = self.env['riba.accreditation'].with_context({
            "active_model": "riba.distinta",
            "active_ids": [riba_list_id],
            "active_id": riba_list_id,
        }).create({
            'bank_amount': 445,
            'expense_amount': 5,
        })
        wiz_accreditation.create_move()
        self.assertEqual(riba_list.state, 'accredited')
        riba_list.accreditation_move_id.assert_balanced()

        # bank notifies cash in
        bank_move = self.move_model.create({
            'journal_id': self.bank_journal.id,
            'line_ids': [
                (0, 0, {
                    'partner_id': self.partner.id,
                    'account_id': self.sbf_effects.id,
                    'credit': 450,
                    'debit': 0,
                    'name': 'sbf effects',
                }),
                (0, 0, {
                    'partner_id': self.partner.id,
                    'account_id': self.riba_account.id,
                    'credit': 0,
                    'debit': 450,
                    'name': 'Banca conto ricevute bancarie',
                }),
            ]
        })
        to_reconcile = self.env['account.move.line']
        line_set = (
            bank_move.line_ids | riba_list.acceptance_move_ids[0].line_ids)
        for line in line_set:
            if line.account_id.id == self.sbf_effects.id:
                to_reconcile |= line
        self.assertEqual(len(to_reconcile), 2)
        to_reconcile.reconcile()
        # refresh otherwise riba_list.payment_ids is not recomputed
        riba_list.refresh()
        self.assertEqual(riba_list.state, 'paid')
        self.assertEqual(len(riba_list.payment_ids), 1)
        self.assertEqual(len(riba_list.line_ids), 1)
        self.assertEqual(riba_list.line_ids[0].state, 'paid')
        to_reconcile.remove_move_reconcile()
        self.assertEqual(riba_list.state, 'accredited')
        self.assertEqual(riba_list.line_ids[0].state, 'accredited')

    def test_unsolved_riba(self):
        # create another invoice to test unsolved riba
        recent_date = self.env['account.invoice'].search(
            [('date_invoice', '!=', False)], order='date_invoice desc',
            limit=1).date_invoice
        invoice = self.env['account.invoice'].create({
            'date_invoice': recent_date,
            'journal_id': self.sale_journal.id,
            'partner_id': self.partner.id,
            'payment_term_id': self.account_payment_term_riba.id,
            'account_id': self.account_rec1_id.id,
            'invoice_line_ids': [(
                0, 0, {
                    'name': 'product1',
                    'product_id': self.product1.id,
                    'quantity': 1.0,
                    'price_unit': 100.00,
                    'account_id': self.sale_account.id
                }
            )]
        })
        invoice.action_invoice_open()
        for move_line in invoice.move_id.line_ids:
            if move_line.account_id.id == self.account_rec1_id.id:
                riba_move_line_id = move_line.id
        # issue wizard
        wizard_riba_issue = self.env['riba.issue'].create({
            'configuration_id': self.riba_config.id
        })
        action = wizard_riba_issue.with_context(
            {'active_ids': [riba_move_line_id]}
        ).create_list()
        riba_list_id = action and action['res_id'] or False
        riba_list = self.distinta_model.browse(riba_list_id)
        riba_list.confirm()
        self.assertEqual(riba_list.state, 'accepted')
        self.assertEqual(invoice.state, 'paid')
        # accreditation wizard
        wiz_accreditation = self.env['riba.accreditation'].with_context({
            "active_model": "riba.distinta",
            "active_ids": [riba_list_id],
            "active_id": riba_list_id,
        }).create({
            'bank_amount': 95,
            'expense_amount': 5,
        })
        wiz_accreditation.create_move()
        self.assertEqual(riba_list.state, 'accredited')
        riba_list.accreditation_move_id.assert_balanced()

        # unsolved wizard
        wiz_unsolved = self.env['riba.unsolved'].with_context({
            "active_model": "riba.distinta.line",
            "active_ids": [riba_list.line_ids[0].id],
            "active_id": riba_list.line_ids[0].id,
        }).create({
            'bank_amount': 102,
            'expense_amount': 2,
        })
        wiz_unsolved.create_move()
        self.assertEqual(riba_list.state, 'unsolved')
        self.assertEqual(len(riba_list.line_ids), 1)
        self.assertEqual(riba_list.line_ids[0].state, 'unsolved')
        self.assertTrue(invoice.unsolved_move_line_ids)

        riba_list.line_ids[0].unsolved_move_id.line_ids.remove_move_reconcile()
        self.assertEqual(riba_list.state, 'accredited')
        self.assertEqual(len(riba_list.line_ids), 1)
        self.assertEqual(riba_list.line_ids[0].state, 'accredited')
