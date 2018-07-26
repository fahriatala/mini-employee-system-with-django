from __future__ import unicode_literals

from django.db import models
from worker.models import Worker

# Create your models here.
class Presence(models.Model):
    PRESENCE_TYPE_CHOICES = (
        ('permit', 'Permit'),
        ('leave', 'Leave'),
        ('noreason', 'No Reason'),
        ('present', 'Present'),
    )

    worker = models.ForeignKey(Worker)
    presence_type = models.CharField(max_length=20, choices=PRESENCE_TYPE_CHOICES)
    time = models.DateField()

    def __unicode__(self):
        return self.worker.name

class Permit(models.Model):
    PRESENCE_TYPE_CHOICES = (
        ('permit','Permit'),
        ('leave','Leave')
        )

    worker = models.ForeignKey(Worker)
    presence_type = models.CharField(max_length=20, choices=PRESENCE_TYPE_CHOICES)
    begin_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    reason = models.TextField()
    approvement = models.BooleanField(default=False)

    def __unicode__(self):
        return self.worker.name