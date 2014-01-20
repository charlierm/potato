from django.db import models
from django.template import defaultfilters
from django.contrib.auth.models import User
import datetime
import markdown2

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250) #TODO: Warn user if title is over 70 chars.
    slug = models.SlugField(blank=True)
    content = models.TextField()
    rendered = models.TextField(blank=True)
    draft = models.BooleanField(default=True)
    pinned = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='posts_created')
    modified_by = models.ForeignKey(User, related_name='posts_modified')
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        self.rendered = markdown2.markdown(self.content, extras=["fenced-code-blocks", 'footnotes', 'wiki-tables'])
        super(Post, self).save(*args, **kwargs)

    def is_recent(self):
        if self.date_created.date < datetime.datetime.now()-datetime.timedelta(hours=48):
            return True
        else:
            return False

    @staticmethod
    def im_a_method(something, something_else, test=23):
        """

        :param something:
        :param something_else:
        :param test:
        :rtype: .. py
        """
        pass


    def __unicode__(self):
        return "<Post: {0}>".format(self.title[0:50])

    class Meta:
        ordering = ["-date_created"]

    @models.permalink
    def get_absolute_url(self):
        return ('detail', (), {'slug': self.slug})



class Tag(models.Model):
    title = models.CharField(max_length=30, primary_key=True)

