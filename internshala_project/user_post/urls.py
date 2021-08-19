from django.urls import path
from user_post import views

urlpatterns = [
	path('', views.home),
	path('about/', views.about, name='about'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('signup/', views.signup, name='signup'),
	path('user_logout/', views.user_logout, name='user_logout'),
	path('login/', views.user_login, name='login'),

	path('addpost/', views.add_newPost, name='addpost'),
	path('updatepost/<int:id>/', views.update_post, name='updatepost'),
	path('deletepost/<int:id>/', views.delete_post, name='deletepost'),
]
