# Copyright (c) 2025, Aparna and contributors
# For license information, please see license.txt

import frappe


import frappe

def execute(filters=None):
    columns = [
        {"label": "Full Name", "fieldname": "full_name", "fieldtype": "Data"},
        {"label": "Enrollment Number", "fieldname": "enrollment_number", "fieldtype": "Data"},
        {"label": "Progress", "fieldname": "progress", "fieldtype": "Percent"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
        {"label": "Grade", "fieldname": "grade", "fieldtype": "Data"},
    ]

    data = get_course_completion_data(filters)
    return columns, data

def get_course_completion_data(filters):
    conditions = ""
    values = {}

    # Dynamic filters based on input
    if filters.get("progress"):
        # Assuming progress is a minimum percentage, customize if you require exact match
        conditions += " AND progress >= %(progress)s"
        values["progress"] = filters["progress"]
    if filters.get("status"):
        conditions += " AND status = %(status)s"
        values["status"] = filters["status"]
    if filters.get("grade"):
        conditions += " AND grade = %(grade)s"
        values["grade"] = filters["grade"]

    query = f"""
        SELECT
            full_name,
            enrollment_number,
            progress,
            status,
            grade
        FROM `tabStudent`
        WHERE 1=1 {conditions}
        ORDER BY progress DESC
    """

    return frappe.db.sql(query, values, as_dict=True)
