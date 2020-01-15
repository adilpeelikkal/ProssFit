from django.db import models

# Create your models here.


class Player(models.Model):

	first_name = models.CharField(max_length=501)
	last_name = models.CharField(max_length=501)
	profile_photo = models.CharField(max_length=254)
	email = models.EmailField(max_length=501)
	age = models.IntegerField(null=True, blank=True)
	phone = models.IntegerField(null=True, blank=True)