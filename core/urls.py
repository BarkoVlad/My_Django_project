from rest_framework.routers import DefaultRouter

from client.api.v1.views.purchaser_views import PurchaserViewSet
from client.api.v1.views.purchaserdata_views import PurchaserDataViewSet
from equipment.api.v1.views.category_views import CategoryViewSet
from equipment.api.v1.views.equipment_views import EquipmentViewSet
from equipment.api.v1.views.shops_views import ShopsViewSet
from suppliers.api.v1.views.brandpartners_views import BrandPartnersViewSet
from suppliers.api.v1.views.storespartners_views import StoresPartnersViewSet
from suppliers.api.v1.views.suppliers_views import SuppliersViewSet

router = DefaultRouter()
router.register(r'purchaser', PurchaserViewSet)
router.register(r'purchaserdata', PurchaserDataViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'shops', ShopsViewSet)
router.register(r'brandpartners', BrandPartnersViewSet)
router.register(r'storespartners', StoresPartnersViewSet)
router.register(r'suppliers', SuppliersViewSet)

urlpatterns = router.urls