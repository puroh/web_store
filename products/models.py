import black
from django.utils.text import slugify
from django.db import models
from uuid import uuid4


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)  # 1232142342.34
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="products/", null=False, blank=False)

    def __str__(self):
        return f"{self.title}"

    # def save(self, *args, **kwargs) -> None:  # esto se comenta cuando funcione el signal
    #     self.slug = slugify(self.title)
    #     return super(Product, self).save(*args, **kwargs)
