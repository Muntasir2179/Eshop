from django.contrib import admin
from .models import Product, Category, Customer, Order


class AdminProduct(admin.ModelAdmin):
    # setting the table columns name to show in the admin site
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    # setting the table columns name to show in the admin site
    list_display = ['name']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
