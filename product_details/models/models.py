# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _

class ProductCategory(models.Model):
    _inherit = 'product.category'

    name = fields.Char('Name', index=True, required=True, translate=True)



class ProductTemplate(models.Model):
    _inherit = "product.template"


    color = fields.Char('Color', index=True,   translate=True)
    brand = fields.Char('Brand', index=True,   translate=True)



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
