from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True)
    body = models.TextField()
    html = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    view_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
