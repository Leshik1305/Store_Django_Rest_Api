
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError

from api.models import CustomUser, Storehouse, Product, Supply, Consumption
from api.serializers import CustomUserSerializer, StorehouseSerializer, ProductSerializer, SupplySerializer, \
    ConsumptionSerializer




class CustomerUserModelViewSet(viewsets.ModelViewSet):
    ''' Представление для модели CustomUser '''
    queryset = CustomUser.objects.all()
    ''' Запрос для получения всех пользователей '''
    serializer_class = CustomUserSerializer
    ''' Используемый сериализатор '''
    permission_classes = [permissions.AllowAny]


class StorehouseModelViewSet(viewsets.ModelViewSet):
    ''' Представление для модели Storehouse '''
    queryset = Storehouse.objects.all()
    serializer_class =StorehouseSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]

class ProductModelViewSet(viewsets.ModelViewSet):
    ''' Представление для модели Product '''
    queryset = Product.objects.all()
    serializer_class =ProductSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]

class SupplyModelViewSet(viewsets.ModelViewSet):
    '''  Представление для модели Supply '''
    serializer_class = SupplySerializer
    queryset = Supply.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        ''' Функция создания поставки '''
        user = self.request.user
        if user.role != "supplier":
            raise ValidationError (
                "Only suppliers can supply products."
            )

        product = serializer.validated_data["product"]
        quantity = serializer.validated_data["quantity"]

        product.quantity += quantity
        product.save()
        serializer.save(supplier = user)


class ConsumptionModelViewSet(viewsets.ModelViewSet):
    ''' Представление для модели Consumption '''

    serializer_class = ConsumptionSerializer
    queryset = Consumption.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        ''' Функция создания потребления товара '''
        user = self.request.user
        if user.role != "consumer":
            raise ValidationError (
                "Only consumers can consume products."
            )
        product = serializer.validated_data["product"]
        quantity = serializer.validated_data["quantity"]

        if product.quantity < quantity:
            raise ValidationError ("Not enough product in stock.")
        product.quantity -= quantity
        product.save()
        serializer.save(consumer=user)
