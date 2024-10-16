from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Product(TimeStampedModel):
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Material(TimeStampedModel):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class ProductMaterial(TimeStampedModel):
    product = models.ForeignKey(Product, related_name='pm', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, related_name='pm', on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return self.product.name

class Warehouse(TimeStampedModel):
    material = models.ForeignKey(Material, related_name='w', on_delete=models.CASCADE)
    remainder = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.material.name

    class Meta:
        ordering = ['created']