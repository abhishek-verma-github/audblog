from django.shortcuts import render
from .models import Blog
# Create your views here.


def home(request):

    blogs = Blog.objects.all()
    context = {
        'posts': blogs
    }
    return render(request, 'blog/home.html', context)
