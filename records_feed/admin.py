from django.contrib import admin
from .models import Setter, User, Agent, UserProfile

admin.site.register(Setter)
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(UserProfile)
