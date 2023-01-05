from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Product, Category, Customer
from django.views import View

# Create your views here.


class Index(View):
    # when user clicks on "add to cart"
    def post(self, request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        # if user clicked on the button "add to card" we will get a dictionary with the values of products id
        if cart:
            # if cart exists
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity - 1
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            # if cart does not exists then create a card dictionary and add the item
            cart = {}
            cart[product_id] = 1

        print(request.session.get('cart'))
        request.session['cart'] = cart
        return redirect('index')

    # when user wants to visit homepage
    def get(self, request):
        # creating cart for the user who logged in
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

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


class Signup(View):
    # validation of users inputs
    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required."
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 char long or more."
        elif not customer.last_name:
            error_message = "Last Name Required."
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 char long or more."
        elif not customer.phone:
            error_message = "Phone number required."
        elif len(customer.phone) < 11:
            error_message = "Phone number must be 11 char long."
        elif not customer.password:
            error_message = "Password required."
        elif len(customer.password) < 5:
            error_message = "Password must be 6 char long."
        elif not customer.email:
            error_message = "Email required."
        elif customer.isExists():
            error_message = "This email is already registered. Use another email to signup."

        return error_message

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        # fetching data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password
        )

        error_message = self.validateCustomer(customer)

        # saving data into the database
        if not error_message:
            # hashing the user entered password
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', context=data)


class Login(View):
    # django will decide witch method to call as the users request
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user_email = request.POST.get('email')
        password = request.POST.get('password')

        # getting the data of the customer if he/she has already registered
        customer = Customer.get_customer_by_email(user_email)

        # checking if the customer exists and its password matches or not with the hashed password
        if customer and check_password(password, customer.password):
            # saving the information of user in session for further use
            request.session['customer'] = customer.id
            # now we can access these data from index page or index function
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': "Incorrect Email or Password."})


def logout(request):
    # clearing the session. All the values will be removed including cart.
    request.session.clear()
    return redirect('login')
