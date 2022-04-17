from email import message
from multiprocessing import context
from re import template
from django.shortcuts import redirect, render, reverse
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import get_object_or_404
from .forms import *

class HomeView(TemplateView):
    template_name = 'base.html'
    
class FeedbackUsers(LoginRequiredMixin, ListView):
    template_name = 'feedback_users.html'
    context_object_name = 'setters'
    
    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = models.Setter.objects.filter(organiser=user.userprofile)
        else:
            queryset = models.Setter.objects.filter(organiser=user.agent.organiser)
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset
    
    # Agenti aniqlanmagan foydalanuvchilar uchun
    def get_context_data(self, **kwargs): # Esda tutish
        context = super(FeedbackUsers, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organiser:
            queryset = Setter.objects.filter(
                organiser = user.userprofile,
                agent__isnull = True
            )
        context.update({
            'unassigned_users': queryset
        })
        return context
    # Agenti aniqlanmagan foydalanuvchilar uchun
    
class SelectInfo(LoginRequiredMixin, DetailView):
    template_name = 'details/feedback_details.html'
    queryset = models.Setter.objects.all()
    context_object_name = 'feedback'
    
class CreateUser(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    form_class = SetterModelForm
    context_object_name = 'form'
    
    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organiser = self.request.user.userprofile
        lead.save()
        return super(CreateUser, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('feedback:customers')

class UpdateUser(LoginRequiredMixin, UpdateView):
    template_name = 'update.html'
    queryset = models.Setter.objects.all()
    form_class = SetterModelForm
    context_object_name = 'customer'
    
    def get_success_url(self):
        return reverse('feedback:customers')
    
class DeleteUser(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = models.Setter.objects.all()
    
    def get_success_url(self):
        return reverse('feedback:customers')

class LoggedOut(TemplateView):
    template_name = 'registration/logged_out.html'
    
class RegisterView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm
    
    def get_success_url(self):
        return reverse('feedback:customers')