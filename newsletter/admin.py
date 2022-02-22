from django.contrib import admin
from . models import Subscribers, MailMessage


# Register your models here.
admin.site.register(Subscribers)
admin.site.register(MailMessage)
