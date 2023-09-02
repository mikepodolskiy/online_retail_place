from rest_framework.viewsets import ModelViewSet

from supplier.models import Supplier
from supplier.permissions import IsActivePermission
from supplier.serializers.suppliers_serializers import SupplierSerializer, SupplierDetailSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()  # ??? do not launch without queryset
    permission_classes = (IsActivePermission,)

    def get_queryset(self):
        queryset = Supplier.objects.all()
        city = self.request.query_params.get('city')
        if city is not None:
            queryset = queryset.filter(contacts__city=city)
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return SupplierDetailSerializer
        return SupplierSerializer
