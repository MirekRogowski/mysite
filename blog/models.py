from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
# from tinymce.models import HTMLField


class Category(models.Model):
    content = models.CharField(max_length=30)

    def __str__(self):
        return self.content


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE)
    status = models.CharField(choices=(('publish', 'opublikuj'), ('draft', 'szablon')), max_length=10, default='draft')
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return f"{self.author} - {self.title} -{self.category.content}"


class Comment(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.post


