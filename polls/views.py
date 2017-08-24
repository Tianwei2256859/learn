# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone


def index(request, template_name='index.html'):
    ip = request.META.get('REMOTE_ADDR')
    now = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

    data = {}
    if request.method == 'GET':
        return render(request, template_name, context={
            'ip': ip,
            'now': now,
            'data': data
        })

    if request.method == 'POST':
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        like = request.POST.getlist('like', [])
        sex = request.POST.get('sex', '')
        fruit = request.POST.get('fruit', '')

        data['name'] = name
        data['password'] = password
        data['like'] = like
        data['sex'] = sex
        data['fruit'] = fruit
        return render(request, template_name, context={
            'ip': ip,
            'now': now,
            'data': data
        })
