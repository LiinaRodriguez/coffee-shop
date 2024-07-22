from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product
from django.views.generic.base import  TemplateView
from django.views import generic
from django.shortcuts import render
# Create your views here.

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Product.CATEGORY_CHOICES
        categorized_products = {category[1]: Product.objects.filter(category=category[0]) for category in categories}
        context['categorized_products'] = categorized_products
        return context

class ProductFormView(generic.FormView):
    template_name = 'products/add_products.html'
    form_class = ProductForm
    success_url= reverse_lazy('products')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
