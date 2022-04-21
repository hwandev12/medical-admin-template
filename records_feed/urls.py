from django.urls import path
from .views import *

app_name = 'feedback'

urlpatterns = [
    path('customers/', FeedbackUsers.as_view(), name='customers'),
    path('<int:pk>/', SelectInfo.as_view(), name='user_info'),
    path('<int:pk>/update/', UpdateUser.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete'),
    path('<int:pk>/assign-agent/', AgentAssignView.as_view(), name='assign_agent'),
    path('create/', CreateUser.as_view(), name='create'),
    path('loggedout/', LoggedOut.as_view(), name='loggedout'),
    path('category-lists/', AssignCategoryView.as_view(), name='category'),
]
