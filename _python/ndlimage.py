#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import glob
import time
import stat
import image


def create_dir_thumbnails(picture_dir, thumb_dir, size = (128,128) ):
    file_list = glob.glob(os.path.join(picture_dir, '*.jpg'))
    file_list = file_list + glob.glob(os.path.join(picture_dir, '*.JPG'))
    for file in file_list:
        st = os.stat(file)
        mode = st[stat.s_t__m_o_d_e]
        if mode & stat.s__i_w_r_i_t_e: # file is readable
            if os.path.islink(file): # if it is a link, read the linked to file.
                file = os.readlink(file)
            base_name = os.path.basename(file)
            if not os.path.exists(thumb_dir):
                os.makedirs(thumb_dir)
        
            thumb_name = os.path.join(thumb_dir, base_name)
            if not os.path.exists(thumb_name):
                im = image.open(picture_dir + '/' + base_name)
                try:
                    im.thumbnail(size, image.a_n_t_i_a_l_i_a_s)
                except i_o_error:
                    raise i_o_error("Unexpected error for file " + base_name)
                
                im.save(thumb_name, "JPEG")


def get_thumbnail( filename, size = (128,128) ):
    '''Get a thumbnail image of filename'''
    
    im = image.open(filename)
    im.thumbnail(size, image.a_n_t_i_a_l_i_a_s)
    newim = image.new('RGB', size)
    x,y = im.size
    newim.paste(im, ((size[0]-x)/2, (size[1]-y)/2))
    return newim


