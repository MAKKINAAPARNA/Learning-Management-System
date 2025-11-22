# Copyright (c) 2025, Aparna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student(Document):
    def auto_name(self):
        # Set the title (name field) of the document to Full Name
        if self.first_name and self.last_name:
            self.name = f"{self.first_name} {self.last_name}".strip()
        elif self.first_name:
            self.name = self.first_name.strip()
        else:
            self.name = frappe.generate_hash(length=10)

    def before_save(self):
        # Safely handle missing names to avoid "None"
        first = self.first_name or ""
        last = self.last_name or ""
        self.full_name = f"{first} {last}".strip()

        # Fetch current progress; set to 0 if None
        progress = self.progress or 0

        # Set the grade based on progress value
        if progress >= 90:
            self.grade = "A"
        elif progress >= 70:
            self.grade = "B"
        elif progress >= 60:
            self.grade = "C"
        elif progress >= 50:
            self.grade = "D"
        elif progress >= 35:
            self.grade = "E"
        else:
            self.grade = "F"

        # Set the status based on progress value
        if progress >= 100:
            self.status = "Completed"
        elif progress > 0:
            self.status = "In Progress"
        else:
            self.status = "Dropped"

        # Show message
        frappe.msgprint(f"Progress: {progress:.2f}%, Status: {self.status}, Grade: {self.grade}")
