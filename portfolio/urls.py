# portfolio/urls.py
from django.urls import path

from .views import (
    PortfolioListView,
    FeaturedProjectDetailView,
    QuickProjectDetailView,
)


urlpatterns = [
    path("featured-project/<str:slug>/", FeaturedProjectDetailView.as_view(), name="featured_project_detail"),
    path("quick-project/<str:slug>/", QuickProjectDetailView.as_view(), name="quick_project_detail"),
    path("", PortfolioListView.as_view(), name="portfolio_list"),
]
