from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    # images
    brand = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    sale = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # category = models.ForeignKey(default='')


class Categories(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    subcategory = models.CharField(max_length=150)


class SubCategory(models.CharField):
    category = models.CharField(max_length=150)
