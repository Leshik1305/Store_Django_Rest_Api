from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ("supplier", "Supplier"),
        ("consumer", "Consumer"),
    ]



class Storehouse(models.Model):
    name = models.CharField(max_length=128)


class Product(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.PositiveIntegerField()
    storehouse = models.ForeignKey(Storehouse, related_name="products", on_delete=models.CASCADE)

class Supply(models.Model):
    supplier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Consumption(models.Model):
    consumer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()