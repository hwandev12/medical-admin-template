from email import message
from multiprocessing import context
from re import template
from django.shortcuts import redirect, render, reverse
from . import models
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import get_object_or_404
from .forms import *

class HomeView(TemplateView):
    template_name = 'base.html'
    
class FeedbackUsers(ListView):
    template_name = 'feedback_users.html'
    queryset = models.Setter.objects.all()
    context_object_name = 'setters'
    
    
class SelectInfo(DetailView):
    template_name = 'details/feedback_details.html'
    queryset = models.Setter.objects.all()
    context_object_name = 'feedback'
    
class CreateUser(CreateView):
    template_name = 'create.html'
    form_class = SetterModelForm
    context_object_name = 'form'
    
    def get_success_url(self):
        return reverse('feedback:customers')

class UpdateUser(UpdateView):
    template_name = 'update.html'
    queryset = models.Setter.objects.all()
    form_class = SetterModelForm
    context_object_name = 'customer'
    
    def get_success_url(self):
        return reverse('feedback:customers')
    
class DeleteUser(DeleteView):
    template_name = 'delete.html'
    queryset = models.Setter.objects.all()
    
    def get_success_url(self):
        return reverse('feedback:customers')

class LoggedOut(TemplateView):
    template_name = 'registration/logged_out.html'
    
class RegisterView(CreateUser):
    template_name = 'registration/signup.html'
    form_class = RegisterForm
    
    def get_success_url(self):
        return reverse('feedback:customers')