from odoo import http, _
from odoo.http import request

class CustomerClass(http.Controller):
#---------- Fetch data in customer details in website-------------------

    @http.route('/customer',auth='public',type='http',website=True)
    def cus_method(self,**kw):
        cus_data = []
        data = request.env['customer.details'].search([])
        for rec in data:
            cus_data.append({
                'Name': rec.name,
                'Phone': rec.phone,
                'Dob': rec.dob,
                'Age': rec.age,
                'Gender': rec.gender,
                'Mail': rec.mail,
                'City': rec.city,
            })
        print(cus_data)
        return request.render("obrs.cus_details",{'cus_data': cus_data})


    @http.route('/add_customer', auth='user', type='http', website=True)
    def booking_reg(self):
        # bike = request.env['bikes.details'].search([])
        # customer = request.env['customer.details'].search([])
        # book = request.env['booking.details'].search([])
        state = request.env['res.country.state'].search([])
        return request.render("obrs.registration_form", {'state':state})

    @http.route('/customer_reg', auth='user', type='http', website=True)
    def new_reg(self, **c):
        name = c['name']
        phone = c['phone']
        dob = c['dob']
        mail = c['mail']
        gender = c['gender']
        street = c['street']
        city = c['city']
        state = c['state']
        zipcode = c['zip_code']
        # bike = c['bike_id']
        # customer = c['customer_id']
        # book = c['booking_id']
        request.env["customer.details"].create({
            'name': name,
            'phone': phone, 'mail': mail, 'dob': dob,
            'gender': gender, 'street': street, 'city': city,
            'state': state, 'zip_code': zipcode,
        })
        return request.render("obrs.create_record",{})



    @http.route('/bike', auth='public', type='http', website=True)
    def bike_method(self, **kw):
        bike_data = []
        data = request.env['bikes.details'].search([('bike_status','=','available')])
        for rec in data:
            bike_data.append({
                'Name': rec.name,
                'Model': rec.model,
                'Bike_number': rec.bike_number,
                'Bike_type': rec.bike_type,
                'Color': rec.color,
                'Bike_cc': rec.bike_cc,
                'Bike_status': rec.bike_status,
            })
        print(bike_data)
        return request.render("obrs.bike_information", {'bike_data': bike_data})
