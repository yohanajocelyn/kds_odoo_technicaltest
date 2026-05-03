{
    'name': 'Custom Contact Priority',
    'version': '1.0',
    'summary': 'Adds a priority field to the contact form (Technical Test KDS)',
    'sequence': 10,
    'description': """
        This module allows users to set a priority level (Low, Medium, High, Urgent) 
        for each contact, appearing as stars on the contact form.
    """,
    'depends': ['base', 'contacts'],  # Ensures 'contacts' is installed first
    'data': [
        'views/contacts_views.xml',  # Loads your XML UI changes
        'views/sales_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}