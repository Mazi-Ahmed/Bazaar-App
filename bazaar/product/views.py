from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, ProductImage
from .forms import NewProduct, EditProduct, ProductImageForm
from django.forms import modelformset_factory

def products(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    products = Product.objects.filter(item_sold=False)
    free_products = Product.objects.filter(price=0, item_sold=False)

    if category_id:
        products = products.filter(category_id=category_id)
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query)) 
    return render(request, 'product/products.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'free_products': free_products
    })


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    images = ProductImage.objects.filter(product=product)
    similar_products = Product.objects.filter(category=product.category, item_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'product/detail.html', {
        'product': product,
        'images': images,
        'similar_products': similar_products,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    })
@login_required
def new(request):
    ProductImageFormSet = modelformset_factory(ProductImage, form=ProductImageForm, extra=4)

    if request.method == 'POST':
        product_form = NewProduct(request.POST, request.FILES)
        image_formset = ProductImageFormSet(request.POST, request.FILES)

        print("POST data:", request.POST)
        print("FILES data:", request.FILES)

        if product_form.is_valid():
            print("Product form is valid")
            if image_formset.is_valid():
                print("Image formset is valid")
                product = product_form.save(commit=False)
                product.created_by = request.user
                product.save()

                for form in image_formset:
                    if form.cleaned_data:  
                        image = form.save(commit=False)
                        image.product = product
                        image.save()

                return redirect('product:detail', pk=product.id)
            else:
                print("Image formset errors:", image_formset.errors)
        else:
            print("Product form errors:", product_form.errors)

    else:
        product_form = NewProduct()
        image_formset = ProductImageFormSet(queryset=ProductImage.objects.none())

    return render(request, 'product/form.html', {
        'form': product_form,
        'image_formset': image_formset,
        'title': 'Create new listing'
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
        product_form = EditProduct(request.POST, request.FILES, instance=product)

        if product_form.is_valid():
            product_form.save()
            return redirect('product:detail', pk=product.id)
        else:
            print("Product form errors:", product_form.errors)

    else:
        product_form = EditProduct(instance=product)

    return render(request, 'product/form.html', {
        'form': product_form,
        'title': 'Edit Listing'
    })

@login_required
def delivery(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/delivery.html', {
        'product':product,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
        })





