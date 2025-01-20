from rest_framework.routers import DefaultRouter

from api.views import CustomerUserModelViewSet, StorehouseModelViewSet, ProductModelViewSet, SupplyModelViewSet, ConsumptionModelViewSet

router = DefaultRouter()
router.register('users', CustomerUserModelViewSet)
router.register('storehouses', StorehouseModelViewSet)
router.register('products', ProductModelViewSet)
router.register('supplies', SupplyModelViewSet)
router.register('consumptions', ConsumptionModelViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)