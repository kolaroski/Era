from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name: models.CharField = models.CharField(
        max_length=32, unique=True, primary_key=True)
    users = models.ManyToManyField(User, null=True)
