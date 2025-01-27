# education_certificates/models.py
from django.db import models


class Certificate(models.Model):
    """Represents certificates earned from any course"""
    title = models.CharField(max_length=60)  # name/title of course
    institution_name = models.CharField(max_length=60)  # name of institution issuing certificate
    date_earned = models.DateField()  # date when certificate was earned
    certificate_file = models.FileField(upload_to='uploads/')  # certificate file

    def __str__(self):
        return f"{self.title[:15]} | {self.institution_name[:15]}"
