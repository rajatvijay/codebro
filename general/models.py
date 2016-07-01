from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class Paste(models.Model):

    LEXERS = [item for item in get_all_lexers() if item[1]]
    LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
    STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

    title = models.CharField(max_length=200)
    syntax = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, default='python')
    paste = models.TextField()
    slug = models.SlugField(max_length=6, unique=True, db_index=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    highlighted = models.TextField()
    linenos = models.BooleanField(default=False)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
