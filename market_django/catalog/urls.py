from django.urls import path

from . import views
from .views import CategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('<category>/', ProductListView.as_view(), name='products'),
    path('product/<pk>', ProductDetailView.as_view(), name='product')
]