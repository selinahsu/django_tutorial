from django.db import models
from django.utils import timezone

# database relationships:
# the (default) django user model has a one-to-many relationship with the posts model 
  # one user can create many posts, but a post can only have one author 
from django.contrib.auth.models import User


class Post(models.Model): 
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now)
  # on_delete is used to delete the post if its authoring user gets deleted
  author = models.ForeignKey(User, on_delete=models.CASCADE) 

  def __str__(self):
    return self.title