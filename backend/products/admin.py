from django.contrib import admin

from products.models import Product, Category, SubCategory


class ProductAdmin(admin.ModelAdmin):

    class Meta:
        model = Product


class SubCategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = SubCategory


class CategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = Category


admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
