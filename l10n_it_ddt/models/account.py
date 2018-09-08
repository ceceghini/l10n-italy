# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Abstract (http://www.abstract.it)
#    @author Davide Corio <davide.corio@abstract.it>
#    Copyright (C) 2015 Apulia Software s.r.l. (http://www.apuliasoftware.it)
#    @author Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
#
#    License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
##############################################################################


from openerp import fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    carriage_condition_id = fields.Many2one(
        'stock.picking.carriage_condition',
        string='Carriage Condition')
    goods_description_id = fields.Many2one(
        'stock.picking.goods_description',
        string='Description of Goods')
    transportation_reason_id = fields.Many2one(
        'stock.picking.transportation_reason',
        string='Reason for Transportation')
    transportation_method_id = fields.Many2one(
        'stock.picking.transportation_method',
        string='Method of Transportation')
    parcels = fields.Integer('Parcels')

    def onchange_partner_id(
            self, cr, uid, ids, type, partner_id, date_invoice=False,
            payment_term=False, partner_bank_id=False, company_id=False,
            context=None):
        context = context or {}
        res = super(AccountInvoice, self).onchange_partner_id(
            cr, uid, ids, type, partner_id, date_invoice, payment_term,
            partner_bank_id, company_id, context)
        if partner_id:
            partner = self.pool.get('res.partner').browse(cr, uid, partner_id)
            res['value'][
                'carriage_condition_id'] = partner.carriage_condition_id.id
            res['value'][
                'goods_description_id'] = partner.goods_description_id.id
            res['value'][
                'transportation_reason_id'
                ] = partner.transportation_reason_id.id
            res['value'][
                'transportation_method_id'
                ] = partner.transportation_method_id.id
        return res
