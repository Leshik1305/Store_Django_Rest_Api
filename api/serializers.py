from rest_framework import serializers
from rest_framework import validators

from api.models import CustomUser, Storehouse, Product, Supply, Consumption


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','role', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        email = validated_data.get("email")
        if email:
            instance.email = email
        password = validated_data.get("password")
        if password:
            instance.set_password = password

        instance.save()
        return instance


class StorehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storehouse
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ("id", "product", "quantity")
        extra_kwargs = {"id": {"read_only": True}}


class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = ("id", "product", "quantity")
        extra_kwargs = {"id": {"read_only": True}}
