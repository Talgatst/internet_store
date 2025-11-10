from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, Category


def products_view(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def product_add_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        image_url = request.POST.get('image_url')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        category = Category.objects.get(id=category_id)
        product = Product.objects.create(
            title=title,
            price=price,
            image_url=image_url,
            category=category,
            description=description
        )
        return redirect(f'/products/{product.id}/')

    categories = Category.objects.all()
    return render(request, 'product_add.html', {'categories': categories})


def category_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = Category.objects.create(
            name=name,
            description=description
        )
        return redirect('/')

    return render(request, 'category_add.html')
