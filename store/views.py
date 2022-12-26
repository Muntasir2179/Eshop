from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def index(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    data = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context=data)
