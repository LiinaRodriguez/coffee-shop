from .models import Product
from django import forms
class ProductForm(forms.Form):

    APPETIZER = 'AP'
    MAIN_COURSE = 'MC'
    DESSERT = 'DS'
    BEVERAGE = 'BV'

    CATEGORY_CHOICES = [
        (APPETIZER, 'Appetizer'),
        (MAIN_COURSE, 'Main Course'),
        (DESSERT, 'Dessert'),
        (BEVERAGE, 'Beverage'),
    ]

    name = forms.CharField(max_length=100, label='Name')
    description = forms.CharField(max_length=350, label='Description')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Price')
    available = forms.BooleanField(initial=True, label='Available', required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category')
    photo = forms.ImageField(label='Photo', required=False)
    
    def save(self):
        Product.objects.create(
            name =self.cleaned_data['name'],
            description =self.cleaned_data['description'],
            price = self.cleaned_data['price'],
            available = self.cleaned_data['available'],
            category = self.cleaned_data['category'],
            photo = self.cleaned_data['photo'],
        )
    