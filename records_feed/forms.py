from email import message
from django import forms
from django_countries.fields import CountryField


class Users_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    contact_number = forms.CharField(max_length=30)
    country = CountryField().formfield()
        
    def __init__(self, *args, **kwargs):
        super(Users_form, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs={
                "id": "myCustomId",
                "class": "input-text js-input",
                "name": "myCustomName"
            }
        self.fields["last_name"].widget.attrs={
                "id": "lastName",
                "class": "input-text js-input",
                "name": "myCustomName"
            }
        self.fields["email"].widget.attrs={
                "id": "email",
                "class": "input-text js-input",
                "name": "Email"
            }
        self.fields["message"].widget.attrs={
                "id": "Text",
                "class": "input-text js-input",
                "name": "Text"
            }
        self.fields["contact_number"].widget.attrs={
                "id": "Text",
                "class": "input-text js-input",
                "name": "Text",
            }
        self.fields["country"].widget.attrs={
                "id": "Text",
                "class": "input-text js-input",
                "name": "Text",
            }