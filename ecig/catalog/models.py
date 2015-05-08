from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    price = models.FloatField()
    quantity_on_hand = models.IntegerField(default=0)
    available_when_out = models.BooleanField(default=True)

class ProductImage(models.Model):
    product_id = models.ForeignKey(Product)
    image = models.ImageField()

class Category(models.Model):
    label = CharField(max_length=255)
    parent_id = IntegerField(null=True)

class ProductCategory(models.Model):
    product_id = models.ForeignKey(Product)
    category_id = models.ForeignKey(Category)
