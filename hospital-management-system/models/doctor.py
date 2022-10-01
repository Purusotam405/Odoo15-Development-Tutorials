# -*- coding utf-8 -*-
from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"

    doctor_name = fields.Char(string='Name', required=False)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
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
