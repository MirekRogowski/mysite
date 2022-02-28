from django.shortcuts import render, redirect
from . forms import SubscribersForm, MailMessageForm
from django.views.generic import CreateView
from . models import MailMessage
from django.contrib import messages
from django.core.mail import send_mail
from django.apps import apps
from django.conf import settings
from django.urls import reverse_lazy

# Create your views here.


def subscribers(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Twój enal został dodany do Newslettera')
            return redirect('subscribers')
    else:
        form = SubscribersForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/subscribers.html', context)


class SendLetter(CreateView):
    model = MailMessage
    form_class = MailMessageForm
    template_name = 'newsletter/sendletter.html'
    success_url = reverse_lazy('send-letter')

    def form_valid(self, form):
        form.send()
        messages.add_message(self.request, messages.SUCCESS, 'Wysłano email')
        return super().form_valid(form)


def send_letter(request):
    # emails = list(apps.get_model("newsletter.Subscribers").objects.all().values_list("email"))
    emails = list(apps.get_model('blog.Newsletter').objects.all().values_list("email"))
    print(emails)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            for mail in emails:
                send_mail(title, message, settings.EMAIL_HOST_USER, mail, fail_silently=False)
            messages.success(request, 'Wiadomość została wysłana')
            return redirect('send-letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/sendletter.html', context)
