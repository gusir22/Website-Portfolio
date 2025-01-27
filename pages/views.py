# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

from education_certificates.models import Certificate


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_context'] = "I am a custom context str!"  # add custom context data here
        return context


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get all certificates ordered newest to oldest
        context["certificates_list"] = Certificate.objects.all().order_by("-date_earned")
        return context
