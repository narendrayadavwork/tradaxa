from django.urls import path
from product import views

urlpatterns = [
	path('index/', views.index, name='home'),
	path('addproduct/', views.addProduct, name='addproduct'),
	path('updateproduct/<int:id>/', views.updateProduct, name='updateproduct'),
	path('deleteproduct/<int:id>/', views.deleteProduct, name='deleteproduct'),
]