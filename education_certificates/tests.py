# education_certificates/tests.py
from datetime import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .models import Certificate


class CertificateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_file = SimpleUploadedFile(
            name="test_certificate.pdf",
            content=b"fake certificate content",
            content_type="application/pdf",
        )

        cls.certificate = Certificate.objects.create(
            title="A Certificate Title",
            institution_name="Harvard",
            date_earned=datetime(2025, 1,25),
            certificate_file = test_file,
        )

    def test_instance_creation(self):
        """Test that the Certificate instance is created correctly."""
        self.assertEqual(self.certificate.title, "A Certificate Title")
        self.assertEqual(self.certificate.institution_name, "Harvard")
        self.assertEqual(self.certificate.date_earned, datetime(2025, 1,25))
        # Django adds extra chrs at the end of file names to prevent collision
        # We are checking the file name starts with correct dir and file name
        # Then that the file ends with the .pdf file type
        self.assertTrue(self.certificate.certificate_file.name.startswith("uploads/test_certificate"))
        self.assertTrue(self.certificate.certificate_file.name.endswith(".pdf"))

    def test_str_method(self):
        """Test the __str__ method of the Certificate model."""
        expected_str = "A Certificate T | Harvard"
        self.assertEqual(str(self.certificate), expected_str)
