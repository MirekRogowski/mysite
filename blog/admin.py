from django.contrib import admin
from . models import Post, Category, Comment, Newsletter, NewsLetterPost


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", 'author', 'status')

class NewsLetterPosAdmin(admin.ModelAdmin):
    exclude = ('emails', )
    list_display = ('post', )

admin.site.register(Post, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Newsletter)
admin.site.register(NewsLetterPost, NewsLetterPosAdmin)
