from django.shortcuts import render
from .models import Post

# each page also needs to be added to urls.py 
def home(request):
    context = {
    'posts': Post.objects.all() # get posts from the database
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})