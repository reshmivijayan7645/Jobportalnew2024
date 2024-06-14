from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20, default="pass")
    website = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Jobs(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    applied_users = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return self.title
