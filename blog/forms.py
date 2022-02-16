from django import forms
from .models import Post, Category, Comment, Newsletter


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'content', 'status')
        widgets = {
            'author': forms.Select(attrs={'class': 'col-sm-12'}),
            'category': forms.Select(attrs={'class': 'col-sm-12'}),
            'title': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'col-sm-12'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'content','status')
        widgets = {
            'author': forms.Select(attrs={'class': 'col-sm-12'}),
            'category': forms.Select(attrs={'class': 'col-sm-12'}),
            'title': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'col-sm-12'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name_category': forms.TextInput(attrs={'class': 'ol-sm-12'}),
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


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Twój email'}))

    class Meta:
        model = Newsletter
        fields = ('email',)


class SendMailForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content','status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'col-sm-12'}),
        }

