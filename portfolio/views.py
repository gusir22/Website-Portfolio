# portfolio/views.py
from django.views.generic import TemplateView

from .models import FeaturedProject


class PortfolioListView(TemplateView):
    template_name = "portfolio/portfolio-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # query Featured Projects here
        context['featured_projects'] = FeaturedProject.objects.all()
        # query Quick Projects here

        return context