from __future__ import unicode_literals
from datetime import *
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Todo1(models.Model):
#     title = models.CharField(max_length=200, null=True)
#     text = models.TextField(null=True)
#     create_at = models.DateTimeField(default=datetime.now)

#     def __str__(self):
#         return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = u'User profiles'
