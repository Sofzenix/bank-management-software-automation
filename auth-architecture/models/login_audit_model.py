"""
Module: Authentication & System Architecture
Owner: T. Malleshwari
Source: Django audit/models.py
Purpose: Tracks login attempts (SUCCESS / FAILED / LOCKED)
"""


# Create your models here.
from django.conf import settings
from django.db import models


class LoginAudit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.status} - {self.timestamp}"
