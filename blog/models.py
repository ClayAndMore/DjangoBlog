import datetime
from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, blank=False, null=False)
    content = models.TextField(max_length=100, blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(protocol='both',blank=True, null=True, default='0.0.0.0')

    class Meta:
        db_table = 'message'

class Essay(models.Model):
    id=models.AutoField(primary_key=True)
    text = models.TextField()
    text_time = models.DateTimeField(default=datetime.datetime.now, blank=True)

    @property
    def get_month(self):
        return self.text_time.month
    @property
    def get_day(self):
        return self.text_time.day

    class Meta:
        db_table = 'essays'

# the images models
class Images(models.Model):
    IMAGE_KIND = (
            ('trace',u'旅游'),
            ('movies',u'电影'),
            ('books',u'书籍'),
            ('anime',u'动漫'),
            ('life',u'生活'),
    )

    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255, blank=False, null=False) # 图片外链
    img_time = models.DateTimeField(blank=False) 
    kind = models.CharField(max_length=50, blank=False, null=False, choices=IMAGE_KIND)
    introduce = models.CharField(max_length=255, blank=True, null=True) # 图片简介

    essay_rel = models.ForeignKey(Essay, related_name="its_images", db_constraint=False, blank=True, null=True, on_delete=models.SET_NULL)

