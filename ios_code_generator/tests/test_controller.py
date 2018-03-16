# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from StringIO import StringIO

import sys

__author__ = 'banxi'
from ios_code_generator.generators import generate_v2

def test_controller():
    strio = StringIO(u'''
    DiscoverViewController(m=DiscoverItem,req,adapter=c,page,init_views=false,search_ui,right_button=完成):vc
    slide[t0,hor0,h180]
    _[hor0,t0,b0]:c
    ''')
    sys.stdin = strio
    output = generate_v2("controller")
    print(output)

def test_sadapter():
    strio = StringIO(u'''
    DiscoverViewController(sadapter):tvc
    name:ltc
    area:rdc
    ''')
    sys.stdin = strio
    output = generate_v2("controller")
    print(output)