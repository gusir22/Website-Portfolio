# portfolio/views.py
from django.views.generic import TemplateView


class PortfolioListView(TemplateView):
    template_name = "portfolio/portfolio-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # query Featured Projects here
        # query Quick Projects here
        return context