{
    'name': "xXo",
    'author': "ziad waheed",
    'category': '',
    'version': "17.0.0.2",
    'depends': ['base','sale_management','account_accountant', 'mail',
               ],
    'data': [
        'views/base_menu.xml',
        'views/property_views.xml',
        'security/ir.model.access.csv',
        'views/owner_views.xml',
        'views/tag_views.xml',
        'views/sale_order_view.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css',
        ]
    },



    'applaction': True,
}
