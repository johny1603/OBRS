from odoo import fields, models, api
from datetime import datetime
from odoo .exceptions import UserError


class DateReport(models.AbstractModel):
    _name = 'report.obrs.booking_date_template'

    # here 'report.passengers.field.report' is folder_name, addon_name and template_name

    def get_data(self, form_values):
        data = []
        from_date = form_values['from_date']
        to_date = form_values['to_date']
        total_all = 0

        # here we are using query to get data instead if search ORM
        # sql = """ SELECT
        #                 bo.book_seq, cu.name, cu.phone, cu.mail, bo.booking_date, bo.total, bo.booking_status
        #             FROM
        #                 booking_details as bo
        #             LEFT JOIN
        #                 customer_details as cu
        #             ON
        #                 cu.id = bo.customer_id"""
        # self.env.cr.execute(sql, (tuple(self.ids),))
        # results = self.env.cr.dictfetchall()
        # print("results")
        # print(results)

        if form_values['from_date'] or form_values['to_date']:
            recordsets = self.env['booking.details'].search(
                [('booking_date', '>=', form_values['from_date']), ('booking_date', '<=', form_values['to_date'])])

            print("recordsets")
            print(recordsets)

        for obj in recordsets:
            if obj.total:
                total_all += obj.total
        print(total_all)
        for rec in recordsets:
            data.append({'book_seq': rec.book_seq,
                         'name': rec.customer_id.name,
                         'phone': rec.customer_id.phone,
                         'mail': rec.customer_id.mail,
                         'booking_date': rec.booking_date,
                         'total': rec.total,})
        # for rec in recordsets:
        #     rec['total_all'] = total_all
        # data.append({'total_all':total_all})
        print(data)


        return data

    @api.model
    def _get_report_values(self, docsids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        # print(self.total_all)
        return {
            'doc_ids': docsids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'get_data': self.get_data(data['form']),
        }
