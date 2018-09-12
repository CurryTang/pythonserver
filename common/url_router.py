#!/usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from importlib import import_module


def include(module):
    mod = import_module(module)
    urls = getattr(mod, 'urls', mod)
    return urls


def url_wrapper(urls):
    wrapper_list = []
    for url in urls:
        ## path是第一级的域名，handles是对应的处理类
        path, handles = url
        # 返回的handle第二项是一个list
        if isinstance(handles, (tuple, list)):
            for handle in handles:
                pattern, handle_class = handle
                wrap = ('{0}{1}'.format(path, pattern),
                        handle_class)
                wrapper_list.append(wrap)
        else:
            wrapper_list.append((path, handles))
    return wrapper_list

