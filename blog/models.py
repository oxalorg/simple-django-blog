from django.db import models


# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=250)
    post_body = models.TextField()
    pub_date = models.DateTimeField('date published')
    view_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return "title: {post.post_title}\n"\
                "body: {post.post_body}\n"\
                "pub_date: {post.pub_date}\n"\
                "view_count: {post.view_count}\n"\
                "likes: {post.likes}".format(post=self)
