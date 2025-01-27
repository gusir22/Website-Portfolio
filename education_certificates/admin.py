# education_certificates/admin.py
from django.contrib import admin

from .models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
    ]

    list_filter = [
        "institution_name",
        "date_earned",
    ]

    search_fields = [
        "institution_name",
        "date_earned",
    ]

admin.site.register(Certificate, CertificateAdmin)
