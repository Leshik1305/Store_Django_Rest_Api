#Импорт моделей из Django
from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):  #Пользовательская модель, расширяющая стандартную модель пользователя Django

    ROLE_CHOICES = [
        ("supplier", "Supplier"), # Значение для поставщика
        ("consumer", "Consumer"), # Значение для потребителя
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)  # Поле для хранения типа пользователя



class Storehouse(models.Model): # Модель для представления склада
    name = models.CharField(max_length=128)  # Название склада


class Product(models.Model): # Модель для товара
    name = models.CharField(max_length=128) # Название товара
    quantity = models.PositiveIntegerField()  # Количесвто товара
    storehouse = models.ForeignKey(Storehouse, related_name="products", on_delete=models.CASCADE) # Внешний ключ на склад, связь многие к одному

class Supply(models.Model):  # Модель для представления поставок товара
    supplier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Внешний ключ на поставщика
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)   # Внешний ключ на товар
    quantity = models.PositiveIntegerField()  # Количесвто товара

class Consumption(models.Model):
    consumer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)   # Внешний ключ на потребителя
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)   # Внешний ключ на товар
    quantity = models.PositiveIntegerField()  # Количесвто товара
