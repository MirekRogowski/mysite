from django.contrib import admin
from . models import Post, Category, Comment, Newsletter


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", 'author', 'status')


admin.site.register(Post, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Newsletter)