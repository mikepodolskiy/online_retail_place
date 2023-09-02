from rest_framework import routers

from supplier.views.contacts import ContactsViewSet
from supplier.views.products import ProductsViewSet
from supplier.views.suppliers import SupplierViewSet

supplier_router = routers.SimpleRouter()
supplier_router.register("supplier", SupplierViewSet)
contacts_router = routers.SimpleRouter()
supplier_router.register("contacts", ContactsViewSet)
products_router = routers.SimpleRouter()
supplier_router.register("product", ProductsViewSet)

