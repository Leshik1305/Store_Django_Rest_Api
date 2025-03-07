from rest_framework import serializers
from rest_framework import validators

from api.models import CustomUser, Storehouse, Product, Supply, Consumption


class CustomUserSerializer(serializers.ModelSerializer):  # Определяем класс сериализатора для модели CustomUser
    class Meta:  # Внутренний класс Meta используется для указания метаинформации
        model = CustomUser  # Указываем модель, для которой создаем сериализатор 
        fields = ['username','role', 'email', 'password']  # Перечисляем поля, которые будут сериализоваться
        extra_kwargs = {'password': {'write_only': True}}  # Чтобы пароль не возвращался в ответе

    def create(self, validated_data):  # Функция создания нового пользователя
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):  # Функция обновления e-mail 
        email = validated_data.get("email")
        if email:
            instance.email = email
        password = validated_data.get("password")
        if password:
            instance.set_password = password

        instance.save()
        return instance


class StorehouseSerializer(serializers.ModelSerializer):  # Определяем класс сериализатора для модели Storehouse
    class Meta: # Внутренний класс Meta используется для указания метаинформации
        model = Storehouse  # Указываем модель, для которой создаем сериализатор 
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):  # Определяем класс сериализатора для модели  Product
    class Meta:   # Внутренний класс Meta используется для указания метаинформации
        model = Product   # Указываем модель, для которой создаем сериализатор 
        fields = "__all__"  # Перечисляем поля, которые будут сериализоваться
        extra_kwargs = {"id": {"read_only": True}}


class SupplySerializer(serializers.ModelSerializer):   # Определяем класс сериализатора для модели  Supply
    class Meta:  # Внутренний класс Meta используется для указания метаинформации
        model = Supply  # Указываем модель, для которой создаем сериализатор 
        fields = ("id", "product", "quantity")  # Перечисляем поля, которые будут сериализоваться
        extra_kwargs = {"id": {"read_only": True}}


class ConsumptionSerializer(serializers.ModelSerializer):   # Определяем класс сериализатора для модели  Consumption
    class Meta:   # Внутренний класс Meta используется для указания метаинформации
        model = Consumption   # Указываем модель, для которой создаем сериализатор 
        fields = ("id", "product", "quantity")  # Перечисляем поля, которые будут сериализоваться
        extra_kwargs = {"id": {"read_only": True}}
