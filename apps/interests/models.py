from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    interest = models.CharField(max_length=30)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)


class Interest(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, related_name="userinterest")
    interest = models.ForeignKey('User', models.DO_NOTHING, related_name="interestinterest")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
