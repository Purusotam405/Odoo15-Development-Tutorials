# from odoo import api, fields, models
#
#
# class AllPatietReport(models.AbstractModel):
#     _name = 'report.hospital_management_system.report_all_patient_list'
#     _description = 'Patient Report'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         docs = self.env['hospital.patient'].search([])
#         return {
#             'docs': docs
#         }
