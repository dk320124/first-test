{
    'name': 'employee expense',
    'version': '1.0.0.6',
    'author': 'ceo',
    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/employee.xml',
        'views/domestic.xml',
        'views/International.xml',
        'security/security.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}
