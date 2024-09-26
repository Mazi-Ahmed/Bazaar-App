from django.shortcuts import render, redirect
from product.models import Category, Product
from .forms import Signup

def index(request):
    products = Product.objects.filter(item_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'products': products,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = Signup()
    return render(request, 'core/signup.html', {
        'form':form
    })

def home_view(request):
    return render(request, 'core/base.html', {
        'active_page': 'home'  
    })

def products_view(request):
    return render(request, 'core/base.html', {
        'active_page': 'products'  
    })

def new_product_view(request):
    return render(request, 'core/base.html', {
        'active_page': 'new' 
    })