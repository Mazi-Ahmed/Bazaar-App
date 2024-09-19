from django import forms
from .models import Product

class NewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'image')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            })}
class EditProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'item_sold')

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
            'image': forms.FileInput(attrs={
                'class': 'w-full py-2 px-4 rounded-xl border'
            })}