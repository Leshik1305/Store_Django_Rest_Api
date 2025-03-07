from rest_framework.routers import DefaultRouter

from api.views import CustomerUserModelViewSet, StorehouseModelViewSet, ProductModelViewSet, SupplyModelViewSet, ConsumptionModelViewSet

router = DefaultRouter()  # Создание маршрутизатора

router.register('users', CustomerUserModelViewSet)  # Регистрация представления для пользователей
router.register('storehouses', StorehouseModelViewSet)   # Регистрация представления для товаров
router.register('products', ProductModelViewSet)  # Регистрация представления для складов
router.register('supplies', SupplyModelViewSet)  # Регистрация представления для поставок
router.register('consumptions', ConsumptionModelViewSet)   # Регистрация представления для потреблений

urlpatterns = [

]

urlpatterns.extend(router.urls)
