# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _name = 'sale.sale'
    _description = 'Sale Order'
    name = fields.Char('Customer name')
    mail = fields.Char('Email')
    phone_number = fields.Char('Phone number')
    group_code = fields.Selection(
        [('vip_10', 'VIP_10'), ('vip_20', 'VIP_20'), ('vip_8', 'VIP_8')], 'group code', default="")
    detail_code = fields.Char('discount voucher')
    total_money = fields.Float('total')
    sale_order_discount_estimated = fields.Float('Used discount', compute='get_cost')
    general_code = fields.Char('general_code', compute='get_code')

    @api.depends('total_money', 'group_code')
    def get_cost(self):
        for rec in self:
            rec.sale_order_discount_estimated = rec.total_money
            if rec.group_code == 'vip_10':
                rec.sale_order_discount_estimated = rec.total_money - rec.total_money*10/100
            elif rec.group_code == 'vip_20':
                rec.sale_order_discount_estimated = rec.total_money - rec.total_money*20/100

    @api.depends('group_code','detail_code')
    def get_code(self):
        for rec in self:
            rec.general_code = ''
            if rec.group_code == 'vip_10':
                rec.general_code = 'VIP_10' + rec.detail_code
            elif rec.group_code == 'vip_20':
                rec.general_code = 'VIP_20' + rec.detail_code

    @api.constrains('group_code')
    def _check_detail_code(self):
        for record in self:

            numcode = record.detail_code

            if numcode.isdigit() == True:
                numcode = int(record.detail_code)
                if numcode <= 0 or numcode > 999999:
                    raise models.ValidationError('must 6 numbers')
            else:
                raise models.ValidationError('not Char !!!')

    @api.model
    def action_plus(self):
        for rec in self:
            rec.general_code = "used"
        return {"type": "set_scrollTop"}

