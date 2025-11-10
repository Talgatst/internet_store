from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, Category
from webapp.forms import ProductForm


def products_view(request):
    products = Product.objects.filter(stock__gte=1).order_by('category__name', 'title')
    return render(request, 'product_list.html', {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()

    context = {
        'form': form,
        'title': 'Add product',
        'button_text': 'Add'
    }
    return render(request, 'product_form.html', context)


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


def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'title': 'Edit product',
        'button_text': 'Edit'
    }
    return render(request, 'product_form.html', context)


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})


