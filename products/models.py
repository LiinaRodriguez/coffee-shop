from django.db import models

# Create your models here.
class Product(models.Model):
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

    name = models.TextField(max_length=100, verbose_name='Name')
    description = models.TextField(max_length=350, verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='available')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=APPETIZER)
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name='Photo')

    def __str__(self):
        return self.name