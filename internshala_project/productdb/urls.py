from django.urls import path
from productdb import views

urlpatterns = [
	path('home/', views.home, name='home'),
	path('addproduct/', views.addProduct, name='addproduct'),
	path('updateproduct/<int:id>/', views.updateProduct, name='updateproduct'),
	path('deleteproduct/<int:id>/', views.deleteProduct, name='deleteproduct'),
]