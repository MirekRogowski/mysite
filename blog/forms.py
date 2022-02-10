from django import forms
from .models import Post, Category


def category_list():
    category = Category.objects.all().values_list('content', 'content')
    choices_list = []
    for item in category:
        choices_list.append(item)
    return choices_list


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','category','title',"title_tag", 'text', 'published_date')
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_list(), attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control'})
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', "title_tag", 'text', 'author')
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_list(), attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('content',)
        widgets = {
            'name_category': forms.TextInput(attrs={'class': 'form-control'}),

        }