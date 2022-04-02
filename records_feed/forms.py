from pyexpat import model
from django import forms
from .models import Setter


# class SetterModelForm(forms.ModelForm):
#     class Meta:
#         model = Setter
#         fields = (
#             "name",
#             "last_name",
#             "email",
#             "message",
#             "contact_number",
#             "agent",
#         )



class Users_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    contact_number = forms.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super(Users_form, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs = {
            "id": "myCustomId",
            "class": "input-text js-input",
            "name": "name"
        }
        self.fields["last_name"].widget.attrs = {
            "id": "lastName",
            "class": "input-text js-input",
            "name": "last_name"
        }
        self.fields["email"].widget.attrs = {
            "id": "email",
            "class": "input-text js-input",
            "name": "Email"
        }
        self.fields["message"].widget.attrs = {
            "id": "Text",
            "class": "input-text js-input",
            "name": "message"
        }
        self.fields["contact_number"].widget.attrs = {
            "id": "Text",
            "class": "input-text js-input",
            "name": "Text",
        }
