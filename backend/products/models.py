from django.db import models


class Products(models.Model):
    title = models.CharField()
    slug = models.SlugField()
    # images
    brand = models.CharField()
    description = models.TextField()
    price = models.FloatField()
    sale = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    category = models.ForeignKey(default='')


class Categories(models.Model):
    title = models.CharField()
    description = models.TextField()
    subcategory = models.CharField()


class SubCategory(models.CharField):
    pass
