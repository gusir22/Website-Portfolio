# pages/urls.py
from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ContactSuccessPageView,
)


urlpatterns = [
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("contact/success/", ContactSuccessPageView.as_view(), name="contact_success"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
