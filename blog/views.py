import os
import re
import copy
import stat
import json

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from .for_path import k_v_tree, to_bootstrap_tree 

DIR = '/home/Memo/'
find_dir = '/root/posts' 
tree_list = to_bootstrap_tree(k_v_tree(DIR))
tree_list_json = json.dumps(tree_list)
def dir_list(request):
    return HttpResponse(tree_list_json, content_type="application/json")
 
# 博客列表
def get_posts_list(request, post_class, post_type):
    #data = {'inum': 0,'title':'','time':''}
    #data_list = []
    #global find_dir
    #find_dir = '/root/posts/'+str(post_class)+'/'+str(post_type)
    #for filename in os.listdir(find_dir):
    #    data['title'] = filename
    #    filename_all = find_dir+'/'+str(filename)
    #    file_open = open(filename_all)
    #    data['inum'] = os.stat(filename_all).st_ino
    #    index = 1
    #    for line in file_open:
    #        index+=1
    #        # 找前四行的日期
    #        if 'date' in line or index>4:
    #            re_str = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    #            r = re.search(re_str, line.strip())
    #            if r:
    #                data['time'] = r.group(0)
    #            data_list.append(copy.deepcopy(data))
    #            break
    # 
    file_path = '/home/Memo/Ab___Python/.md'
    with open(file_path) as f:
        file_content = f.read()
    data_list = [{'inum': 111, 'title': 'ttt', 'time': 20180405}]
    return render(request,'post_list.html',{'file_content':file_content})
    #return render(request,'post_list.html')

#@api_view(['GET'])
def get_post(request):
    # 注意目录
    try:
        file_path = '/home/Memo/Ab___Python/YAML.md'
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
    print ('AAAAAAAA', filename)
    if not filename.endswith('.md') and '..' in filename: # 防止有人跳目录。
        return HttpResponse(json.dumps('no'), content_type="application/json")
    try:
        file_popen = os.popen('find %s -name "%s"'%(DIR,filename))
        file_path = file_popen.read().strip('\n')
        file_popen.close()
        with open(file_path) as f:
            file_content = f.read()
    except FileNotFoundError:
        return HttpResponse(json.dumps('no'), content_type="application/json")
        
    file_content_json = json.dumps(file_content)

    return render(request, 'post_list.html',{'file_content':file_content})
    #return HttpResponse(file_content_json, content_type="application/json")

# 归档
@api_view(['GET'])
def archiving(request):
    return Response('归档')

# 关于我
@api_view(['GET'])
def about_me(request):
    return Response('关于我')
