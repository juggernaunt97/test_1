# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CodeList(models.Model):

    _name = "list.code"
    _description = "list code"
    name_code = fields.Char(string='Detail code')
    date_code = fields.Datetime(string='date code')
    check_code = fields.Char(string='is Code', compute='')

    def update(self):
        is_code = self.env['sale.sale'].sudo().search([])
        for rec in self:
            for rec2 in is_code:
                if rec.name_code == rec2.general_code:
                    rec.check_code = "Used"
                else:
                    rec.check_code = "Available"


