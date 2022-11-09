from uuid import uuid4
from django.db.models.signals import pre_save
from django.dispatch import receiver
from orders.models import Order


@receiver(pre_save, sender=Order)
def set_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid4())
