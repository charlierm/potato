from django.db import models
from django.template import defaultfilters
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250) #TODO: Warn user if title is over 70 chars.
    slug = models.SlugField()
    content = models.TextField()
    draft = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='posts_created')
    modified_by = models.ForeignKey(User, related_name='posts_modified')

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return "<Post: {0}>".format(self.title[0:50])

