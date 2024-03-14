# myapp/models.py

from django.db import models

class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    # Add other fields as needed
