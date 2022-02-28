from django import forms
from .models import Subscribers, MailMessage
from django.apps import apps
from django.conf import settings
from django.core.mail import send_mail


class SubscribersForm(forms.ModelForm):

    class Meta:
        model = Subscribers
        fields = ('email',)
        labels = {
            'email': "Wpisz email",
        }


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'

    def get_info(self):
        clean_data = super().clean()
        title = clean_data.get('title')
        message = clean_data.get('message')
        return title, message

    def send(self):
        emails = list(apps.get_model('blog.Newsletter').objects.all().values_list("email"))
        subject, content = self.get_info()
        for mail in emails:
            send_mail(subject, content, settings.EMAIL_HOST_USER, mail, fail_silently=False)

