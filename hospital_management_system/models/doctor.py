# -*- coding utf-8 -*-
from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, string="Gender", tracking=True)

    note = fields.Text(string='Description')
    image = fields.Binary(string="Patient Image")
    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count")
    active = fields.Boolean(string="Active", default="True")
    appointment_ids = fields.Many2many('hospital.appointment', 'hospital_patient_rel', 'doctor_id_rec', 'appointment_id',
                                       string="Appointments")

    date_appointment = fields.Date(string="Date")
    date_time_checkup = fields.Datetime(string="Time_Checkup")

    def copy(self, default=None):
        print('Successfully overriden')
        if default is None:
            default = {}
        if not default.get('doctor_name'):
            default['doctor_name'] = _("%s (COPY)", self.doctor_name)
        default['note'] = "Copied Record"
        return super(HospitalDoctor, self.copy(default))

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count_id = self.env['hospital.appointment'].search_count([('doctor_id', '=', rec.id)])
            rec.appointment_count = appointment_count_id
