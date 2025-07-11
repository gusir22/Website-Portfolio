# pages/views.py
from datetime import datetime

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy

from education_certificates.models import Certificate

from .forms import ContactForm
from .models import Book


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_context'] = "I am a custom context str!"  # add custom context data here
        context['book_list'] = Book.objects.all()  # get all book instances for table
        return context


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get all certificates ordered newest to oldest
        context["certificates_list"] = Certificate.objects.all().order_by("-date_earned")
        return context


class ContactPageView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_success")

    def form_valid(self, form):
        subject = f"Contact Request: {form.cleaned_data['subject']}"
        from_email = settings.DEFAULT_FROM_EMAIL
        date = datetime.now()  # Get contact request time
        message = f"""
                Contact Request

                Date: {date.strftime("%m/%d/%y %H:%M")}
                ---------------------------------------------------------
                Name: {form.cleaned_data['last_name']}, {form.cleaned_data['first_name']}
                Company: {form.cleaned_data['company']}
                Phone Number: {form.cleaned_data['phone_number']}
                Contact Email: {form.cleaned_data['contact_email']}
                ----------------------------------------------------------

                {form.cleaned_data['message']}

                """
        send_mail(subject, message, from_email, [settings.CONTACT_EMAIL], fail_silently=False)
        return super().form_valid(form)


class ContactSuccessPageView(TemplateView):
    template_name = "pages/contact_success.html"
