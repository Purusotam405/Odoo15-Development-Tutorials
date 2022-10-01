{
    'name': 'Website plant nursery Development',
    'version': '1.0.0',
    'category': 'Website plant nursery',
    'summary': 'Website plant nursery',
    'sequence': -100,
    'description': """ Website plant nursery""",
    'depends': [
        'website', 'website_theme_install'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/Theme_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}
