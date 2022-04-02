from email import message
from django.shortcuts import redirect, render
from . import models
from django.shortcuts import get_object_or_404
from django_countries.fields import CountryField
from .forms import *


def home(request):
    return render(request, 'base.html')


def feedback_users(request):
    setters = models.Setter.objects.all()
    context = {"setters": setters}
    return render(request, 'feedback_users.html', context)


def select_info(request, pk):
    feedback = get_object_or_404(models.Setter, id=pk)
    context = {"feedback": feedback}
    return render(request, 'details/feedback_details.html', context)


def create_user(request):
    form = Users_form()
    if request.method == "POST":
        form = Users_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact_number = form.cleaned_data['contact_number']
            agent = models.Agent.objects.first()
            models.Setter.objects.create(
                name=name,
                last_name=last_name,
                email=email,
                message=message,
                contact_number=contact_number,
                agent=agent
            )
            return redirect('/')
    context = {
        "form": form 
    }
    return render(request, 'create.html', context)
