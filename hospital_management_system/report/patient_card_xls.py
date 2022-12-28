from odoo import models
import base64
import io


class PatientCardXlsx(models.AbstractModel):
    _name = 'report.hospital_management_system.report_patient_id_card_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patient):
        r = 0

        format1 = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'center', })
        sheet = workbook.add_worksheet('Patient Card %s' % (r))
        sheet.set_column('A:A', 22)
        sheet.set_column('B:B', 10)
        sheet.set_column('C:C', 22)
        sheet.set_column('D:D', 15)
        sheet.set_column('E:E', 15)
        sheet.set_column('F:F', 12)
        sheet.set_column('G:G', 15)
        sheet.set_column('H:H', 20)
        sheet.set_column('I:I', 20)
        sheet.set_column('J:J', 10)
        sheet.set_column('K:K', 10)
        sheet.set_column('L:L', 10)
        sheet.set_column('M:M', 10)
        sheet.set_column('N:N', 30)
        sheet.set_column('O:O', 10)
        row = 0
        col = 0
        # sheet.merge_range(row, col, 'Reference', format1)
        sheet.merge_range(row + 2, col, row, col + 1, 'Name', format1)
        sheet.merge_range(row + 2, col + 2, row, col + 3, 'EID', format1)
        sheet.merge_range(row + 2, col + 4, row, col + 5, 'CID', format1)
        sheet.merge_range(row + 2, col + 6, row, col + 7, 'Gender', format1)
        sheet.merge_range(row + 2, col + 8, row, col + 9, 'Designation', format1)
        sheet.merge_range(row + 2, col + 10, row, col + 11, 'Department', format1)
        sheet.merge_range(row + 2, col + 12, row, col + 13, 'D.O.B', format1)
        sheet.merge_range(row + 2, col + 14, row, col + 15, 'Blood Group', format1)
        sheet.merge_range(row + 2, col + 16, row, col + 17, 'Age', format1)
        sheet.merge_range(row + 1, col + 18, row, col + 21, 'Parents Details', format1)
        sheet.merge_range(row, col + 18, row, col + 18, 'Father', format1)
        sheet.merge_range(row + 1, col + 22, row, col + 24, 'Permanent Address', format1)
        sheet.merge_range(row + 1, col + 25, row, col + 28, 'Qualification Details', format1)
        sheet.merge_range(row + 1, col + 29, row, col + 30, 'Marital Status', format1)
        sheet.merge_range(row + 1, col + 31, row, col + 33, 'Spouse Details', format1)
        sheet.merge_range(row + 1, col + 34, row, col + 36, 'Spouse Parents', format1)
        sheet.merge_range(row + 1, col + 37, row, col + 38, 'Childs Details', format1)
        sheet.merge_range(row + 2, col + 39, row, col + 40, 'Personal Email Address', format1)
        sheet.merge_range(row + 1, col + 41, row, col + 42, 'Contact No', format1)

        row += 3
        for patients in patient:
            r += 1
            sheet.write(row, col, patients.name, format2)
            sheet.write(row, col + 1, patients.eid, format2)
            r += 2
            sheet.write(row, col + 2, patients.cid, format2)
            sheet.write(row, col + 3, patients.gender, format2)
            r += 3
            sheet.write(row, col + 4, patients.designation, format2)
            sheet.write(row, col + 5, patients.department, format2)
            r += 4
            sheet.write(row, col + 6, patients.dob, format2)
            sheet.write(row, col + 7, patients.blood_group, format2)
            r += 5
            sheet.write(row, col + 8, patients.age, format2)

            r += 6
            sheet.write(row, col + 9, patients.parents_detail, format2)
            r += 1
            sheet.write(row, col + 9, patients.father, format2)

            # sheet.write(row, col + 11, patients.mother_name, format2)
