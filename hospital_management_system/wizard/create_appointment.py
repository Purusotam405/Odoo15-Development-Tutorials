from odoo import api, fields, models, _


class CreateAppointmentwizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    date_appointment = fields.Date(string='Date')
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)

    def action_create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment,
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        print("appointment", "appointment_rec.id")
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id

        }

    def action_view_appointment(self):
        # method1
        action = self.env.ref('hospital_management_system.appointment_action').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action

        # # method2
        # action = self.env['ir.actions.actions']._for_xml_id("hospital_management_system.action_hospital_appointment")
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action

        # method3

        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'Appointments',
        #     'res_model': 'hospital.appointment',
        #     'xml': 'form',
        #     'view_mode': 'tree,from',
        #     'target': 'current',
        # }
        #
        # return action
