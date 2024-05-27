# Copyright (c) 2024, export_contract and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ForwardContract(Document):
	@frappe.whitelist()
	def calset(self):
		self.childcalset()



	@frappe.whitelist()
	def childcalset(self):
		if self.cancellation_amount != None and self.cancellation_rate != None and self.bank_account != None and self.cancellation_amount != 0.00:
			cancellation_detail = {
				"date": self.cancellation_date,
				"cancel_amount": self.cancellation_amount,
				"rate": self.cancellation_rate,
				"cancellation_profit_loss": self.cancellation_amount
			}
			self.append("cancellation_details", cancellation_detail)
			self.totcalset()
			self.jvent()
			self.cancellation_amount =0,
			self.cancellation_rate = 0,
			self.cancellation_amount = 0
			

		else:
			frappe.throw("Please select cancellation detail")

		



	@frappe.whitelist()
	def totcalset(self):
		rawitemprice = sum(i.cancel_amount for i in self.get("cancellation_details"))
		self.total_cancelled = rawitemprice

	@frappe.whitelist()
	def jvent(self):
		moc = frappe.new_doc("Journal Entry")
		moc.cheque_no = self.name
		moc.cheque_date =self.cancellation_date
		moc.posting_date =self.cancellation_date
		mn = frappe.get_doc("Company",self.company)
		moc.append("accounts",
					{
						"account": mn.exchange_gain_loss_account,
						"credit_in_account_currency":self.cancellation_amount,
					},)
		moc.append("accounts",
					{
						"account": "Advance Income Tax (Ass.Y.2022-2023) - NFPL",
						"debit_in_account_currency":self.cancellation_amount,
					},)
		moc.save()

	

		
	