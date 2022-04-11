from django.urls import path
from .views import AgentsListView

app_name = 'agents'

urlpatterns = [
    path('', AgentsListView.as_view(), name='agent-lists')
]