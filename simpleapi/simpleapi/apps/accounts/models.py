# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils.timezone import now


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    def __len__(self):
        return 1


class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, default='Default')
    creation_date = models.DateField(default=now, editable=False)
    author = models.ForeignKey(CustomUser, null=False, blank=False, editable=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
