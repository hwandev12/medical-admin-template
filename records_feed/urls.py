from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('customers/', feedback_users, name='customers'),
    path('<int:pk>/', select_info),
    path('create/', create_user)
]