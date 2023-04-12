from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning


class DateWizard(models.TransientModel):
    _name = 'date.wizard'
    _description = "This is the table for Date wizard"

    from_date = fields.Datetime(string="From Date", required=True)
    to_date = fields.Datetime(string="To Date", required=True)

    # CONSTRAINS DEOCRATOR
    @api.constrains('from_date', 'to_date')
    def validate_date(self):
        if self.from_date and self.to_date and not self.from_date <= self.to_date:
            raise ValidationError("Enter Futurastic date")


    def fetch_booking_details(self):
        self.ensure_one()
        data = {}
        data['ids'] = self.env.context.get('acive_ids', [])
        data['active_model'] = self.env.context.get('active_model', 'ir.ui.menu')
        data['form'] = self.read(['from_date', 'to_date'])[0]
        return self.env.ref('obrs.booking_report').report_action(self, data=data)


