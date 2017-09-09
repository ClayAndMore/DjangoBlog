# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Essay, Images

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('__all__')

class EssaySerializer(serializers.ModelSerializer):
    its_images = ImagesSerializer(many=True)

    class Meta:
        model = Essay
        fields = ('text','text_time','its_images','get_month','get_day')





