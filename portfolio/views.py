# portfolio/views.py
from django.views.generic import TemplateView, DetailView

from .models import FeaturedProject, QuickProject


class PortfolioListView(TemplateView):
    template_name = "portfolio/portfolio-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # query Featured Projects here
        context['featured_projects'] = FeaturedProject.objects.all()
        # query Quick Projects here
        context['quick_projects'] = QuickProject.objects.all()
        return context
    
class FeaturedProjectDetailView(DetailView):
    model = FeaturedProject
    context_object_name = "project"
    template_name = "portfolio/featured-project-detail.html"



class QuickProjectDetailView(DetailView):
    model = QuickProject
    context_object_name = "project"
    template_name = "portfolio/quick-project-detail.html"
