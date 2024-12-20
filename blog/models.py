from django.db import models
from accounts.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Post(models.Model):
    '''
    this is a class for define post for blog
    '''
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    status = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
