{
    'name': 'Hospital Management System',
    'version': '1.0.0',
    'category': 'Hospital',
    'summary': 'Hospital Management System',
    'sequence': -100,
    'description': """ Hospital Management System """,
    'images': [
        'static/description/logo.png'
    ],
    'depends': [
        'sale',
        'mail',
        'report_xlsx'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'wizard/appointment_report_view.xml',
        # 'wizard/all_patient_report_view.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/kids_view.xml',
        'views/partner.xml',
        'views/patient_gender_view.xml',
        'views/sale.xml',
        'report/appointment_details.xml',
        'report/patient_card.xml',
        'report/report.xml',
        # 'report/all_patient_list.xml'


    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}
