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
