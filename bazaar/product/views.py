from django.shortcuts import render, get_object_or_404
from .models import Product


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    similar_products = Product.objects.filter(category=product.category, item_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'product/detail.html', {
        'product': product,
        'similar_products': similar_products
    })