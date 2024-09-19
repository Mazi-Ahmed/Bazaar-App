from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from product.models import Product


@login_required
def index(request):
    products = Product.objects.filter(created_by=request.user)
    return render(request, 'userprofile/index.html', {
        'products': products
    })



