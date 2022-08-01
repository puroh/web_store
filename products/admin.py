from django.contrib import admin

from products.models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "price",
        "description",
        "image",
    )
    list_display = (
        "title",
        "price",
        "slug",
        "description",
        "created_at",
    )
