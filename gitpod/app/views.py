# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'title': 'Home',

    }
    return render(request, 'app/index.html', context)
