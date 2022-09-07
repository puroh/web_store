from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product

from carts.utils import get_or_create_cart
from carts.models import CartProducts


def cart_view(request):
    cart = get_or_create_cart(request)
    return render(request, "carts/cart.html", {"cart": cart})


def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get("product_id"))

    quantity = int(request.POST.get("quantity", 1))

    # cart.products.add(product, through_defaults={"quantity": quantity})

    cart_product = CartProducts.objects.create_or_update_quantity(
        cart=cart,
        product=product,
        quantity=quantity,
    )

    return render(
        request,
        "carts/add.html",
        {
            "quantity": quantity,
            "cart_product": cart_product,
            "product": product,
        },
    )


def remove(request):

    product = get_object_or_404(Product, pk=request.POST.get("product_id"))
    cart = get_or_create_cart(request)

    cart.products.remove(product)
    return redirect("carts:cart")
