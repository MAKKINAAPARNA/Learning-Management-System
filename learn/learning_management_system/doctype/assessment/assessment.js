// Copyright (c) 2025, Aparna and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Assessment", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Assessment', {
    test_add: function(frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);
        if (!row.max_marks) row.max_marks = 100;
        if (!row.passing_marks) row.passing_marks = 35;
        frm.refresh_field('test');
    }
});
