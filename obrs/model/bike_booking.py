from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError, Warning
from odoo.osv import expression
from lxml import etree
import json
import datetime

class Booking(models.Model):
    _name = "booking.details"
    _rec_name = "customer_id"

    STATUS_LIST = [('draft', 'Draft'), ('cancel', 'Cancel'), ('confirm', 'Confirm')]

    customer_id = fields.Many2one("customer.details", string="Customer")
    employee_id = fields.Many2one("employee.details", string="Employee")
    booking_date = fields.Datetime(string="Booking Date", default=datetime.datetime.now())
    taken_date = fields.Datetime(string="Taken Date")
    given_date = fields.Datetime(string="Given date")
    booking_status = fields.Selection(STATUS_LIST, required=True, default='draft')
    reason = fields.Selection([('plan_cancel', 'Plan Cancel'), ('over_cost', 'Over Cost'), ('disquieted', 'disquieted')], string="Reason")
    cancel_date = fields.Datetime(string="Cancel Date")
    book_seq = fields.Char(string="Booking Reference", required=True, readonly=True, copy=False, index=True, default=lambda self: _('New'))
    status = fields.Selection([('confirm', 'Confirm'), ('pending', 'Pending'), ('refunded', 'Refunded')], string="Status")
    booking_line_ids = fields.One2many("booking.line", "booking_id", string="Booking Line")
    total = fields.Integer(string="Total", compute="_amount_all", store=True)

    @api.depends('booking_line_ids.amount')
    def _amount_all(self):
        print('Total Calculated')
        self.total = False
        for rec in self:
            total = 0
            for line in rec.booking_line_ids:
                total += line.amount
                rec.update({
                    'total': total,
                })

# -------------Create ORM Using in Booking-------------
    @api.model
    def create(self, vals):
        if vals.get('book_seq', _('New')) == _('New'):
            vals['book_seq'] = self.env['ir.sequence'].next_by_code('book.sequence') or _('New')
        result = super(Booking, self).create(vals)
        return result

    # --------This is status bar----------------

    def action_draft(self):
        if self.booking_status:
            print(self.booking_status)
            self.booking_status = "draft"
    def action_confirm(self):
        if self.booking_status:
            print(self.booking_status)
            self.booking_status = "confirm"
    def action_cancel(self):
        if self.booking_status:
            print(self.booking_status)
            self.booking_status = "cancel"

    def action_send_invoice_mail(self):
        print("mail method called")
        template_id = self.env.ref('obrs.bike_book_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)





