# -*- coding: utf-8 -*- 

from openerp import models, fields, api

class product_code_report(models.Model):

	_inherit = "product.product"
	code_sale= fields.selection([('V','Ventas de bienes y servicios'),
                                       ('C','Compras de bienes y servicios'),
                                       ('A','Renta'),
                                       ('SP','Servicios profesionales'),
                                       ('M','Comisiones'),
                                       ('I','Intereses')], string="D-151 Codigo")
                                       
	code_buy = fields.fields.selection([('V','Ventas de bienes y servicios'),
                                       ('C','Compras de bienes y servicios'),
                                       ('A','Renta'),
                                       ('SP','Servicios profesionales'),
                                       ('M','Comisiones'),
                                       ('I','Intereses')], string="D-151 Codigo")



