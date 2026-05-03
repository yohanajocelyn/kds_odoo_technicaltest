from odoo import models, fields

class SalesOrder(models.Model):
    _inherit = 'sale.order'

    customer_priority = fields.Selection(
        related='partner_id.priority',
        string='Customer Priority',
        store=True,
        readonly=True
    )