from django.shortcuts import render, get_object_or_404
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
    html = Markdown2Html().convert(dedent("""
    We have, on an average, 7 minutes of your time before you leave this page and we can no longer jam an impression on you. But we feel that your time is valuable, so here we go.

    ### Earthly Humans

    We've grown accustomed to view everything from our tiny modern life bubble. We've grown so dependent on technology, entertainment, and social media that we've forgotten to live. When was the last time you were bored and you had nothing to do? How many posts do you read on your social feed daily? and how much of it actually makes you feel good?

    Earthly Humans is a self exploring journey and an initiative to make lives more meaningful, by allowing people to connect, understand, and enjoy the melodic convergence of earth and humans. This is our visison, but we'll execute it differently.

    We believe that simple is better than complicated, and that less is actually more. So we won't be wasting your time with fluff, instead we'll use a serene combination of thoughts and art to convey our message.

    ---

    ### Call me maybe?

    Feel free to drop in an email at [gaia@earthlyhumans.com](gaia@earthlyhumans.com). We've got a ninja monkey deployed (yeah that's me) who will take care of the emails you send.

    <small><em>Fun fact: Gaia is the goddess of earth. She's the mother of all gods, titans, and the entire universe in the greek mythology. In religions and mythologies all across the world, there is a great importance given to the earth, maybe it's time we give her too!</em></small>

    You can also contact us using the form below:

    <form method="POST" action="http://mitesh.ninja/api/sendForm/gaia@earthlyhumans.com/">
    <div class="row">
        <div class="col-md-12">
            <div class="form-group">
                <textarea class="form-control" rows="4" placeholder="Message" required=""></textarea>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-4">
            <div class="form-group">
                <input class="form-control" placeholder="email@address.com"type="email" id="senderEmail" name="senderEmail" value="" required>
            </div>
        </div>
        <div class="col-sm-4">
            <div class="form-group">
                <input class="form-control" placeholder="Name" type="text" id="senderName" name="senderName" value="" required>
            </div>
        </div>
        <div class="col-sm-4">
            <div class="form-group">
                <input class="form-control btn btn-primary" type="submit" value="Send" name="submit" />
            </div>
        </div>
    </div>
    <br>
    </form>

    ---

    ### Show us some love

    Currently we remain ad-free, and I will be paying the bills out of my own pockets. But you're welcome to help us pay our server and hosting bills by leaving a small donation ($6 will cover our monthly expenses).

    ---

    ### WE not ME

    I keep using 'we', instead of 'me' because I want to encourage anyone to come and help in this effort.

    List of all researchers, contributors, supporters, and volunteers:

    * Mitesh Shah - [miteshshah.com](http://miteshshah.com)
    """))
    context = {'about_html': html}
    return base_render(request, 'blog/about.html', context)


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
