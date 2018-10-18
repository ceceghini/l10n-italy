[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/OCB.svg?branch=7.0)](https://travis-ci.org/Odoo-Italia-Associazione/OCB)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/OCB/badge.svg?branch=7.0)](https://coveralls.io/github/Odoo-Italia-Associazione/OCB?branch=7.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/OCB/branch/7.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/OCB/branch/7.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](https://erp7.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Flask Sphinx Styles
===================

This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

1. put this folder as _themes into your docs folder.  Alternatively
   you can also use git submodules to check out the contents there.
2. add this to your conf.py:

   sys.path.append(os.path.abspath('_themes'))
   html_theme_path = ['_themes']
   html_theme = 'flask'

The following themes exist:

- 'flask' - the standard flask documentation theme for large
  projects
- 'flask_small' - small one-page theme.  Intended to be used by
  very small addon libraries for flask.

The following options exist for the flask_small theme:

   [options]
   index_logo = ''              filename of a picture in _static
                                to be used as replacement for the
                                h1 in the index.rst file.
   index_logo_height = 120px    height of the index logo
   github_fork = ''             repository name on github for the
                                "fork me" badge

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017 Odoo Italia Associazione issues modules for Italian localization not developed by OCA
or available only with Odoo Proprietary License.
Odoo Italia Associazione distributes code under [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) or [LGPL](https://www.gnu.org/licenses/lgpl.html) free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 rilascia moduli per la localizzazione italiana non sviluppati da OCA
o disponibili solo con [Odoo Proprietary License](https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html).

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) o [LGPL](https://www.gnu.org/licenses/lgpl.html)

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)


