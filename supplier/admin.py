from django.contrib import admin

from supplier.models import Supplier, Contacts, Product


@admin.action(description="Delete debt for selected")
def delete_debt(modeladmin, request, queryset) -> None:
    """
    sets method for admin panel to make debt equal to 0
    """
    queryset.update(debt=0)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    # list of fields to show in admin panel for supplier
    list_display = ("title", "contacts", "product", "supplier", "debt")
    # list of fields to show to be hyperlinks to object
    list_display_links = ("supplier", )
    # filter for admin panel (using lookups to get object's field (city))
    list_filter = ("contacts__city", )




@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ContactsAdmin(admin.ModelAdmin):
    pass
