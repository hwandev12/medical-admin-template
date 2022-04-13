from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# .mixins is actually for agents to show things and hiding
from .mixins import OraniserAndLoginRequiredMixin
from records_feed.models import Agent
from .forms import AgentCreateModel

class AgentsListView(OraniserAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/lists.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)
    
class AgentCreateView(OraniserAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create.html'
    form_class = AgentCreateModel
    
    def get_success_url(self):
        return reverse('agents:agent-lists')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organiser = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    
class AgentDetailView(OraniserAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/details.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)
    
class AgentUpdateView(OraniserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/update.html'
    form_class = AgentCreateModel
    context_object_name = 'agent'
    
    def get_success_url(self):
        return reverse('agents:agent-lists')
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)
    
class AgentDeleteView(OraniserAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/delete.html'
    context_object_name = 'agent'
    
    def get_success_url(self):
        return reverse('agents:agent-lists')
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)
    
