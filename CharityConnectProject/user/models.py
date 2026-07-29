from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    # Personal Information
    full_name = models.CharField(max_length=150, blank=True, null=True)
    father_name = models.CharField(max_length=150, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    # Contact Information
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Other Information
    marital_status = models.CharField(max_length=50, blank=True, null=True)

    # Volunteer Program
    volunteer_program = models.CharField(max_length=150, blank=True, null=True)


    def __str__(self):
        return self.user.username
