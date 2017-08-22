from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Syrup(models.Model):
	name=models.CharField(max_length=50)
	price=models.DecimalField(max_digits=5, decimal_places=3)

	def __str__(self):
		return(self.name)


class Powder(models.Model):
	name=models.CharField(max_length=50)
	price=models.DecimalField(max_digits=5, decimal_places=3)


	def __str__(self):
		return(self.name)

class Beans(models.Model):
	name=models.CharField(max_length=50)
	price=models.DecimalField(max_digits=5, decimal_places=3)


	def __str__(self):
		return(self.name)

class Roast(models.Model):
	name=models.CharField(max_length=50)


	def __str__(self):
		return(self.name)


class Coffee(models.Model):
	user=models.ForeignKey(User)
	name=models.CharField(max_length=50)
	powder=models.ManyToManyField(Powder)
	syrup=models.ManyToManyField(Syrup)
	roast=models.ForeignKey(Roast)
	beans=models.ForeignKey(Beans, null=True)
	milk=models.FloatField()
	water=models.FloatField()
	foam=models.BooleanField()
	shots=models.PositiveIntegerField(default=1)
	extra_instruction=models.TextField(null=True)
	price=models.DecimalField(max_digits=5, decimal_places=3, null=True)


	def __str__(self):
		return(self.name)

	def get_absolute_url(self):
		return reverse ("coffee:userCoffeeDetails", kwargs = {"details_id": self.id})


class City(models.Model):
	name=models.CharField(max_length=50)

	def __str__(self):
		return (self.name)

class Address(models.Model):
	user=models.ForeignKey(User)
	city=models.ForeignKey(City)
	block=models.CharField(max_length=50)
	street=models.CharField(max_length=50)
	building=models.CharField(max_length=50)
	floor=models.PositiveIntegerField(null=True, blank=True)
	apartment_Number=models.PositiveIntegerField(null=True, blank=True)
	extra_instruction=models.TextField(null=True, blank=True)

	def __str__(self):
		return str(self.city)





