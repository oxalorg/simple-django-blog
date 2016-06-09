from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.db.models import F
import datetime


# Create your views here.
def archive(request):
    # the day I gave birth to earthlyhumans
    start_year = datetime.date(2016, 6, 7).year
    # yes I think I'm Gaia.
    # No. Just kdding. Move on.
    current_year = datetime.date.today().year
    context = {'archive': []}
    for year in range(current_year, start_year - 1, -1):
        posts = Post.objects.filter(pub_date__year=year).order_by('-pub_date')
        context['archive'].append({'year': year, 'posts': posts})
    return base_render(request, 'blog/archive.html', context)


def front(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {'posts': posts}
    return base_render(request, 'blog/front.html', context)


def about(request):
    return base_render(request, 'blog/about.html')


def support(request):
    return base_render(request, 'blog/support.html')


def contact(request):
    return base_render(request, 'blog/contact.html')


def article(request, slug):
    post = Post.objects.filter(slug=slug)
    post.update(view_count=F('view_count') + 1)
    context = {'post': post[0]}
    return base_render(request, 'blog/article.html', context)


def update_with_popular_posts(context={}):
    context['popular_posts'] = Post.objects.order_by('-view_count')[:5]
    return context


def base_render(request, template, context={}, *args, **kwargs):
    context = update_with_popular_posts(context)
    return render(request, template, context, *args, **kwargs)
