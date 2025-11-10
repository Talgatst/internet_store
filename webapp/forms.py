# forms.py
from django import forms
from django.core.validators import MinValueValidator
from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'image_url', 'category', 'description', 'stock',]

    price = forms.DecimalField(
        max_digits=7,
        decimal_places=2,
        min_value=0,
        label='Price'
    )
    stock = forms.IntegerField(
        min_value=0,
        label='Stock'
    )
