from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        '_type',
        'title',
        'content',
        'author',
        'created_at',
        'updated_at'
    )
    search_fields = (
        'title',
        'content'
    )


