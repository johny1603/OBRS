from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError, Warning
from odoo.osv import expression
from lxml import etree
import json
import datetime

class BookingLine(models.Model):
    _name = "booking.line"
    _rec_name = "bike_id"

    bike_id = fields.Many2one("bikes.details", string="Bike")
    current_meter = fields.Char(related="bike_id.current_kilo", string="Cur Reading", required=True)
    given_meter = fields.Char(string="Given Reading")
    damage = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Damage")
    days = fields.Integer(string="Days")
    discount = fields.Integer(string="Discount")
    cost = fields.Integer(related="bike_id.amount_per",string="Cost")
    amount = fields.Integer(string="Sub Total", compute="_calculate_subtotal", store=True)
    booking_id = fields.Many2one("booking.details", string="Booking")

    @api.depends('days', 'cost')
    def _calculate_subtotal(self):
        print("depends")
        self.amount = False
        for rec in self:
            if rec.days and rec.cost:
                rec.amount = rec.cost * rec.days
