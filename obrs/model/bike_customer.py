import re
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError, Warning
from odoo.osv import expression
from lxml import etree
import json

class Customer(models.Model):
    _name = "customer.details"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Mobile No", required=True)
    dob = fields.Date(string="Date of Birth")
    age = fields.Char(string="Age",compute="_calculate_age",store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    mail = fields.Char(string="E Mail")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip_code = fields.Char(string="Zip Code")
    state = fields.Many2one('res.country.state',string="State")
    dl_no = fields.Char(string="DL No")
    proof = fields.Selection([('aadhar_card', 'Aadhar Card'),('voter id','Voter Id')])
    upload = fields.Binary(string="proof Upload")


    # --------------Name get ORM---------------------
    def name_get(self):
        var = []
        for rec in self:
            if rec.name and rec.phone:
                name = rec.name + ' (' + rec.phone + ')'
                var.append((rec.id, name))
        return var

    # ----------Phone Number Validation in Customer using constatints------------------

    @api.constrains("phone")
    def _check_phone(self):
        for rec in self:
            if rec.phone.isdigit():
                if len(rec.phone) != 10:
                    raise UserError("Enter the 10 digit valid phone number")
            else:
                raise UserError("Enter digit values")

    # --------------------------E-mail Validation in using constaints---------------
    @api.onchange('mail')
    def validate_mail(self):
        if self.mail:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.mail)
            if match == None:
                raise ValidationError('Your Mail is Not Valid...')

    # -------------Depends decorator using in bike table-----------------

    @api.depends("dob")
    def _calculate_age(self):
        print("Age calculate method called")
        self.age = False
        if self.dob:
            today = fields.date.today()
            year = today.year
            self.age = year - self.dob.year


# Client action method
    @api.model
    def get_customer_details(self):
        print("Python Call")
        val = []
        data = self.env['customer.details'].search([])
        for dt in data:
            val.append((dt.name, dt.dob, dt.phone, dt.mail, dt.city))
            print(dt)
            print(val)
        return val

# mail send method
    def send_mail(self):
        print("cron called")
        template = self.env.ref('obrs.send_mail_template')
        if template:
            template.with_context(name="I am context's value").send_mail(self.id, force_send=True)
        else:
            print("Mail Could not be sent....!")

# Url action render customer data
    def get_customer(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'http://localhost:8069/customer',
            'target': 'new'
        }
    # URL ACtion in Customer Registration

    def cus_registration(self):
         return {
            'type': 'ir.actions.act_url',
            'url': 'http://localhost:8069/add_customer',
            'target': 'new'
        }









