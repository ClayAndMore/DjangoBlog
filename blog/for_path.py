# coding:utf-8
import os,sys,re
import json
import copy
from pprint import pprint
from os.path import basename

from collections import OrderedDict, defaultdict

PY3 = sys.version_info[0] == 3

print(1111,sys.getdefaultencoding())

def k_v_tree(path):
    """ 目录结构变成k-v
    eg:

     'Cb___Sql': {'MySQL安装.md': None,
                  'linux下python与mysql.md': None,
                  'mysql与mongodb的安装与配置.md': None,
                  'slite.md': None,
                  '数据库与SQL.md': None},
     'Cc___Nosql': {'Celery与消息队列.md': None,
                    'Elasticsearch.md': None,
                    'MongoDB': {'Mongo CURD.md': None,
                                'MongoDB(1).md': None,
                                'MongoDB(2).md': None,
    """
    k_v_dict = OrderedDict()
    for dirpath, dirnames, filenames in os.walk(path):
        if '.git' in dirpath: continue
        if '.git' in dirnames: dirnames.remove('.git')
        filenames = [x for x in filenames if not x.startswith('.')]

        #print dirpath, dirnames, filenames    
        if not PY3:
            dirpath = dirpath.decode('utf-8')
            dirnames = [x.decode('utf-8') for x in dirnames]
            filenames = [x.decode('utf-8') for x in filenames]
        # 确定深度

        tmp_kv = {}
        tmp_dir = dirpath[len(path):].split('/') # /home/Memo/a/b -> [a,b]
        #print tmp_dir,'A'*10, dirnames
        if not k_v_dict: # 第一次空，进来
            k_v_dict={}.fromkeys(dirnames, {})
            k_v_dict.update({}.fromkeys(filenames))
            continue
        tmp_kv = k_v_dict
        #tmp_kv = copy_kv 
        for i, x in enumerate(tmp_dir):
            if (i+1)== len(tmp_dir):
                tmp_kv[x] = {}.fromkeys(dirnames)
                tmp_kv[x].update({}.fromkeys(filenames))       
                break
            tmp_kv = tmp_kv[x]    
            
    return k_v_dict


def to_bootstrap_tree(kv_tree):
    """ bootstrap_tree struct:
        var tree = [
      {
        text: "Parent 1",
        nodes: [
          {
            text: "Child 1",
            nodes: [
              {
                text: "Grandchild 1"
              },
              {
                text: "Grandchild 2"
              }
            ]
          },
          {
            text: "Child 2"
          }
        ]
      },
      {
        text: "Parent 2"
      },
      {
        text: "Parent 3"
      }
    ];
    """
    tree_list = []
    def trans(kv_dict, node):
        i = 0 # 控制加入数组的下标
        for k, v in sorted(kv_dict.items()):
            if not v:
                node.append({'text': k})
            else:
                node.append({'text': k, 'nodes': []})
                trans(v, node[i]['nodes'])
            i += 1
         
    trans(kv_tree, tree_list)
    return tree_list

TAG_FILE = './tags.conf'
def get_tags_conf(path):
    if os.path.exists(TAG_FILE):
        with open(TAG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            return json.load(f)
    else:
        return make_tags_config(path)

EVERY_LINE_NUMS = 5 # 每行显示标签的页数。
def get_tags_nums(path):
    conf = get_tags_conf(path)

    for tag, files_list in conf.items():
        conf[tag] = len(files_list)
    #print(conf.items())
    #s = OrderedDict(sorted(d.items(), key=lambda (k, v): v, reverse=True))
    sorted_conf = OrderedDict(sorted(conf.items(), key=lambda item: item[1], reverse=True))
    res_list = []
    tem_dict = OrderedDict()
    i = 0
    for x in sorted_conf:
        i = i+1
        tem_dict[x] = sorted_conf[x]
        if i % EVERY_LINE_NUMS == 0:
            res_list.append(copy.deepcopy(tem_dict))
            tem_dict = {}

    return res_list


def make_tags_config(path):
    """ 读取生成标签配置文件

    tags: [1,2,]

    {'Django': ['Django(一).md',
                'Django(三）.md',
                'Django在Ubuntu下的部署.md',
                'django部署企业微信应用.md',
                'Django（二）.md',
                'Framework.md'],
    'Docker': ['Cgroups.md',
                'Docker .md',
                'Dockerfile.md',
                'Namepace.md',
                'Union FS.md',
                '构造容器.md']
    }

    """
    all_tags = defaultdict(list)

    for dirpath, dirs, fns in os.walk(path):
        if '.git' in dirpath: continue

        fns = [x for x in fns if not x.startswith('.')]
        for fn in fns:
            if fn.startswith('.'): continue
            with open(dirpath + '/' + fn, 'r', encoding='utf-8') as f:
                print(222, fn)
                text = f.readline()
                if len(text)<7: print('4444', fn)
                text_match = re.search(r'\[.*\]', text)
                if text_match:
                    tags = text_match.group()[1:-1].split(',')
                    for tag in tags:
                        all_tags[tag.strip()].append(fn)
    with open(TAG_FILE, 'w') as f:
        #pprint(dict(all_tags))
        json.dump(dict(all_tags), f, indent=4)
    return all_tags


if __name__ == '__main__':
    pprint(get_tags_conf('../Memo/'))
    #d = k_v_tree('../Memo/')
    #pprint(d) 
    #pprint(to_bootstrap_tree(k_v_tree('/home/Memo/')))
