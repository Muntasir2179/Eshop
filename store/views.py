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
        # fetching data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }

        error_message = None

        if not first_name:
            error_message = "First Name Required."
        elif len(first_name) < 4:
            error_message = "First Name must be 4 char long or more."
        elif not last_name:
            error_message = "Last Name Required."
        elif len(last_name) < 4:
            error_message = "Last Name must be 4 char long or more."
        elif not phone:
            error_message = "Phone number required."
        elif len(phone) < 11:
            error_message = "Phone number must be 11 char long."
        elif not password:
            error_message = "Password required."
        elif len(password) < 5:
            error_message = "Password must be 6 char long."
        elif not email:
            error_message = "Email required."

        # saving data into the database
        if not error_message:
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                password=password
            )
            customer.register()
            return HttpResponse("<h1>Signup successful.</h1>")
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', context=data)
