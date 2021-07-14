from odoo import api, models, fields


class MassUpdateCode(models.TransientModel):
    _name = 'list.code.update.wizard'

    _description = 'Mass Update Customer Code'

    customer_discount_code = fields.Text(string="Discount code")

    def update(self):
        pass


