from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from . import models
from django.shortcuts import get_object_or_404
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
    form = SetterModelForm()
    if request.method == "POST":
        form = SetterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(request, 'create.html', context)


def update_user(request, pk):
    customer = models.Setter.objects.get(id=pk)
    form = SetterModelForm(instance=customer)
    if request.method == 'POST':
        form = SetterModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"form": form, "customer": customer}
    return render(request, 'update.html', context)

def delete_user(request, pk):
    customer =  get_object_or_404(Setter, id=pk)
    customer.delete()
    return redirect('/')