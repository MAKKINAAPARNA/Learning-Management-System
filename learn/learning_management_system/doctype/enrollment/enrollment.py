# Copyright (c) 2025, Aparna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Enrollment(Document):

    def validate(self):
        # Get the course capacity
        course_capacity = frappe.db.get_value("Course", self.course, "capacity")

        # Count active enrollments for the course
        active_enrollments = frappe.db.count("Enrollment", filters={
            "course": self.course,
            "status": "Active"
        })

        # Check if enrollment exceeds capacity
        if self.status == "Active" and active_enrollments >= course_capacity:
            frappe.throw(
                f"Cannot enroll: Course capacity of {course_capacity} has been reached."
            )
			

	