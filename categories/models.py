import imp
from django.db import models
from uuid import uuid4
from products.models import Product

# Create your models here.


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(null=False, blank=False, unique=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Categories"
