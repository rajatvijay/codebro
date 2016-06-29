from django.shortcuts import render
from .forms import PasteForm

import uuid


def paste_create(request):
    if request.method == 'POST':
        paste_form = PasteForm(data=request.POST)

        if paste_form.is_valid():
            new_paste = paste_form.save(commit=False)
            new_paste.slug = uuid.uuid4().hex[:6].upper()
            new_paste.save()

    else:
        paste_form = PasteForm()

    return render(request, 'general/paste/paste_form.html', {'form': paste_form})

