from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from .forms import NewProduct, EditProduct

def products(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    products = Product.objects.filter(item_sold=False)

    if category_id:
        products = products.filter(category_id=category_id)
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query)) 
    return render(request, 'product/products.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    similar_products = Product.objects.filter(category=product.category, item_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'product/detail.html', {
        'product': product,
        'similar_products': similar_products
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewProduct(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect('product:detail', pk=product.id)
    else:
        form = NewProduct()
    return render(request, 'product/form.html', {
        'form': form,
        'title': 'New Product'
    })

@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    product.delete()
    return redirect('userprofile:index')

@login_required
def edit(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product:detail', pk=product.id)
    else:
        form = EditProduct(instance=product)
    return render(request, 'product/form.html', {
        'form': form,
        'title': 'Edit Listing'
    })