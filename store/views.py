from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    products = Product.get_all_products()
    return render(request, 'index.html', {'products': products})
