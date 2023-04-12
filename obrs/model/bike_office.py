import re
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError, Warning
from odoo.osv import expression
from lxml import etree
import json

class Office(models.Model):
    _name = "office.details"

    name = fields.Char(string="Office Name")
    phone = fields.Char(string="Office Mobile")
    mail = fields.Char(string="Office Mail")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    state_id = fields.Many2one("res.country.state",string="State")
    zip = fields.Char(string="Zip Code")

    @api.model
    def default_get(self, fields):
        var = super(Office, self).default_get(fields)
        var['state_id'] = self.env['res.country.state'].search([('name', '=', 'Tamil Nadu')], limit=10).id
        return var
