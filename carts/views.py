from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product

from carts.utils import get_or_create


def cart_view(request):
    cart = get_or_create(request)
    return render(request, "carts/cart.html", {"cart": cart})


def add(request):
    cart = get_or_create(request)
    product = get_object_or_404(Product, pk=request.POST.get("product_id"))

    cart.products.add(product)

    return render(request, "carts/add.html", {"product": product})


def remove(request):

    product = get_object_or_404(Product, pk=request.POST.get("product_id"))
    cart = get_or_create(request)

    cart.products.remove(product)
    return redirect("carts:cart")
