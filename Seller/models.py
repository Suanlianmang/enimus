from django.db import models
from django.contrib.auth.models import User

class ProductImage(models.Model):
	file = models.ImageField(upload_to='product_image')

	
class Product(models.Model):
	description = models.TextField(max_length=500)
	discount = models.IntegerField(default=0)
	image = models.ManyToManyField(ProductImage)
	name = models.CharField(max_length=50)
	price = models.IntegerField(default=1)

class Rating(models.Model):
	by = models.ForeignKey(User, on_delete=models.CASCADE)
	like = models.BooleanField(default=False)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Comment(models.Model):
	by = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
