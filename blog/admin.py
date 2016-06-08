from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['post_title', 'post_body']}),
        ('Meta Info', {'fields': ['pub_date']})
    ]
    list_display = ('post_title', 'pub_date')
    search_fields = ['post_title']


admin.site.register(Post, PostAdmin)
