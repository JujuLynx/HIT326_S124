from django.db import models


class TeamMember:
    def __init__(self, full_name, student_number, email_address):
        self.full_name = full_name
        self.student_number = student_number
        self.email_address = email_address