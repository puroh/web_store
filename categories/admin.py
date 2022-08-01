from django.contrib import admin

from categories.models import Category

# Register your models here.


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "description",
        "products",
    )
    list_display = (
        "title",
        # "slug",
        "description",
        "created_at",
    )
