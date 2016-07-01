from django.shortcuts import render, redirect
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.other import NullFormatter, RawTokenFormatter
from pygments.lexers import get_lexer_by_name
from pygments.lexers.special import RawTokenLexer, TextLexer

from .forms import PasteForm
from .models import Paste
from django.shortcuts import get_object_or_404

import uuid


def paste_create(request):
    if request.method == 'POST':
        paste_form = PasteForm(data=request.POST)

        if paste_form.is_valid():
            new_paste = paste_form.save(commit=False)
            new_paste.slug = uuid.uuid4().hex[:6].upper()
            lexer = get_lexer_by_name(new_paste.syntax)
            new_paste.linenos = new_paste.linenos and 'table' or False
            options = new_paste.title and {'title': new_paste.title} or {}
            formatter = HtmlFormatter(style=new_paste.style, linenos=new_paste.linenos, **options)
            new_paste.highlighted = highlight(new_paste.paste, lexer, formatter)
            new_paste.save()
        return redirect('post_list')
    else:
        paste_form = PasteForm()

    return render(request, 'general/paste/paste_form.html', {'form': paste_form})


def paste_list(request):
    pastes = Paste.objects.all()

    return render(request, 'general/paste/list.html', {'pastes': pastes})


def paste_detail(request, slug):
    paste = get_object_or_404(Paste, slug=slug)
    return render(request, 'general/paste/detail.html', {'paste': paste})


def paste_formatter(request, slug):
    paste = get_object_or_404(Paste, slug=slug)
    # safe_text = escape(paste.highlighted)
    return render(request, 'general/paste/formatter.html', {'paste': paste})


def paste_raw(request, slug):
    paste = get_object_or_404(Paste, slug=slug)
    lexer = TextLexer()
    formatter = HtmlFormatter()
    raw = highlight(paste.paste, lexer, formatter)
    return render(request, 'general/paste/raw.html', {'paste': paste, 'raw': raw})
