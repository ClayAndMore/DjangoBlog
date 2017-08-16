# -*- coding:utf-8 -*-
import sys
import datetime

from .form import MessageForm 
sys.path.append("..") # 将上级目录导入环境变量
from blog.models import Message 

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    #return render(request, 'index.html')
    return HttpResponseRedirect(reverse("aboutMe"))

def about_me(request):
    return render(request, 'aboutMe.html')

def message(request):
    form = MessageForm()
    messages = []
    error = ''
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            ip = request.META['REMOTE_ADDR']
            messages = Message.objects.filter(ip=ip).order_by('-time') 
            if messages:
                time_del = datetime.datetime.now()-messages[0].time.replace(tzinfo=None)
                if time_del.seconds < 600:
                    error ='十分钟内只能留言一次'
                    form = MessageForm()
                    messages = Message.objects.all().order_by('-time') 
                    return render(request, 'message.html', {'form':form,'messages':messages,'error':error})

            form_temp=form.save(commit=False)
            form_temp.ip = ip
            form_temp.save()
            return HttpResponseRedirect(reverse("messages"))
        else:
            print(form.errors.as_data())

    # 渲染留言列表
    else:
        messages = Message.objects.all().order_by('-time') 
    return render(request, 'message.html', {'form':form,'messages':messages,'error':error})


def archiving(requst):
    return None
