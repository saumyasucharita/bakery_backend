from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_description = models.CharField(max_length=200)
    price = models.DecimalField(default = 1.0, max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default = 0)
    image_url = models.URLField(null=True, max_length=200)
