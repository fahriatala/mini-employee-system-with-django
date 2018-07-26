from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length=100)
	information = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class Position(models.Model):
	name = models.CharField(max_length=100)
	information = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class Worker(models.Model):
	GENDER_TYPE_OPTIONS = (
		 ('male','Male'),
		 ('female','Female'),
	)

	WORKER_TYPE_OPTIONS = (
		('internship','Internship'),
		('contract','Contract'),
		('permanent','Permanent'),
		)


	name = models.CharField(max_length=100)
	address = models.TextField(blank=True)
	gender_type = models.CharField(max_length=10, choices=GENDER_TYPE_OPTIONS)
	worker_type = models.CharField(max_length=10, choices=WORKER_TYPE_OPTIONS)
	phonenumber = models.CharField(max_length=30,blank=True)
	email = models.CharField(max_length=100)
	department = models.ForeignKey(Department)
	position = models.ForeignKey(Position)

	def __unicode__(self):
		return self.name

class Account(models.Model):
	ACCOUNT_TYPE_CHOICES =(
		('worker','Worker'),
		('administrator','Administrator')
		)

	account = models.ForeignKey(User)
	worker = models.ForeignKey(Worker)
	account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
		
	def __unicode__(self):
		return self.worker.name