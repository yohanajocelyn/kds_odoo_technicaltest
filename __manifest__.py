{
    'name': 'Custom Contact Priority',
    'version': '1.0',
    'summary': 'Adds a priority field to the contact form (Technical Test KDS)',
    'sequence': 10,
    'description': """
        This module allows users to set a priority level (Low, Medium, High) 
        for each contact, appearing as stars on the contact form.
    """,
    'category': 'Tools',
    'author': 'Yohana',
    'website': 'https://github.com/yohanajocelyn',
    'depends': ['base', 'contacts'],  # CRITICAL: Ensures 'contacts' is installed first
    'data': [
        'views/res_partner_view.xml',  # Loads your XML UI changes
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}