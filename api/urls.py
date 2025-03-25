from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.views import CustomerUserModelViewSet, StorehouseModelViewSet, ProductModelViewSet, SupplyModelViewSet, ConsumptionModelViewSet

router = DefaultRouter()
''' Создание маршрутизатора '''

router.register('users', CustomerUserModelViewSet)
''' Регистрация представления для пользователей '''
router.register('storehouses', StorehouseModelViewSet)
''' Регистрация представления для товаров '''
router.register('products', ProductModelViewSet)
''' Регистрация представления для складов '''
router.register('supplies', SupplyModelViewSet)
''' Регистрация представления для поставок '''
router.register('consumptions', ConsumptionModelViewSet)
''' Регистрация представления для потреблений '''


urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns.extend(router.urls)
