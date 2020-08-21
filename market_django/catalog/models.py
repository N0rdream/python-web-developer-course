from django.db import models


class Image(models.Model):
    file = models.ImageField()

    def __str__(self):
        return f'{self.file}'


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    price = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} {self.brand} {self.name}'


class Attribute(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Feature(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.attribute}: {self.value}'


class ProductData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}: {self.feature}'