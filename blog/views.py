from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Post
from django.db.models import F
from .utils import Markdown2Html
from textwrap import dedent
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
    html = Markdown2Html().convert(dedent("""\
    We have, on an average, 7 minutes of your time before you leave this page and we can no longer jam an impression on you. But we feel that your time is valuable, so here we go.

    ### Earthly Humans

    We've grown accustomed to view everything from our tiny modern life bubble. We've grown so dependent on technology, entertainment, and social media that we've forgotten to live. When was the last time you were bored and you had nothing to do? How many posts do you read on your social feed daily? and how much of it actually makes you feel good?

    Earthly Humans is a self exploring journey and an initiative to make lives more meaningful, by allowing people to connect, understand, and enjoy the melodic convergence of earth and humans. This is our visison, but we'll execute it differently.

    We believe that simple is better than complicated, and that less is actually more. So we won't be wasting your time with fluff, instead we'll use a serene combination of thoughts and art to convey our message.

    ### WE not ME

    I keep using 'we', instead of 'me' because I want to encourage anyone to come and [help in this effort](/support)

    List of all researchers, contributors, supporters, and volunteers:

    * Mitesh Shah - [miteshshah.com](http://miteshshah.com)
    """))
    context = {'page_content': html}
    return base_render(request, 'blog/about.html', context)


def support(request):
    html = Markdown2Html().convert(dedent("""\
    # Show us some love <3

    Currently we remain ad-free, and I will be paying the bills out of my own pockets. But you're welcome to help us pay our server and hosting bills by leaving a small donation ($6 will cover our monthly expenses).

    You can also support us

    * by spreading the word. Share our initiative with humans you care about!
    * by sending feedback at [hermes@earthlyhumans.com](mailto:hermes@earthlyhumans.com)
        - <small><em>Fun fact: Hermes is the god of trade, communication, and language in the greek mythology.</em></small>
    * by contributing your thoughts. Send us your views on *anything* at [athena@earthlyhumans.com](mailto:athena@earthlyhumans.com)
        - <small><em>Fun fact: Athena is the goddess of intelligence and wisdom in the greek mythology.</em></small>
    """))
    context = {'page_content': html}
    return base_render(request, 'blog/support.html', context)


def contact(request):
    return base_render(request, 'blog/contact.html')


def article(request, slug):
    post = get_list_or_404(slug=slug)
    post.update(view_count=F('view_count') + 1)
    context = {'post': post[0]}
    return base_render(request, 'blog/article.html', context)


def update_with_popular_posts(context={}):
    context['popular_posts'] = Post.objects.order_by('-view_count')[:5]
    return context


def base_render(request, template, context={}, *args, **kwargs):
    context = update_with_popular_posts(context)
    return render(request, template, context, *args, **kwargs)
