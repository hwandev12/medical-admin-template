from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Setter(models.Model):
    
    class Meta:
        verbose_name = "Setter"
        verbose_name_plural = "Feedback users"
        
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    contact_number = models.CharField(max_length=30)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)