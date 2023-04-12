from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import UserError


class WizardReport(models.AbstractModel):
    _name = "report.obrs.bike_report_template"

    def get_data(self,values):
        data, recordsets = [],self.env['bikes.details']
        if values['bike_status']:
            recordsets = recordsets.search([('status','=',values['bike_status'])])

        for record in recordsets:
            data.append({
                'name': record.name,
                'bike_number': record.bike_number,
                'bike_type': record.bike_type,
                'color': record.color,
            })
        return data
    @api.model
    def _get_report_values(self, docids, data=None):
        print("hello")
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        member = self.env['bikes.details'].search([('bike_status','=',data['form']['status'])])
        print(data)
        print(member)
        return {
            'doc_ids': docids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'get_data': member,
        }



