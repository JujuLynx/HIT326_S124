from django.db import models
from django.contrib.auth.models import User

class TeamMember:
    def __init__(self, full_name, student_number, email_address):
        self.full_name = full_name
        self.student_number = student_number
        self.email_address = email_address

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
