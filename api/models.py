from __future__ import unicode_literals

from django.db import models
from django.core.validators import *
from django.contrib.auth.models import *
from django.contrib import admin

# Create your models here.
	
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	roles = models.CharField(max_length=200, blank=False, default="{\"admin\": false, \"researcher\": false, \"subject\": true}")
	gender = models.CharField(max_length=100, blank=False)
	age = models.IntegerField(blank=False)
	educationlevel = models.CharField(max_length=200, blank=False)
	city = models.CharField(max_length=200, blank=False)
	state = models.CharField(max_length=200, blank=False)
	ip = models.CharField(max_length=200, blank=False)
	
	def __str__(self):
		return self.user.username

	class Admin(admin.ModelAdmin):
		list_display = ('user',)

	class JSONAPIMeta:
		resource_name = "profiles"


class Cloth(models.Model):
	name = models.CharField(max_length=200, blank=False)
	#roles = models.CharField(max_length=200, blank=False, default="{\"admin\": false, \"researcher\": false, \"subject\": true}")
	price = models.CharField(max_length=100, blank=False)
	#age = models.IntegerField(blank=False)
	size = models.CharField(max_length=200, blank=False)
	image = models.CharField(max_length=500, blank=False)
	#state = models.CharField(max_length=200, blank=False)
	#ip = models.CharField(max_length=200, blank=False)
	
	def __str__(self):
		return self.name

	class Admin(admin.ModelAdmin):
		list_display = ('name',)

	class JSONAPIMeta:
		resource_name = "cloth"
