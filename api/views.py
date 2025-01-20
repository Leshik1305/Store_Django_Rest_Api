
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError

from api.models import CustomUser, Storehouse, Product, Supply, Consumption
from api.serializers import CustomUserSerializer, StorehouseSerializer, ProductSerializer, SupplySerializer, \
    ConsumptionSerializer


# Create your views here.


class CustomerUserModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['post', 'get']
    authentication_classes = []
    permission_classes = []


class StorehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Storehouse.objects.all()
    serializer_class =StorehouseSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]

class SupplyModelViewSet(viewsets.ModelViewSet):

    serializer_class = SupplySerializer
    queryset = Supply.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
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

    serializer_class = ConsumptionSerializer
    queryset = Consumption.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
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
