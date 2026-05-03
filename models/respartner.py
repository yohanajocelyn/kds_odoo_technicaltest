from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    priority = fields.Selection(
        [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        string='Priority',
        default='medium',
        help='Set the priority level for this contact.'
    )