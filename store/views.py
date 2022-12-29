from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryId = request.GET.get('category')

    if categoryId:
        products = Product.get_all_products_by_categoryId(
            category_id=categoryId)
    else:
        products = Product.get_all_products()
    data = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context=data)
