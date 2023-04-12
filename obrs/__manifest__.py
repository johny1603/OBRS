{
    'name' : 'OBRS',
    'version' : '1.1',
    'summary': 'Bike Rental Information',
    'sequence': 1,
    'description': """
    """,
    'category': 'Bike',
    'website': '',
    'images' : [],
    'depends' : ['mail','website','base'],
    'data': [
        'security/security_role.xml',
        'security/ir.model.access.csv',
        'data/office_master.xml',
        'data/pay_sequence.xml',
        'data/bike_controller.xml',
        'data/booking_controller.xml',

        'data/controller_template.xml',
        'data/email_template.xml',
        'data/sample_server_action.xml',


        'views/report/report.xml',
        'views/report/invoice_report.xml',


        'views/bike_details_view.xml',
        'views/bike_customer.xml',
        'views/bike_employee.xml',
        'views/bike_booking.xml',
        'views/bike_booking_line.xml',
        'views/bike_payment.xml',
        'views/bike_office.xml',
        'views/client_action.xml',
        'views/menu.xml',

        'wizard/booking_report.xml',
        'wizard/bike_available.xml',
    ],
    'demo': [
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}