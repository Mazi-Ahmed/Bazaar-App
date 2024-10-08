from django import forms
from .models import Product, ProductImage

class NewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price','condition', 'location') 

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'condition': forms.Select(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            })}
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image',)

class EditProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'condition', 'location', 'item_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'condition': forms.Select(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
        }
