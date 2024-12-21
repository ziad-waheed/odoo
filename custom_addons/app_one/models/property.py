from odoo import models,fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description = 'record'      #the name user wii be show
    _inherit = ['mail.thread', 'mail.activity.mixin'] #for chatter

    name = fields.Char(string="Name",required='1', size=12, default='new', tracking=1)
    description = fields.Text(default='Abc')
    postcode = fields.Char(tracking=1)
    date_availability = fields.Date(tracking=1)
    expected_price = fields.Float()
    selling_price = fields.Float(digits=(1,5))
    diff = fields.Float(compute="_compute_diff", readonly=0)
    bedrooms = fields.Integer(required=1)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('north','North')
    ], default='north')
    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
    ], default='draft')


    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    owner_phone = fields.Char(related='owner_id.phone', string='Owner phone', readonly=0)
    owner_address = fields.Char(related='owner_id.address', string='Owner address', readonly=0)

    _sql_constraints = [
        ('check_uniqueness', 'unique(name)', 'The property name shall be unique !'),
       # ('check_unique', 'unique(owner_id)', 'The property name shall be unique !')
    ]

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms ==0:
                print("not valid")
                raise ValidationError('please add valid number of bedrooms')

#crud methods
    @api.model_create_multi
    def create(self,vals):
        res = super(Property, self).create(vals)
        print('create method')
        return res
    @api.model

   # def search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
       # res = super(Property, self). search(domain, offset, limit, order, access_rights_uid)
        #print('search method')
       # return res

    def write(self, vals):
        res = super(Property, self).write(vals)
        print('write method')
        return res

    def unlink(self):
        res = super(Property, self).unlink()
        print('unlink method')
        return res

    def action_draft(self):
        for rec in self:
            print("inside draft action")
            rec.write({
                 'state':'draft'
            })

    def action_pending(self):
        for rec in self:
            print("inside pending action")
            rec.write({'state': 'pending'})

    def action_sold(self):
        for rec in self:
            print("inside sold action")
            rec.write({'state': 'sold'})

    @api.depends('expected_price','selling_price')
    def _compute_diff(self):
        for rec in self:
            print('inside compute diff')
            rec.diff = rec.expected_price - rec.selling_price


   # @api.onchange('expected-price')
   # def _onchange_expected_price(self):
       # for rec in self:
           # print(rec)
           # print('inside_onchange_expected_price')
           # return {'title': 'warning', 'message': 'negative vales', 'type': 'notification'}
