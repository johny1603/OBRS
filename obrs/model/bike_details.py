from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError, Warning
from odoo.osv import expression
from lxml import etree
import json


class Bike(models.Model):
    _name = "bikes.details"

    STATUS_LIST = [('available', 'Available'), ('not_available', 'Non Available')]

    name = fields.Char(string="Name")
    model = fields.Char(string="Model Year")
    bike_number = fields.Char(string="Bike Number")
    bike_type = fields.Selection([('gear_bike', 'Gear bike'), ('scooty', 'Scooty')], string="Bike Type")
    fuel_type = fields.Selection([('petrol', 'Petrol'), ('diesel', 'Diesel')], string="Fuel Type")
    bike_con = fields.Boolean(string="Good Condition", default=True)
    color = fields.Char(string="Colour")
    bike_cc = fields.Char(string="Bike CC")
    bike_status = fields.Selection(STATUS_LIST, default='not_available', string="Status")
    current_kilo = fields.Char(string="Kilometer", default="0kms")
    image_123 = fields.Image(string="Image")
    amount_per = fields.Integer(string="Amount")

# ---------------------Stausbar action redirect----------------
    def action_status_available(self):
        for rec in self:
            if rec.bike_status == 'not_available':
                rec.action_available()

    # ------------- Name get ORM-----------------
    # def name_get(self):
    #     var = []
    #     for rec in self:
    #         if rec.name and rec.bike_cc:
    #             name = rec.name + ' (' + rec.bike_cc + ')'
    #             var.append((rec.id, name))
    #     return var

    # --------------------- Unlink Orm---------------------------
    def unlink(self):
        for rec in self:
            if rec.bike_con == 1:
                raise ValidationError(_("You cannot delete Good Condition bikes"))
            return super(Bike, self).unlink()

        # ----------------------- THIS IS for STATUS BAR-----------------------------------------------------------------
    def action_non_available(self):
        if self.bike_status:
            print(self.bike_status)
            self.bike_status = "not_available"

    def action_available(self):
        if self.bike_status:
            print(self.bike_status)
            self.bike_status = "available"

    # ------------cost Validation using decorator---------------
    @api.constrains('amount_per')
    def validate_cost(self):
        print('cost validated')
        if self.amount_per:
            for rec in self:
                print(rec.amount_per)
                if rec.amount_per < 0.00 or not rec.amount_per:
                    raise ValidationError("Please Enter a valid cost")

    def available_bike(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'http://localhost:8069/bike',
            'target': 'new'
        }

