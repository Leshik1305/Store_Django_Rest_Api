from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    '''Пользовательская модель, расширяющая стандартную модель пользователя Django'''

    ROLE_CHOICES = [
        ("supplier", "Supplier"),
        ("consumer", "Consumer"),
    ]
    ''' выбор вида юзера (поставщик и потребитель) '''
    role = models.CharField(max_length=15,  choices=ROLE_CHOICES)



class Storehouse(models.Model):
    ''' Модель для представления склада'''
    name = models.CharField(max_length=128)


class Product(models.Model):
    ''' Модель для товара '''
    name = models.CharField(max_length=128)
    quantity = models.PositiveIntegerField()
    storehouse = models.ForeignKey(Storehouse, related_name="products", on_delete=models.CASCADE)

class Supply(models.Model):
    ''' Модель для представления поставок товара '''
    supplier = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'supplier')
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Consumption(models.Model):
    ''' Модель для представления потребления товара '''
    consumer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'consumer' )
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
