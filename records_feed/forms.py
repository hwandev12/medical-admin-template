from pyexpat import model
from django import forms
from .models import Setter
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
