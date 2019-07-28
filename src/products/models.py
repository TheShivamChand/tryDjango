from django.db import models

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(max_length=100)
	description = models.TextField(null=False,blank=False)
	price 		= models.DecimalField(decimal_places=2,max_digits=10)
	summary		= models.TextField(default="Nice")
	featured	= models.BooleanField(default=False)