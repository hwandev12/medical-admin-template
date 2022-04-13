from django.urls import path
from .views import *

app_name = 'agents'

urlpatterns = [
    path('', AgentsListView.as_view(), name='agent-lists'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'),
    path('agent-create/', AgentCreateView.as_view(), name='agent-create'),
]