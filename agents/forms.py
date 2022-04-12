from dataclasses import fields
from django import forms
from records_feed.models import Agent

class AgentCreateModel(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )