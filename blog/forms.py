from django import forms
from .models import Post, Category, Comment


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
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }