from django.core import validators
from django.db import models
from django.db.models.fields import CharField
from django.core.validators import MinLengthValidator

class Author(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 80)
    email_address = models.EmailField(null = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Tag(models.Model):
    caption = CharField(max_length= 50, null = True)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length = 50)
    excerpt = models.CharField(max_length= 200)
    image = models.ImageField(upload_to = 'posts', null = True)
    date = models.DateField(auto_now = True)
    slug = models.SlugField(unique=True) #db_index = True is here by default, we don't have to add it.(it is use to make quering the data more efficient)
    content = models.TextField(validators = [MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete= models.SET_NULL, related_name = 'posts', null = True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'Post Title : {self.title}  |  Post Author : {self.author}'

class Comment(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField()
    comment_content = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')