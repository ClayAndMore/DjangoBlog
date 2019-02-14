# coding:utf-8
import os,sys
from pprint import pprint
from os.path import basename

from collections import OrderedDict

PY3 = sys.version_info[0] == 3

def k_v_tree(path):
    """ 目录结构变成k-v
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


if __name__ == '__main__':
    #d = k_v_tree('/home/Memo/')
    #pprint(d) 
    pprint(to_bootstrap_tree(k_v_tree('/home/Memo/')))
