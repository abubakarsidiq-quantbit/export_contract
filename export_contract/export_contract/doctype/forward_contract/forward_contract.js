// Copyright (c) 2024, export_contract and contributors
// For license information, please see license.txt
frappe.ui.form.on('Forward Contract', {
	add_cancellation_details(frm){
		frm.call	({
			method:"calset",
			doc:frm.doc,
		})
	}
});

// frappe.ui.form.on('Forward Contract', {
//     add_cancellation_details: function(frm) {
//         frm.doc.cancellation_details.forEach(function(cancel_det) {
//             cancel_det.date = frm.doc.cancellation_date;
//         });
//         frm.refresh_field('cancellation_details');
//     }
// });



frappe.ui.form.on('Forward Contract', { amount_usd_book: function (frm, cdt, cdn) {
		var outstd = frm.doc.amount_usd_book
        var row =(frm.doc.amount_usd_book * frm.doc.current_rate);
            frappe.model.set_value(cdt, cdn, 'outstanding_inr', row);
			frappe.model.set_value(cdt, cdn, 'amount_outstanding', outstd);
    }});
frappe.ui.form.on('Forward Contract', { current_rate: function (frm, cdt, cdn) {
		var borate = frm.doc.current_rate
        var row =(frm.doc.amount_usd_book * frm.doc.current_rate);
            frappe.model.set_value(cdt, cdn, 'outstanding_inr', row);
			frappe.model.set_value(cdt, cdn, 'booking_rate', borate);
    }});

frappe.ui.form.on('Forward Contract', {
	maturity_from: function(frm, cdt, cdn) {
		var days_diff = frappe.datetime.get_day_diff(frm.doc.maturity_to, frm.doc.maturity_from) + 1;
		frappe.model.set_value(cdt, cdn, 'days_of_premium', days_diff);
	}
});
frappe.ui.form.on('Forward Contract', {
	maturity_to: function(frm, cdt, cdn) {
		var days_diff = frappe.datetime.get_day_diff(frm.doc.maturity_to, frm.doc.maturity_from) + 1;
		frappe.model.set_value(cdt, cdn, 'days_of_premium', days_diff);
	}
});






