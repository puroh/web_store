from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate

from django.contrib.auth import login, logout
from django.contrib import messages

from facilito_store.forms import RegisterForm

# from django.contrib.auth.models import User
from users.models import User
from products.models import Product


def index(request):

    products = Product.objects.all().order_by("-created_at")
    return render(
        request,
        "index.html",
        {
            "message": "este es mi mensaje desde el view",
            "title": "productos",
            "products": products,
        },
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "welcome {}".format(user.username))
            return redirect("index")

        else:
            messages.error(request, "not valid user")
    return render(
        request,
        "users/login.html",
        {},
    )


def logout_view(request):
    logout(request)
    messages.success(request, "Seccion close")
    return redirect("login")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = form.save()
        if user:
            messages.success(
                request,
                "User created",
            )
            return redirect("index")

    return render(
        request,
        "users/register.html",
        {
            "form": form,
        },
    )
