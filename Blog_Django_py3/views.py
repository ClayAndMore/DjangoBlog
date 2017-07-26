# -*- coding:utf-8 -*-
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return render(request, 'index_basic.html')

def about_me(request):
    return render(request, 'index0.html')

@api_view(['GET'])
def message(request):
    return Response("留言墙")

