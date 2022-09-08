from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def post(request):
    return render(request,'blog/post.html')

def posts(request):
    u = User.objects.first()
    
    p =Post.objects.first()
    c = {"user":u,"post":p}
    return render(request,'blog/posts.html',c)