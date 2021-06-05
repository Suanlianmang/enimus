from django.db import models
from django.contrib.auth.models import User
from Seller.models import Product

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

