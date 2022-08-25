from datetime import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def post(request):
    return render(request,'blog/post.html')

def posts(request):
    u = {"name":"mohammad","lastname":"nozari"}
    p = {"title":"first post title","body":"first post body","date":datetime(2022,1,1,20,20,20,20)}
    c = {"user":u,"post":p}
    return render(request,'blog/posts.html',c)