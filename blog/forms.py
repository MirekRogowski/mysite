from django import forms
from .models import Post, Category, Comment, Newsletter, NewsLetterPost
import blog.models
from django.apps import apps
from django.conf import settings
from django.core.mail import send_mail


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('author', 'category', 'title', 'content', 'status')
        fields = ( 'title', 'content','category', 'status')
        widgets = {
            # 'author': forms.Select(attrs={'class': 'col-sm-12 '},),
            'category': forms.Select(attrs={'class': 'col-sm-12'}),
            'title': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'col-sm-12'}),
        }
        labels = {
            # 'author': 'Autor',
            'category': "Wybierz kategorię",
            'title': "Tytuł postu",
            'content': 'Treśc postu',
            'status': "Status postu"
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name_category': forms.TextInput(attrs={'class': 'ol-sm-12'}),
        }
        labels = {
            'name': 'Wpisz nową kategorię',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Podaj Nick',
            'email': "Wpisz email",
            'content': 'Wpisz komentarz',
        }


class NewsLetterForm(forms.ModelForm):
    # email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
    #     'placeholder': 'Wpisz email'}))

    class Meta:
        model = Newsletter
        fields = ('email',)
        labels = {
            'email': "Wpisz email",
        }


class NewsLetterPostForm(forms.ModelForm):
    model = Post
    fields = ('title', 'content', 'status')
    labels = {
        'title': "Tytuł postu",
        'content': 'Treść postu',
        'status': "Status postu"
    }


class ContactForm(forms.Form):

    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )


