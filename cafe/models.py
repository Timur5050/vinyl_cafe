import os
import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def movie_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/movies/", filename)


class Product(models.Model):
    class ProductType(models.TextChoices):
        HOT_COFFEE = "HOT_COFFEE", _("Hot Coffee")
        COLD_COFFEE = "COLD_COFFEE", _("Cold Coffee")
        TEA = "TEA", _("Tea")
        SHAWARMA = "SHAWARMA", _("Shawarma")
        SANDWICH = "SANDWICH", _("Sandwich")
        HOT_DOG = "HOT_DOG", _("Hot Dog")
        ANOTHER_FAST_FOOD = "ANOTHER_FAST_FOOD", _("Another Fast Food")
        BAKERY = "BAKERY", _("Bakery")
        ICE_CREAM = "ICE_CREAM", _("Ice Cream")

    title = models.CharField(max_length=100)
    description = models.TextField()
    product_type = models.CharField(max_length=20, choices=ProductType.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(null=True, upload_to=movie_image_file_path)
    season_product = models.BooleanField(default=False)


class Order(models.Model):
    products = models.ManyToManyField(Product, related_name="orders")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class FeedBack(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    time = models.DateTimeField(auto_now_add=True)

