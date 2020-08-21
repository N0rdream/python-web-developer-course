from django.shortcuts import render, redirect
from .models import Category, Product, ProductData
from django.conf import settings
from django.views.generic import ListView, DetailView


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'


class ProductListView(ListView):
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(
            category__name=self.kwargs['category']
        ).values('brand__name', 'name', 'price', 'id', 'image__file')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        for qs in context['products']:
            qs['image__file'] = settings.MEDIA_URL + qs['image__file']
        return context


class ProductDetailView(DetailView):
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.values('price', 'name', 'brand__name', 'image__file')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_url = settings.MEDIA_URL + context['product']['image__file']
        context['product']['image__file'] = image_url
        product_data = ProductData.objects.filter(
            product_id=self.kwargs['pk']
        ).values('feature__value', 'feature__attribute__name')
        context['product_data'] = product_data
        return context