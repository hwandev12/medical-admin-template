from django.contrib import admin
from django.urls import path, include
from records_feed.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('', include('records_feed.urls'))
]
