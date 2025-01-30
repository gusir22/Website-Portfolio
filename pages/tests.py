# pages/test.py
from datetime import datetime

from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse, resolve

from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ContactSuccessPageView,
)
from .forms import ContactForm
from education_certificates.models import Certificate


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, "Hello there,")

    def test_homepage_url_resolves_homepageview(self):
        """Tests that the url pattern references the correct view"""
        view = resolve(reverse("home"))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(TestCase):
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
            date_earned=datetime(2025, 1, 25),
            certificate_file=test_file,
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_aboutpage(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertContains(response, "Inspect > Element: me")

    def test_aboutpage_url_resolves_aboutpageview(self):
        """Tests that the url pattern references the correct view"""
        view = resolve(reverse("about"))
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)


class ContactPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests (executed once per test class)"""
        cls.valid_form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "company": "ExampleCorp",
            "phone_number": "123-456-7890",
            "contact_email": "johndoe@example.com",
            "subject": "Inquiry",
            "message": "I have a question about your services.",
            "g-recaptcha-response": "PASSED"  # Required for reCAPTCHA validation
        }

        cls.invalid_form_data = {
            "first_name": "John",
            "last_name": "",
            "company": "ExampleCorp",
            "phone_number": "1234567890",  # Invalid phone number format
            "contact_email": "invalid-email",  # Invalid email
            "subject": "",
            "message": "",
            "g-recaptcha-response": "PASSED"  # Required for reCAPTCHA validation
        }

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    @override_settings(DEFAULT_FROM_EMAIL="admin@example.com", CONTACT_EMAIL="admin@example.com")
    def test_fully_valid_data_redirects_to_correct_location_and_sends_email_notice(self):
        """Ensures that the form contact success redirects to /contact/success/"""
        response = self.client.post(reverse("contact"), self.valid_form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("contact_success"))

        # Check that an email was sent
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        # Validate email content
        self.assertEqual(email.subject, "Contact Request: Inquiry")
        self.assertEqual(email.to, ["admin@example.com"])
        self.assertIn("Doe, John", email.body)
        self.assertIn("ExampleCorp", email.body)
        self.assertIn("123-456-7890", email.body)
        self.assertIn("johndoe@example.com", email.body)
        self.assertIn("I have a question about your services.", email.body)
