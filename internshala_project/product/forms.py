from django import forms

from .models import ProductData

class ProductForm(forms.ModelForm):
	class Meta:
		model=ProductData
		fields = ['name','weight', 'price']
		labels = {'name': 'Name', 'weight': 'Weight', 'price': 'Price'}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'weight': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'})
		}