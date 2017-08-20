from django.db import models
from django.contrib.auth.models import User


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
	shots=models.PositiveIntegerField()
	extra_instruction=models.TextField(null=True)
	price=models.DecimalField(max_digits=5, decimal_places=3, null=True)


	def __str__(self):
		return(self.name)








