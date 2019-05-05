# -*- coding:utf-8 -*-
import sys
import json
import datetime

from .form import MessageForm 
sys.path.append("..") # 将上级目录导入环境变量
from blog.models import Message, Essay, Images
from blog.serializers import EssaySerializer,ImagesSerializer

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    #return render(request, 'index.html')
    return HttpResponseRedirect(reverse("aboutMe"))

def about_me(request):
    print('AAAAAAA')
    return render(request, 'aboutMe.html')

def message(request):
    form = MessageForm()
    messages = []
    error = ''
    messages = Message.objects.all().order_by('-time')
    if request.method == 'POST':
        conf = {'message': 'disabled'}
        with open('./toggle_message.conf', 'r') as f:
            conf = json.load(f)
        if conf.get('message', 'disabled') == 'disabled':
            error = '该功能现只对个人开放'
            return render(request, 'message.html', {'form': form, 'messages': messages, 'error': error})
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

    return render(request, 'message.html', {'form':form,'messages':messages,'error':error})



def mylife(request):
    years = Essay.objects.values('text_time')
    years_dis = set()
    for year in years:
        years_dis.add(year['text_time'].year)
    return render(request, 'life.html', {'years_dis': sorted(years_dis)})

@api_view(['GET'])
def life_list(request, year):
    try:
        essaies = Essay.objects.filter(text_time__year=year).order_by('text_time')
    except Exception:
        print(Exception)
    #image = essaies[0].essay.all()
    serializer = EssaySerializer(essaies,many=True)
    return Response(serializer.data)
