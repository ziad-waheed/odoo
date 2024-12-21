from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    property_id = fields.Many2one('property')


    def action_confirm (self):
        res = super(SaleOrder, self).action_confirm()
        #logic
        print('success confirm')
        return res

#how add logic to methods or edit