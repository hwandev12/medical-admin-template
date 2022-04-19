from pyexpat import model
from django import forms
from .models import Agent, Setter
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


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


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", )
        field_classes = {'username': UsernameField}
        
class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = Agent.objects.filter(organiser=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents
# Bu AssignaAgentForm da agenti yo'qni aniqlash va t
