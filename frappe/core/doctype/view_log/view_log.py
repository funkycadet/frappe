# Copyright (c) 2018, Frappe Technologies and contributors
# License: MIT. See LICENSE

import frappe
from frappe.model.document import Document


class ViewLog(Document):
	@staticmethod
	def clear_old_logs(days=180):
		from frappe.query_builder import Interval
		from frappe.query_builder.functions import Now

		table = frappe.qb.DocType("View Log")
		frappe.db.delete(table, filters=(table.modified < (Now() - Interval(days=days))))
