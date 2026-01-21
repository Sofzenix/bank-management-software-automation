from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    EMPLOYEE = 'EMPLOYEE', 'Employee'
    CUSTOMER = 'CUSTOMER', 'Customer'
class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CUSTOMER
    )

    failed_login_attempts = models.PositiveIntegerField(default=0)
    is_locked = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

"""
Module: Authentication & System Architecture
Owner: T. Malleshwari
Source: Django users/models.py
Purpose: Custom user model with roles and account lock
"""
