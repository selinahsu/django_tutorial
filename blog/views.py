from django.shortcuts import render

# mock data: represent eahc post with a dictionaries
posts = [
  {
    'author': 'Selina Hsu',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'August 27, 2020',
  }, 
  {
    'author': 'Corey Schafer',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'August 28, 2020',
  }, 
]

# each page also needs to be added to urls.py 
def home(request): 
  context = {
    'posts': posts # pass in the list of dictionaries to the posts key
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})