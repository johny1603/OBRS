from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import UserError

STATUS_LIST = [('available', 'Available'), ('not_available', 'Non Available')]


class CustomerGenderWizard(models.TransientModel):

    _name = "bike.wizard"
    _description = "bike wizard report"

    status = fields.Selection(STATUS_LIST, string="Status")

    def available_bike_report(self):
        self.ensure_one()
        data = {}
        data['ids'] = self.env.context.get('active_ids', [])
        data['active_model'] = self.env.context.get('active_model','ir.ui.menu')
        data['form'] = self.read(['status'])[0]
        return self.env.ref('obrs.bike_available_report_action').report_action(self, data=data)













