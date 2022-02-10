from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce.models import HTMLField


class Category(models.Model):
    content = models.CharField(max_length=30)
    # post = models.ForeignKey(Post, on_delete=models.)

    def __str__(self):
        return self.content

    # def get_absolute_url(self):
    #     return reverse("blog-home")


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    text =  HTMLField()
    # created_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=200, default='uncatedorized')
    # categories = models.ManyToManyField(Category)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return f"{self.author} - {self.title} -{self.category}"

    def get_absolute_url(self):
        return reverse("blog-home")


class Comment(models.Model):
    content = models.TextField()
    # created_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


