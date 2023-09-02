from django.contrib import admin

from supplier.models import Supplier, Contacts, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ContactsAdmin(admin.ModelAdmin):
    pass
