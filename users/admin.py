from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

# Register your models here.


# @admin.register(User, UserAdmin)
# class UserAdmin(admin.ModelAdmin):
#     fields = (
#         "firts_name",
#         # "description",
#         # "products",
#     )
#     list_display = (
#         "firts_name",
#         # "slug",
#         # "description",
#         # "created_at",
#     )

admin.site.register(User, UserAdmin)
