{
    'name': "To Do Management",
    'author': "Omar Abdelkarim",
    'category': '',
    'version': '17.0.0.1.0',
    'depends': ['base', 'mail'],

    'data': [  # path within the application
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/to_do_view.xml',
    ],
    'application': True,
    'installable': True,
}
