# -*- coding: utf-8 -*- 

from openerp import models, fields, api

class price_product_template(models.Model):

	_inherit = "product.template"
	price_1 = fields.Float(string='Precio Monge', digits=(9,2), default='0')
	price_2 = fields.Float(string='Precio_2', digits=(9,2), default='0')
	price_3 = fields.Float(string='Precio_3', digits=(9,2), default='0')

