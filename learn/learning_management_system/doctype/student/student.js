// Copyright (c) 2025, Aparna and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
// 	refresh(frm) {
        
// 	},
// });
frappe.ui.form.on('Test', {
    marks_obtained: function(frm, cdt, cdn) {
        calculate_overall_progress(frm);
    },
    max_marks: function(frm, cdt, cdn) {
        calculate_overall_progress(frm);
    }
});

// Also recalculate progress whenever the Student form loads, or is validated/saved
frappe.ui.form.on('Student', {
    onload: function(frm) {
        calculate_overall_progress(frm);
    },
    validate: function(frm) {
        calculate_overall_progress(frm);
    }
});

// Calculation function: average percentage for all rows in child table
function calculate_overall_progress(frm) {
    let total_percentage = 0;
    let count = 0;
    (frm.doc.test || []).forEach(row => {
        // Parse numbers for safety
        let marks = parseFloat(row.marks_obtained);
        let max = parseFloat(row.max_marks);
        if (!isNaN(marks) && !isNaN(max) && max > 0) {
            total_percentage += (marks / max) * 100;
            count += 1;
        }
    });
    let overall = count > 0 ? (total_percentage / count) : 0;
    frm.set_value('progress', overall);
}
