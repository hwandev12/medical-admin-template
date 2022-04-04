from pyexpat import model
from django import forms
from .models import Setter


class SetterModelForm(forms.ModelForm):
    class Meta:
        model = Setter
        fields = (
            "name",
            "last_name",
            "email",
            "message",
            "contact_number",
            "agent",
        )
