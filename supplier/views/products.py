from rest_framework.viewsets import ModelViewSet

from supplier.models import Product
from supplier.serializers.product_serializers import ProductSerializer


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
