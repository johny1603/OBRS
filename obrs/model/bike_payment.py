from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError, Warning
from odoo.osv import expression
from lxml import etree
import json
import datetime

class Payment(models.Model):
    _name = "payment.details"
    _rec_name = "booking_id"

    booking_id = fields.Many2one("booking.details", string="Booking Name")
    payment_type = fields.Selection([('online','Online'),('cod','Cash in Hand')])
    payment_date = fields.Datetime(string="Date",default=datetime.datetime.now())
    payment_status = fields.Selection([('paid','Paid'),('unpaid','Unpaid')])
    amount = fields.Integer(string="Amount",related="booking_id.total",readonly=True)
    ref_code = fields.Char(string="Reference Code")

    @api.model
    def create(self, vals):
        print(vals)
        vals['ref_code'] = self.env['ir.sequence'].next_by_code('payment.seq')
        return super(Payment, self).create(vals)




