# -*- coding: utf-8 -*-
# -- coding utf-8 --
# {
#     'name': 'Mubeth Rent Car',
#     'version': '1.0',
#     'summary': 'Style RentCar RealTime',
#     'sequence': 10,
#     'description': """Style rentcar management software""",
#     'category': 'Productivity',
#     'website': '',
#     'depends': ['base'],
#     'data': [
#         'security/ir.model.access.csv'
#     ],
#     'demo':[],
#     'qweb':[],
#     'installable': True,
#     'auto_install': False,
#     'application': True
# }

# -*- coding: utf-8 -*-
{
    'name': 'Mubeth Rent Car',
    'summary': 'Mubeth Rent Car management software',
    'description': """Mubeth Rent Car management software""",
    'author': "My Company",
    'website': "http://srikandiart.com",
    
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mubethrentcar_views.xml',
        'views/mubethrentcar_maintenance.xml',
        'views/mubethrentcar_pegawai.xml',
        'views/mubethrentcar_customer.xml',
        'views/mubethrentcar_order.xml'
    ],
}

