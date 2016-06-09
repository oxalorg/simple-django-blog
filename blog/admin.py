from django.contrib import admin
from blog.forms import PostForm
from blog.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    fieldsets = [
        (None, {'fields': ['title', 'body', 'html']}),
        ('Meta Info', {'fields': ['slug', 'pub_date', 'view_count']})
    ]
    list_display = ('title', 'pub_date')
    search_fields = ['title']

    def get_readonly_fields(self, request, obj=None):
        return ('html')


admin.site.register(Post, PostAdmin)
