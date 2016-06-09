from django.forms import ModelForm
from blog.models import Post
from blog.utils import Markdown2Html, Slugger


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = []

    def clean_html(self):
        data = self.cleaned_data['body']
        return Markdown2Html().convert(data)

    def clean_slug(self):
        title = self.cleaned_data['title']
        slug = self.cleaned_data['slug']
        if slug == '':
            return Slugger().slug(title)
        else:
            return Slugger().slug(slug)
