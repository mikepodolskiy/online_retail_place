from rest_framework import serializers

from supplier.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ("debt",)


class SupplierDetailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="contacts.email")
    country = serializers.CharField(source="contacts.country")
    city = serializers.CharField(source="contacts.city")
    street = serializers.CharField(source="contacts.street")
    building_number = serializers.IntegerField(source="contacts.building_number")
    product_title = serializers.CharField(source="product.title")
    product_model = serializers.CharField(source="product.model")
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    created_at = serializers.DateField(required=False)

    class Meta:
        model = Supplier
        fields = ("title", "email", "country", "city", "street", "building_number", "product_title","product_model","debt","created_at",)
