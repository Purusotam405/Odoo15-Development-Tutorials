from odoo import api, fields, models, _


class AppointmentReportWizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Print Appointment Wizard"

    patient_id = fields.Many2one('hospital.patient', string="Name")
    # eid = fields.Many2one('hospital.patient', string="EID")
    # cid = fields.Many2one('hospital.patient', string="CID")
    # age = fields.Many2one('hospital.patient', string="Age`")
    # gender = fields.Many2one('hospital.patient', string="gender")
    # designation = fields.Many2one('hospital.patient', string="Designation")
    # department = fields.Many2one('hospital.patient', string="Department/Branch/Division/Unit")
    # dob = fields.Many2one('hospital.patient', string="D.O.B")
    # blood_group = fields.Many2one('hospital.patient', string="Blood Group")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_print_excel_report(self):
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date_appointment', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('date_appointment', '<=', date_to)]

        appointments = self.env['hospital.appointment'].search_read([])
        print('appointments', appointments)

        data = {
            'appointments': appointments,
            'form_data': self.read()[0]
        }
        return self.env.ref('hospital_management_system.report_appointment_xls').report_action(self, data=data)

    def action_print_report(self):
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date_appointment', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('date_appointment', '<=', date_to)]

        appointments = self.env['hospital.appointment'].search(domain)
        print('appointments', appointments)
        appointment_list = []
        for appointment in appointments:
            vals = {
                'name': appointment.name,
                'note': appointment.note,
                'age': appointment.age

            }
            appointment_list.append(vals)
        data = {
            'form_data': self.read()[0],
            'appointments': appointment_list

        }
        return self.env.ref('hospital_management_system.action_report_appointment').report_action(self, data=data)
