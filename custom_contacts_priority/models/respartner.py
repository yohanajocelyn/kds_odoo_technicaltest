from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    priority = fields.Selection(
        [('low', 'Low'), ('normal', 'Normal'), ('high', 'High'), ('urgent', 'Urgent')],
        string='Priority',
        default='normal',
        help='Set the priority level for this contact.'
    )