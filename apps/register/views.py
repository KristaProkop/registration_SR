# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from .forms import Name_Email_Form, Name_Email_Password_Form, Credit_Card_Form

def index(request):
    return render(request, 'register/index.html')

def display_modal(request, id):
    modal_dict = {
        1: Name_Email_Form(),
        2: Name_Email_Password_Form(),
        3: Credit_Card_Form(),
    }
    context = {
        'form': modal_dict[int(id)],
        'form_id': int(id),
    }
    return render(request, 'register/modal.html', context)

def register(request, form_id):
    if request.method == "POST":
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer, kwargs={form_id})