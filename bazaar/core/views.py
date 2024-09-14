from django.shortcuts import render
from product.models import Category, Product


def index(request):
    products = Product.objects.filter(item_sold=False)[0:5]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'products': products,
    })

def contact(request):
    return render(request, 'core/contact.html')
