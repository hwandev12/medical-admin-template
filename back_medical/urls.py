from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import(
     LoginView,
     LogoutView,
     PasswordResetView,
)
from records_feed.views import HomeView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset-view/', PasswordResetView.as_view(), name='password_reset_view'),
    path('', include('records_feed.urls')),
    path('agents/', include('agents.urls', namespace='agents'))
]
