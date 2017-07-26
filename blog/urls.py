# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'index'),
        url(r'^posts/(?P<post_class>[a-zA-Z]+)/(?P<post_type>[a-zA-Z0-9]+)/$', views.get_posts_list, name = 'posts_list'),
        url(r'^post/(?P<inum>[0-9]+)/$', views.get_post, name = 'post'),
        url(r'^archiving/$', views.archiving, name = 'archiving'),
        # url(r'^aboutMe/$', views.about_me, name = 'aboutMe'),
        ]
        
