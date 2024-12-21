from odoo import models,fields

class Tag(models.Model):
    _name = 'tag'

    name = fields.Char(string="Name",required='1', size=12, default='new')
