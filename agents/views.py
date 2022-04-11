from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from records_feed.models import Agent

class AgentsListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/lists.html'
    
    def get_queryset(self):
        return Agent.objects.all()
