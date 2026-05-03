{
    'name': 'Custom Contact Priority',
    'version': '1.0',
    'summary': 'Adds a priority field to the contact form (Technical Test KDS)',
    'sequence': 10,
    'description': """
        This module allows users to set a priority level (Low, Medium, High, Urgent) 
        for each contact, appearing as stars on the contact form.
    """,
    'depends': ['base', 'contacts', 'sale'],  # Ensures the necessary modules are installed first
    # Where to add new view files
    'data': [
        'views/contacts_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}