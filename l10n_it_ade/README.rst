============================
|icon| Agenzia delle Entrate
============================

**Codice e definizioni come da Agenzia delle Entrate**

.. |icon| image:: https://raw.githubusercontent.com/Odoo-Italia-Associazione/l10n-italy/10.0/l10n_it_ade/static/description/icon.png

|Maturity| |Build Status| |Coverage Status| |Codecov Status| |license gpl| |Tech Doc| |Help| |Try Me|

.. contents::

Overview / Panoramica
=====================

|en| Tax Authority Definitions
==============================

This module has no specific function for End-user.

It defines the structures by Italian Tax Authority to manage
all fiscal communications.
Inside there are xml schema files used by FatturaPA, EInvoice and VAT settlement.

This module requires `PyXB 1.2.4 <http://pyxb.sourceforge.net/>`__

|it| Definizioni Agenzia delle Entrate
======================================

Questo modulo non ha funzioni specifiche per l'utente finale.
Contiene dati e definizioni stabilite dall'Agenzia delle Entrate
All'interno sono presenti gli schemi xml usati da FatturaPA,
Fattura Elettronica B2B, Liquidazione IVA elettronica e Comunicazione IVA.

|info| Questo modulo è incompatibile con alcuni moduli OCA.

|warning| Lo schema di definizione dei file xml, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml dell'Agenzia delle Entrate; come conseguenza nasce un conflitto tra
moduli diversi che riferiscono allo schema dell'Agenzia delle Entrate,
segnalato dall'errore:

|exclamation| name CryptoBinary used for multiple values in typeBinding

Tutti i moduli della localizzazione italiana che generano file xml dipendenti
dallo schema dell'Agenzia delle Entrate devono dichiare il modulo
`l10n_it_ade <https://github.com/Odoo-Italia-Associazione/l10n-italy/tree/10.0/l10n_it_ade>`__ come dipendenza.

Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'ultimo autore: Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>.

Features / Caratteristiche
--------------------------

Features / Funzioni
-------------------

+------------------------------------------------------+----------+----------------------------------------------+
| Feature / Funzione                                   |  Status  | Notes / Note                                 |
+------------------------------------------------------+----------+----------------------------------------------+
| Fiscal Invoice Type / Tipo fattura fiscale           | |check|  | Codifica tipo di fattura come da AdE         |
+------------------------------------------------------+----------+----------------------------------------------+
| Codice Carica                                        | |check|  | Codifica codice carica come da AdE           |
+------------------------------------------------------+----------+----------------------------------------------+
| Tax Nature / Natura fiscael dell'IVA                 | |check|  | Codifica natura fiscale dell'IVA come da AdE |
+------------------------------------------------------+----------+----------------------------------------------+


Certifications / Certificazioni
-------------------------------

Certifications / Certificazioni
-------------------------------

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| Logo                 | Ente/Certificato                                                                                                                                                                                                  | Data inizio   | Da fine      | Note                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |xml\_schema|        | `ISO + Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__                             | 01-06-2017    | 31-12-2018   | Validazione contro schema xml                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+
| |FatturaPA|          | `FatturaPA <https://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Comunicazioni/Fatture+e+corrispettivi/Fatture+e+corrispettivi+ST/ST+invio+di+fatturazione+elettronica/?page=schedecomunicazioni/>`__  | 01-06-2017    | 31-12-2018   | Controllo tramite sito Agenzia delle Entrate |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------------+


Usage / Utilizo
---------------

Usage / Uso
===========

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Natura dell'IVA

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Tipi Fattura

|menu| Contabilità > Configurazione > Contabilità > Definizioni Agenzia delle Entrate > Codice Carica


OCA comparation / Confronto con OCA
-----------------------------------

|OCA project|


Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
----------------------------

* python
* postgresql 9.2+

Installation / Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__         |
+---------------------------------+------------------------------------------+
| Suggested deployment is         | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| /opt/odoo/10.0/l10n-italy/                                                 |
+----------------------------------------------------------------------------+

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 10.0 -O oia
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 10.0 -vsy -o /opt/odoo/10.0

From UI: go to:

* |menu| Setting > Activate Developer mode 
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **l10n_it_ade** > Install

Upgrade / Aggiornamento
-----------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| When you want upgrade and you   | Per aggiornare, se avete installato con  |
| installed using above           | le istruzioni di cui sopra:              |
| statements:                     |                                          |
+---------------------------------+------------------------------------------+

::

    cd /opt/odoo/10.0/l10n-italy/
    git pull origin 10.0
    # Adjust following statements as per your system
    sudo systemctl restart odoo

From UI: go to:

* |menu| Setting > Activate Developer mode
* |menu| Apps > Update Apps List
* |menu| Setting > Apps |right_do| Select **l10n_it_ade** > Update

Support / Supporto
------------------

|Odoo Italia Associazione| This module is maintained by the Odoo Italia Associazione and support is supplied
through its `forum <https://odoo-italia.org/index.php/kunena/recente>`__



Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/Odoo-Italia-Associazione/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------

If you have a proposal to change this module, you may want to send an email to
<moderatore@odoo-italia.org> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.


Credits / Titoli di coda
========================

Authors / Autori
----------------

* SHS-AV s.r.l. <https://www.zeroincombenze.it/>

Contributors / Contributi da
----------------------------

* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

Acknowledges / Riconoscimenti
-----------------------------

+-----------------------------------+-------------------------------------------+
| |en|                              | |it|                                      |
+-----------------------------------+-------------------------------------------+
| This software inherits from past  | Questo software eredita da versioni       |
| versions some parts of code. Even | passate alcune parti di codice. Anche     |
| if people did not actively        | se non hanno partecipato attivamente allo |
| participate to development, we    | allo sviluppo, noi siamo grati a tutte le |
| acknowledge them for their prior  | persone che precedentemente vi hanno      |
| contributions.                    | contribuito.                              |
+-----------------------------------+-------------------------------------------+

----------------

**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP)

**OCA**, or the `Odoo Community Association <http://odoo-community.org/>`__,
is a nonprofit organization whose mission is to support
the collaborative development of Odoo features and promote its widespread use.

**Odoo Italia Associazione**, or the `Associazione Odoo Italia <https://www.odoo-italia.org/>`__
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017 Odoo Italia Associazione issues modules for Italian localization not developed by OCA
or available only with `Odoo Proprietary License <https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html>`__
Odoo Italia Associazione distributes code under `AGPL <https://www.gnu.org/licenses/agpl-3.0.html>`__
or `LGPL <https://www.gnu.org/licenses/lgpl.html>`__ free license.

`Odoo Italia Associazione <https://www.odoo-italia.org/>`__ è un'Associazione senza fine di lucro
che dal 2017 rilascia moduli per la localizzazione italiana non sviluppati da OCA
o disponibili solo con `Odoo Proprietary License <https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html>`__

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza `AGPL <https://www.gnu.org/licenses/agpl-3.0.html>`__
o `LGPL <https://www.gnu.org/licenses/lgpl.html>`__


|chat_with_us|


|

Last Update / Ultimo aggiornamento: 2018-11-02

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=10.0
    :target: https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=10.0
    :target: https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=10.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/10.0
    :alt: Codecov
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg
    :target: https://github.com/OCA/l10n-italy/tree/10.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/10.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/10.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://odoo10.odoo-italia.org
    :alt: Try Me
.. |OCA Codecov Status| image:: Unknown badge-oca-codecov
    :target: Unknown oca-codecov-URL
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://gitter.im/odoo_italia/development
