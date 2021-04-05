from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name                    = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('community:board')


class Post(models.Model):
    title                   = models.CharField(max_length=255)
    author                  = models.ForeignKey(User, on_delete=models.CASCADE)
    body                    = RichTextField(blank=True, null=True)
    post_date               = models.DateField(auto_now_add=True)
    post_created            = models.DateTimeField(auto_now_add=True)
    category                = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('community:board')

    class Meta:
        ordering            = ('post_created',)

class Comment(models.Model):
    post                    = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name                    = models.CharField(max_length=250)
    body                    = models.TextField()
    date_added              = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    class Meta:
        ordering            = ('date_added',)


