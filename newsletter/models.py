from django.db import models
from django.apps import apps


# Register your models here.
class Subscribers(models.Model):
    email = models.EmailField(null=True, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_emails(self):
        return list(apps.get_model("letter.Subscribers").objects.all().values_list("email"))

    # def send_emails(self):
    #     return send_mail(self.post.title, self.post.content, settings.EMAIL_HOST_USER, self.get_emails())


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title

