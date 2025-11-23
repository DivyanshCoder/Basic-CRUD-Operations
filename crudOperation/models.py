from django.db import models

class Notification(models.Model):
    TYPE_CHOICES = (
        ('Email', 'Email'),
        ('SMS', 'SMS'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type}: {self.email} / {self.mobile}"
