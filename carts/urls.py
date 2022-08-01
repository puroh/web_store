from django.urls import path
from carts.views import cart_view, add, remove

app_name = "carts"

urlpatterns = [
    path("", cart_view, name="cart"),
    path("add", add, name="add"),
    path("remove", remove, name="remove"),
]
