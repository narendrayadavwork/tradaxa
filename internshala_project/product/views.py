from django.shortcuts import render, redirect
from .models import ProductData

from .forms import ProductForm
from django.contrib import messages

# Create your views here.

def index(request):
	prods = ProductData.objects.all()
	return render(request, 'product_temp/index.html', {'prods': prods})

def addProduct(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			weight = form.cleaned_data['weight']
			price = form.cleaned_data['price']
			pdct = Product(name=name, weight=weight, price=price)
			pdct.save()
			form = ProductForm()
			messages.success(request, 'Data Inserted Successfully !!!')
	else:
		form = ProductForm()
	return render(request, 'product_temp/add_product.html', {'form': form})

def updateProduct(request, id):
	product = ProductData.objects.get(id=id)
	if request.method == "POST":
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('/product/index/')
			messages.success(request, "Product Updated Successfully !!!")	
	else:
		form = ProductForm()
	return render(request, 'product_temp/update_product.html', {'product': product})


def deleteProduct(request, id):
	product = ProductData.objects.get(id=id)
	product.delete()
	messages.success(request, "Product Deleted Successfully !!!")
	return redirect('/product/index/')