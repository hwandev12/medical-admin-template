from django.urls import path
from .views import *

urlpatterns = [
    path('', feedback_users, name='customers'),
    path('<pk>/', select_info)
]