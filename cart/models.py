from django.db import models
from coffee.models import Coffee
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, post_delete
from decimal import Decimal

class CartItem(models.Model):
	cart = models.ForeignKey('Cart')
	item = models.ForeignKey(Coffee)
	quantity = models.PositiveIntegerField(default=1)
	line_item_total = models.DecimalField(max_digits=5, decimal_places=3)

	def __str__(self):
		return self.item.name

def cart_item_pre_save(sender, instance, *args, **kargs):
	qty = instance.quantity
	if qty >= 1:
		price = instance.item.price
		total = Decimal(price) * Decimal(qty)
		instance.line_item_total = total

pre_save.connect(cart_item_pre_save, sender=CartItem)

def cart_item_post_save(sender, instance, *args, **kargs):
	instance.cart.update_subtotal()

post_save.connect(cart_item_post_save, sender=CartItem)
post_delete.connect(cart_item_post_save, sender=CartItem)

class Cart(models.Model):
	user = models.ForeignKey(User)
	items = models.ManyToManyField(Coffee, through=CartItem)
	subtotal = models.DecimalField(max_digits=6, decimal_places=3, default=1)
	delivery_total = models.DecimalField(max_digits=5, decimal_places=3)
	total = models.DecimalField(max_digits=5, decimal_places=3, default=1)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.user.username



	def update_subtotal(self):
		subtotal = 0
		items = self.cartitem_set.all()
		for item in items:
			subtotal += item.line_item_total
		self.subtotal = "%.3f"%subtotal
		self.save()


def delivery_and_total(sender, instance, *args, **kargs):

	subtotal = Decimal(instance.subtotal)
	delivery_total = Decimal(2.000)
	total = subtotal + delivery_total
	instance.delivery_total = Decimal(delivery_total)
	instance.total = Decimal(total)


pre_save.connect(delivery_and_total, sender=Cart)