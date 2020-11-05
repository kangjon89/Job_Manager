from __future__ import unicode_literals
from django.db import models
from login.models import User


class JobManger(models.Manager):
    def trip_validator(self, postData):
        errors = {}

        if len(postData['title']) < 3:
            errors['title'] = "A job must consist of at least 3 characters!"
        if len(postData['description']) < 3:
            errors['description'] = "A description must consist of at least 3 characters!"
        if len(postData['location']) < 3:
            errors['location'] = "A locatoin must be provided"

        return errors

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    catagory = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='job', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManger()

