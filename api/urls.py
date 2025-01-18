from rest_framework.routers import DefaultRouter

from api.views import CustomerUserModelViewSet, StorehouseModelViewSet, ProductModelViewSet, SupplyModelViewSet, ConsumptionModelViewSet

router = DefaultRouter()
router.register('users', CustomerUserModelViewSet)
router.register('storehouse', StorehouseModelViewSet)
router.register('product', ProductModelViewSet)
router.register('supply', SupplyModelViewSet)
router.register('consumption', ConsumptionModelViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)