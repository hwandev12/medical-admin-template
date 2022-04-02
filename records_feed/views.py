from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404
from .forms import Users_form


def home(request):
    return render(request, 'base.html')

def feedback_users(request):
    setters = models.Setter.objects.all()
    context = {"setters": setters}
    return render(request, 'feedback_users.html', context)


def select_info(request, pk):
    feedback = get_object_or_404(models.Setter, id=pk)
    context = {
        "feedback": feedback
    }
    return render(request, 'details/feedback_details.html', context)

def create_user(request):
    print(request.POST)
    context = {
        "forms": Users_form()        
    }
    return render(request, 'create.html', context)
