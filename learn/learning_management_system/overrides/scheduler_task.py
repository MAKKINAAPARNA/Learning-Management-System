import frappe

def send_weekly_student_plan():
    # Fetch all active students
    students = frappe.get_all("Student", fields=["full_name", "email_id"], filters={"status": "In Progress"})

    for s in students:
        # Compose the weekly message
        subject = "Your Weekly Study Plan"
        message = f"""
        Hello {s.full_name},  
        Here is your study plan for this week.  
        Stay consistent and keep learning!
        """

        # Send Email
        frappe.sendmail(
            recipients=[s.email],
            subject=subject,
            message=message
        )

    frappe.logger().info("Weekly student planning email sent.")
