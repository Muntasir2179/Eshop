from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Customer

# Create your views here.


def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryId = request.GET.get('category')
    if categoryId:
        if categoryId == "-1":
            products = Product.get_all_products()
        else:
            products = Product.get_all_products_by_categoryId(
                category_id=categoryId)
    else:
        products = Product.get_all_products()
    data = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context=data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password
        )

        customer.register()

        return HttpResponse("<h1>Signup successful.</h1>")
