from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product
from django.views.generic.base import  TemplateView
from django.views import generic
from django.shortcuts import render
# Create your views here.

class ProductListView(TemplateView):
    template_name = 'products/products_list.html'

    def get_context_data(self):
        product_list = Product.objects.all()
        return {'products_list': product_list}

class ProductFormView(generic.FormView):
    template_name = 'products/add_products.html'
    form_class = ProductForm
    success_url= reverse_lazy('products')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)