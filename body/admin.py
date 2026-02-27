from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Category,
    PickupPoint,
    Manufacturer,
    Order,
    OrderItem,
    Product,
    Role,
    Supplier,
    Unit,
    User,
)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "full_name", "role", "email", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        ("Доп. данные", {"fields": ("full_name", "role")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Доп. данные", {"fields": ("full_name", "role")}),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "article",
        "name",
        "price",
        "discount_percent",
        "stock_quantity",
        "category",
        "supplier",
    ]
    list_filter = ["category", "supplier", "manufacturer"]
    search_fields = ["article", "name"]


@admin.register(PickupPoint)
class PickupPointAdmin(admin.ModelAdmin):
    list_display = ["address"]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ["name"]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    autocomplete_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "order_number",
        "client_full_name",
        "order_date",
        "status",
        "pickup_point",
    ]
    list_filter = ["status"]
    search_fields = ["order_number", "client_full_name", "items__product__article"]
    inlines = [OrderItemInline]
