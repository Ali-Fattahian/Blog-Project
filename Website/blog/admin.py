from django.contrib import admin
from .models import Tag, Author, Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tag', 'date')
    list_display = ('title', 'date', 'author')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
