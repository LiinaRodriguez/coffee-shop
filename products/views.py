from .models import Product
from django.views.generic.base import  TemplateView
from django.shortcuts import render
# Create your views here.

class ProductListView(TemplateView):
    template_name = 'products/products_list.html'

    def get_context_data(self):
        product_list = Product.objects.all()
        return {'products_list': product_list}