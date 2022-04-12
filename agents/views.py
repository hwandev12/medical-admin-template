from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from records_feed.models import Agent
from .forms import AgentCreateModel

class AgentsListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/lists.html'
    
    def get_queryset(self):
        return Agent.objects.all()
    
class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create.html'
    form_class = AgentCreateModel
    
    def get_success_url(self):
        return reverse('agents:agent-lists')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.profile = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
