from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    options = (
        ('publish', 'opublikuj'),
        ('draft', 'szablon')
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE)
    status = models.CharField(choices=options, max_length=10, default='draft')

    def __str__(self):
        return f"{self.author} - {self.title} -{self.category.name}"

    class Meta:
        ordering = ('-created_date',)


class Comment(models.Model):
    name = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=100, blank=True, default="")
    content = models.TextField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return f"Comment by {self.name}"
