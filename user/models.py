from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True, null=True)
    qualification = models.CharField(max_length=100)
    password = models.CharField(max_length=10, default="pass")
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
