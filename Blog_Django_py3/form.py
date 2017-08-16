# -*- coding:utf-8 -*-
from django.forms import ModelForm 
from blog.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('name','content',)
