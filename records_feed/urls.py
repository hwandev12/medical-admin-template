from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('customers/', feedback_users, name='customers'),
    path('<int:pk>/', select_info),
    path('<int:pk>/update/', update_user),
    path('<int:pk>/delete/', delete_user),
    path('create/', create_user)
]