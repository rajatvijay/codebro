from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from pygments.lexers import get_all_lexers


class Paste(models.Model):
    LEXERS = [item for item in get_all_lexers() if item[1]]
    LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

    title = models.CharField(max_length=200)
    syntax = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, default='python')
    paste = models.TextField()
    slug = models.SlugField(max_length=6, unique=True, db_index=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_share_url(self):
        return reverse('paste_detail', args=[self.slug])

    def get_raw_url(self):
        return reverse('paste_raw', args=[self.slug])
