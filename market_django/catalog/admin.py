from django.contrib import admin
from .models import Image, Brand, Category, Product, Attribute, Feature, ProductData


admin.site.register(Image)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(Feature)
admin.site.register(ProductData)