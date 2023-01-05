from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _order = "id desc"

    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        res['gender'] = 'male'
        return res

    name = fields.Char(string='Name', required=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))

    eid = fields.Integer(string='EID', tracking=True)
    cid = fields.Integer(string='CID', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, string="Gender", default="male", tracking=True)
    designation = fields.Many2one('res.partner', String="Designation")
    department = fields.Many2one('res.partner', String="Department/Brand/Division/Unit")
    dob = fields.Date(String="D.O.B")
    blood_group = fields.Char(String="Blood Group")
    parents_detail = fields.Char(String="Parents Details")
    father = fields.Char(String="Father")
    father_cid = fields.Integer(String="Fathers CID")
    mother = fields.Char(String="Mother")
    mother_cid = fields.Integer(String="Mothers CID")
    village = fields.Char(String="Village")
    gewog = fields.Char(String="Gewog")
    dzongkhag = fields.Char(String="Dzongkhag")

    # company = fields.Char(string="Company", tracking=True)
    # website = fields.Char(string="Website", tracking=True)

    # note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default="draft", string="Status",
                             tracking=True)

    # responsible_id = fields.Many2one('res.partner', string="Responsible")
    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count")
    image = fields.Binary(string="Patient_image")

    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')

    # father_name = fields.Char('hospital.patient', string='Fathers Name')
    # date_appointment = fields.Date(string="Date")

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count_id = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count_id

    def action_send_card(self):
        template_id = self.env.ref('hospital_management_system.patient_card_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    def action_confirm(self):
        for rec in self:
            rec.state = "confirm"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_draft(self):
        for rec in self:
            rec.state = "draft"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient.seq') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res

    def copy(self, default=None):
        print('Successfully overriden')
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (COPY)", self.name)
        default['note'] = "Copied Record"
        return super(HospitalPatient, self.copy(default))

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            patients = self.env['hospital.patient'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if patients:
                raise ValidationError(_("Name %s Already Exists" % rec.name))

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError(_("Age cannot be zero"))

    def name_get(self):
        result = []
        for rec in self:
            if not self.env.context.get('hide_code'):
                name = '[' + rec.reference + ']' + rec.name
            else:
                name = rec.name
            result.append((rec.id, name))
            return result

    def action_open_appointments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current'
        }
