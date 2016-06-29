from __future__ import unicode_literals

from django.db import models


class Paste(models.Model):

    SYNTAX_HIGHLIGHTING = (('java', 'JAVA'),
                           ('ruby', 'RUBY'),
                           ('python', 'PYTHON'),
                           ('html', 'HTML'),
                           ('c', 'C'))

    title = models.CharField(max_length=200)
    syntax = models.CharField(choices=SYNTAX_HIGHLIGHTING, max_length=10, default='python')
    paste = models.TextField()
    slug = models.SlugField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
