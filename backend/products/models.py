from datetime import datetime

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateField(default=datetime.now)
    updated_at = models.DateField(default=datetime.now)


class SubCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateField(default=datetime.now)
    updated_at = models.DateField(default=datetime.now)


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    # images
    # # image = ImageField(upload_to=_get_image_directory_path) # TODO: m2m relationship
    brand = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    sale = models.FloatField()
    created_at = models.DateField(default=datetime.now)
    updated_at = models.DateField(default=datetime.now)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False, blank=False)
