#!/usr/bin/env python

# Text utilities

import os
import sys
import re
import shutil
import time
import string
import glob
import datetime


def wrap_text(text, padding, width = 70, indent = 0, comment = '%'):
    """Takes a text string and wraps around with line breaks
    :param text: text to be wrapped
    :param padding: 
    :param width: (default 70)
    :param indent: (default 0)
    :param comment: (default %)"""
    
    text = ' ' + text
    pos_list = [0]
    out_text = ''
    end_point = width
    while end_point<len(text):
        pos = text[0:end_point].rfind(' ')
        pos_list.append(pos)
        end_point = pos + width
    pad_str = padding
    for pos_no in range(len(pos_list)-1):
        out_text+= comment + pad_str + text[pos_list[pos_no]+1:pos_list[pos_no+1]] + '\n'
        if indent>0:
            pad_str = padding
            for num in range(indent):
                pad_str += ' '    
    out_text += comment + pad_str + text[pos_list[-1]+1:-1] + '\n'
        
    return out_text


