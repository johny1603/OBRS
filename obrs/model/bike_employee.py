import re
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError, Warning
from odoo.osv import expression
from lxml import etree
import json

class Employee(models.Model):
    _name = "employee.details"
    _inherit = ['mail.activity.mixin', 'mail.thread']

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
    mail = fields.Char(string="Email")
    dob = fields.Date(string="Date Of Birth")
    gender = fields.Selection([('male', 'Male'),('female', 'Female'), ('others', 'Others')],string="Gender")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip_code = fields.Char(string="Zip Code")
    state = fields.Many2one("res.country.state", string="State")
    document = fields.Binary(string="Document")
    # picture = fields.Image(string="Picture")

    # -----------------Name Get ORM-----------------------
    def name_get(self):
        var = []
        for rec in self:
            if rec.name and rec.phone:
                name = rec.name + ' (' + rec.phone + ')'
                var.append((rec.id, name))
        return var

    # -------------Check phone number Validation----------------------------

    @api.constrains("phone")
    def _check_phone(self):
        for rec in self:
            if rec.phone.isdigit():
                if len(rec.phone) != 10:
                    raise UserError("Enter the 10 digit valid phone number")
            else:
                raise UserError("Enter digit values")
    # ------------E-Mail Validation Using Decorators.-----------------

    @api.onchange('mail')
    def validate_mail(self):
        if self.mail:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.mail)
            if match == None:
                raise ValidationError('Your Mail is Not Valid...')







