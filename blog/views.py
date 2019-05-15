# coding:utf-8
import os
import re
import copy
import stat
import json

from django.shortcuts import render
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from .for_path import k_v_tree, to_bootstrap_tree, get_tags_nums, get_tags_conf

DIR = './Memo/' # 相对于运行目录
find_dir = '/root/posts' 
tree_list = to_bootstrap_tree(k_v_tree(DIR))
tree_list_json = json.dumps(tree_list)
def dir_list(request):
    return HttpResponse(tree_list_json, content_type="application/json")
 
# 博客列表
def get_posts_list(request):

    data_list = [{'inum': 111, 'title': 'ttt', 'time': 20180405}]
    return render(request,'post_list.html', {'file_content':'nono'})
    #return render(request,'post_list.html')

#@api_view(['GET'])
def get_post(request):
    # 注意目录
    try:
        file_path = DIR + 'Ab___Python/YAML.md'
        with open(file_path) as f:
            file_content = f.read()
            #return Response(f.read())
            return render(request, 'post_list.html',{'file_content':file_content})
    except Exception as e:
        print(Exception)
        print(e)
        print('dddddddd')
        # return Response('不可修改参数')
        return render(request, 'post_content.html')

# 具体博文
def one_markdown(request, filename):
    print(111111,os.getcwd(), settings.BASE_DIR)
    if '..' in filename: # 防止有人跳目录。
        return HttpResponse(json.dumps('no'), content_type="application/json")
    try:
        file_popen = os.popen('find %s -name "%s"'%(DIR,filename))
        file_path = file_popen.read().strip('\n')
        file_popen.close()
        with open(file_path) as f:
            file_content = f.read()
    except FileNotFoundError:
        return HttpResponse(json.dumps('no such file'), content_type="application/json")
        
    file_content_json = json.dumps(file_content)

    return render(request, 'post_list.html', {'file_content':file_content})
    #return HttpResponse(file_content_json, content_type="application/json")

# 分类
@api_view(['GET'])
def archives(request):
    archives = get_tags_nums(DIR)
    # from pprint import  pprint
    # pprint(archives)
    return render(request, 'archives.html', {'archives': archives})


@api_view(['GET'])
def archive_get(request):
    archive = request.GET.get('tag','')
    all_achives = get_tags_conf(DIR)
    if archive and archive in all_achives:
        num = len(all_achives[archive])
        contents = all_achives[archive]
        # print(1111, num )
        return render(request, 'archive_contents.html',{
            'archive': archive,
            'contents': contents,
            'num': num
        })

    else:
        return 'no this archive'

# 关于我
@api_view(['GET'])
def about_me(request):
    return Response('关于我')
