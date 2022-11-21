# -*- coding utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _order = "doctor_id, name"

    name = fields.Char(string='Name', required=False)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))

    patient_id = fields.Many2one('hospital.patient', String='Patient', required=True)
    patient_name_id = fields.Many2one('hospital.patient', String='Patient Name', required=True)
    age = fields.Integer(string='Age', related="patient_id.age", tracking=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, string="Gender", related="patient_id.gender", tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default="draft", string="Status",
                             tracking=True)

    note = fields.Text(string='Description')

    date_appointment = fields.Date(string="Date")
    date_time_checkup = fields.Datetime(string="Time_Checkup")
    prescription = fields.Text(string='Prescription')
    prescription_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_id',
                                            string="Prescription  Lines")

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_draft(self):
        self.state = "draft"

    def action_cancel(self):
        self.state = "cancel"

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New appointment'
            if vals.get('reference', _('New')) == _('New'):
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

    @api.onchange(patient_id)
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
                if self.patient_id_note:
                    self.note = self.patient_id_note
            else:
                self.patient_id = ""
                self.note = ""

    def unlink(self):
        if self.state == "done":
            raise ValidationError(_("You cannot delete %s as it is in the Done state" % self.name))
        return super(HospitalAppointment, self).unlink()

    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://apps.odoo.com/apps/modules/14.0/%s/' % self.prescription
        }


class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"
    _description = "Appointment Prescription Lines"

    name = fields.Char(string="Medicine", required="True")
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    active = fields.Boolean(string="Active", default="True")
