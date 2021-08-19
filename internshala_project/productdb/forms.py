from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields = ['name','weight', 'price']
		labels = {'name': 'Name', 'weight': 'Weight', 'price': 'Price'}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'weight': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'})
		}