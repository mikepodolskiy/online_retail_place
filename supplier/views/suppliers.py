from django.db.models import QuerySet
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from supplier.models import Supplier
from supplier.serializers.suppliers_serializers import SupplierSerializer, SupplierDetailSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()  # add filter

    # @action(detail=False, methods=['get'])
    # def city(self, request, *args, **kwargs) -> QuerySet:
    #     return super().list(self, request, *args, **kwargs)
    #
    # def get_queryset(self):
    #     if self.action == 'city':
    #         return Supplier.objects.filter(contacts__city=self.request.city).all()
    #     return Supplier.objects.all()

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
