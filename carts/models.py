from django.db import models
from users.models import User
from products.models import Product
from uuid import uuid4

from django.db.models.signals import pre_save


class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        blank=True,
    )
    products = models.ManyToManyField(Product)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.cart_id}"


def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid4())


pre_save.connect(set_cart_id, sender=Cart)
