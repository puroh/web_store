from enum import Enum

from django.db import models

from carts.models import Cart
from users.models import User


class OrderStatus(Enum):
    CREATED = "CREATED"
    PAYED = "PAYED"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"


choices = [(tag, tag.value) for tag in OrderStatus]


class Order(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=choices, default=OrderStatus.CREATED)
    shipping_total = models.DecimalField(default=5, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.order_id}"
