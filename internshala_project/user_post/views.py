from django.shortcuts import render, redirect
from .models import Post

from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
	posts = Post.objects.all()
	context = {
		'posts': posts,
	}
	return render(request, 'user_blog/home.html', context)

def about(request):
	return render(request, 'user_blog/about.html')

def contact(request):
	return render(request, 'user_blog/contact.html')

# login
def user_login(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = LoginForm(request=request, data=request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				upass = form.cleaned_data['password']
				user = authenticate(username=uname, password=upass)
				if user is not None:
					login(request, user)
					messages.success(request, 'Logged In Successfully !!!')
					return redirect('/dashboard/')
		else:
			form = LoginForm()
		return render(request, 'user_blog/login.html', {'form': form})
	else:
		return redirect('/dashboard/')


# dashboard
def dashboard(request):
	if request.user.is_authenticated:
		posts = Post.objects.all()
		context = {
			'posts': posts,
		}
		return render(request, 'user_blog/dashboard.html',context)
	else:
		return redirect('/login/')

# logout
def user_logout(request):
	logout(request)
	return redirect('/login/')

# signup
def signup(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Congratulations!! You have become an Author...')
			form.save()
	else:
		form = SignUpForm()
	return render(request, 'user_blog/signup.html', {'form': form})

# Add New Post
def add_newPost(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = PostForm(request.POST)
			if form.is_valid():
				title = form.cleaned_data['title']
				body = form.cleaned_data['body']
				author = form.cleaned_data['author']
				pst = Post(title=title, body=body, author=author)
				pst.save()
				form = PostForm()
		else:
			form = PostForm()
		return render(request, 'user_blog/add_post.html', {'form': form})
	else:
		return redirect('/login/')

# Update Post
def update_post(request, id):
	if request.user.is_authenticated:
		if request.method == "POST":
			post = Post.objects.get(pk=id)
			form=PostForm(request.POST, instance=post)
			if form.is_valid():
				form.save()
		else:
			post=Post.objects.get(pk=id)
			form = PostForm(instance=post)
		return render(request, 'user_blog/update_post.html', {'form': form})
	else:
		return redirect('/login/')

# Delete Post
def delete_post(request, id):
	if request.user.is_authenticated:
		if request.method == "POST":
			post=Post.objects.get(pk=id)
			post.delete()
		return redirect('/dashboard/')
	else:
		return redirect('/login/')