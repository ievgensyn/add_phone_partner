{
    'name': 'Partner customization',
    'summary': 'Additional fields in res.partner',
    'category': 'Extra Tools',

    'license': 'Other proprietary',
    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'version': '13.0.0.0.1',
    'depends': ['base', 'contacts', ],

    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
    ],
    'application': False,
    'installable': True,
}
