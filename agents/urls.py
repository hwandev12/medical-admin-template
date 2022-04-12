from django.urls import path
from .views import AgentsListView, AgentCreateView

app_name = 'agents'

urlpatterns = [
    path('', AgentsListView.as_view(), name='agent-lists'),
    path('agent-create/', AgentCreateView.as_view(), name='agent-create'),
]