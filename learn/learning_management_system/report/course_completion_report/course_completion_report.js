// Copyright (c) 2025, Aparna and contributors
// For license information, please see license.txt

frappe.query_reports["Course Completion Report"] = {
    "filters": [
        {
            "fieldname": "progress",
            "label": __("Progress (%)"),
            "fieldtype": "Percent",
            "reqd": 0,
            "default": ""
        },
        {
            "fieldname": "status",
            "label": __("Status"),
            "fieldtype": "Select",
            "options": "\nIn Progress\nCompleted\nDropped", // Add all your status options here
            "reqd": 0,
            "default": ""
        },
        {
            "fieldname": "grade",
            "label": __("Grade"),
            "fieldtype": "Data",
            "reqd": 0,
            "default": ""
        }
        // Add additional filters as needed, for course or date ranges etc.
    ]
};

