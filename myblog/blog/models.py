from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    readeble_url = models.CharField(max_length=100, db_index=True, unique=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('category', args=[self.readeble_url, ])


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    readeble_url = models.CharField(max_length=100, db_index=True, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('post', args=[self.readeble_url, ])
