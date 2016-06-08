from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'body']}),
        ('Meta Info', {'fields': ['pub_date']})
    ]
    list_display = ('title', 'pub_date')
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
