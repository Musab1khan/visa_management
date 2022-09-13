# Copyright (c) 2022, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VisaApplication(Document):
	pass

def validate(self,cdt):
	if self.workflow_state == "Approved":
		visa_app_no = self.name	
		emp_name = self.employee
		emp_nationality = self.nationality
		emp_pass = self.passport_number
		emp_visa_type = self.visa_type
		emp_app_date = self.application_date
		emp_expire_date = self.expire_date

		vals = frappe.get_doc({
			"doctype": "Visa Approval History",
			"visa_application_no": visa_app_no,
			"emp_name": emp_name,
			"nationality": emp_nationality,
			"visa_type": emp_visa_type,
			"application_date": emp_app_date,
			"expire_date": emp_expire_date 
		})
		vals.insert()
	if self.workflow_state == "Visa Use":
		visa_app_no = self.name	
		emp_name = self.employee
		emp_nationality = self.nationality
		emp_pass = self.passport_number
		emp_visa_type = self.visa_type
		emp_pass_no = self.passport_number
		emp_app_date = self.application_date
		emp_expire_date = self.expire_date

		vals = frappe.get_doc({
			"doctype": "Visa Use History",
			"visa_application_no": visa_app_no,
			"employee": emp_name,
			"nationality": emp_nationality,
			"visa_type": emp_visa_type,
			"passport_number": emp_pass_no,
			"date": emp_app_date,
			"expire_date": emp_expire_date, 
			"status": self.workflow_state
		})
		vals.insert()
	if self.workflow_state == "Return":
		visa_app_no = self.name	
		emp_name = self.employee
		emp_nationality = self.nationality
		emp_pass = self.passport_number
		emp_visa_type = self.visa_type
		emp_pass_no = self.passport_number
		emp_app_date = self.application_date
		emp_expire_date = self.expire_date

		vals = frappe.get_doc({
			"doctype": "Visa Return History",
			"visa_application_no": visa_app_no,
			"employee": emp_name,
			"nationality": emp_nationality,
			"visa_type": emp_visa_type,
			"passport_number": emp_pass_no,
			"date": emp_app_date,
			"expire_date": emp_expire_date,
			"status": self.workflow_state
		})
		vals.insert()
