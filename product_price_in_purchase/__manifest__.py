# -*- coding: utf-8 -*-
{
    'name': "Product Price in Purchase",
    'summary': """Show product price in purchase order line""",
    'description': """Show product price in purchase order line""",
    'author': "Tri Nanda",
    'website': "http://www.github.com/trinanda",
    'images': ['static/description/icon.png'],
    'category': 'Purchases',
    'version': '15.0.0.0.1',
    'support': 'trinanda357@gmail.com',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'views/purchase_views.xml',
    ],
}
