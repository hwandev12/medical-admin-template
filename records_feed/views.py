from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404


def feedback_users(request):
    setters = models.Setter.objects.all()
    context = {"setters": setters}
    return render(request, 'feedback_users.html', context)


def select_info(request, pk):
    feedback = get_object_or_404(models.Setter, id=pk)
    return render(request, 'details/feedback_details.html')
