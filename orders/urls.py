from django.urls import path
from .views import MyOrderView, CreateOrderProductView

urlpatterns = [
    path('my-order',MyOrderView.as_view(), name='myorder'),
    path('add-product', CreateOrderProductView.as_view(), name='add_order_product')
]
