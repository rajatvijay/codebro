import uuid
from django.shortcuts import render, redirect, get_object_or_404
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.special import TextLexer
from .forms import PasteForm
from .models import Paste


def paste_create(request):
    if request.method == 'POST':
        paste_form = PasteForm(data=request.POST)

        if paste_form.is_valid():
            new_paste = paste_form.save(commit=False)
            new_paste.slug = uuid.uuid4().hex[:6].upper()
            new_paste.save()
        return redirect('paste_list')
    else:
        paste_form = PasteForm()

    return render(request, 'general/paste/form.html', {'form': paste_form})


def paste_list(request):
    pastes = Paste.objects.all()
    share_url = {str(paste.title): request.build_absolute_uri(paste.get_share_url()) for paste in pastes}
    raw_url = {str(paste.title): request.build_absolute_uri(paste.get_raw_url()) for paste in pastes}
    return render(request, 'general/paste/list.html', {'pastes': pastes,
                                                       'share_urls': share_url,
                                                       'raw_urls': raw_url})


def paste_detail(request, slug):
    paste = get_object_or_404(Paste, slug=slug)
    share_url = request.build_absolute_uri(paste.get_share_url())
    raw_url = request.build_absolute_uri(paste.get_raw_url())
    return render(request, 'general/paste/detail.html', {'paste': paste,
                                                         'share_url': share_url,
                                                         'raw_url': raw_url})


def paste_raw(request, slug):
    paste = get_object_or_404(Paste, slug=slug)
    raw = highlight(paste.paste, lexer=TextLexer(), formatter=HtmlFormatter())
    return render(request, 'general/paste/raw.html', {'raw': raw})
