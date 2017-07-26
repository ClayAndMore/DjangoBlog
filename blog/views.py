import os
import re
import copy
import stat

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# 首页
@api_view(['GET'])
def index(request):
    return Response('post首页')

# 定义一个全局变量，用于标识当前用户所在页级
find_dir = '' 

# 博客列表
def get_posts_list(request, post_class, post_type):
    data = {'inum': 0,'title':'','time':''}
    data_list = []
    global find_dir
    find_dir = '/root/posts/'+str(post_class)+'/'+str(post_type)
    for filename in os.listdir(find_dir):
        data['title'] = filename
        filename_all = find_dir+'/'+str(filename)
        file_open = open(filename_all)
        data['inum'] = os.stat(filename_all).st_ino
        index = 1
        for line in file_open:
            index+=1
            # 找前四行的日期
            if 'date' in line or index>4:
                re_str = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
                r = re.search(re_str, line.strip())
                if r:
                    data['time'] = r.group(0)
                data_list.append(copy.deepcopy(data))
                break
     
    return render(request,'post_list.html',{'data': data_list})

# 具体博文
#@api_view(['GET'])
def get_post(request, inum):
    # 注意目录
    try:
        file_popen = os.popen('find '+find_dir+' -inum '+str(inum))
        file_path = file_popen.read().strip('\n')
        file_popen.close()
        with open(file_path) as f:
            file_content = f.read()
            print(file_content)
            #return Response(f.read())
            return render(request, 'post_content.html',{'file_content':file_content})
    except Exception as e:
        print(Exception)
        print(e)
        # return Response('不可修改参数')
        return render(request, 'post_content.html')

# 归档
@api_view(['GET'])
def archiving(request):
    return Response('归档')

# 关于我
@api_view(['GET'])
def about_me(request):
    return Response('关于我')
