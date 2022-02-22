from django.conf import settings
from django.db import models
from django.apps import apps
from django.core.mail import send_mail


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

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
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.PROTECT, default=1)
    status = models.CharField(choices=options, max_length=10, default='draft')

    def __str__(self):
        return f"{self.author} : {self.title} : {self.category.name}"

    class Meta:
        ordering = ('-created_date',)
        # get_latest_by = [{'status': 'publish'},]
        get_latest_by = ['pk',]


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


class Newsletter(models.Model):
    email = models.EmailField(null=True, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def display(self):
        print(self.email)


class NewsLetterPost(models.Model):
    post = models.ForeignKey('Post', related_name='newsletterpost', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    emails = models.JSONField(null=True)

    def __str__(self):
        return f'{self.post} : {self.date} : {self.emails}'

    def get_emails(self):
        return list(apps.get_model("blog.Newsletter").objects.all().values_list("email", flat=True))

    def send_emails(self):
        return send_mail(self.post.title, self.post.content, settings.EMAIL_HOST_USER, self.get_emails())
