# pages/test.py
from datetime import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView
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
