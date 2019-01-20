#!/usr/bin/env python

import os
import glob
import stat
import Image


def create_dir_thumbnails(picture_dir, thumb_dir, size = (128,128) ):
    """Create a directory of thumbnails from a picture directory
    :param picture_dir: the directory containing pictures.
    :param thumb_dir: the directory to contain thumbnails.
    :param size: the size of thumbnail (default (128, 128)).
    """
    file_list = glob.glob(os.path.join(picture_dir, '*.jpg'))
    file_list = file_list + glob.glob(os.path.join(picture_dir, '*.JPG'))
    for file in file_list:
        st = os.stat(file)
        mode = st[stat.ST_MODE]
        if mode & stat.S_IWRITE: # file is readable
            if os.path.islink(file): # if it is a link, read the linked to file.
                file = os.readlink(file)
            base_name = os.path.basename(file)
            if not os.path.exists(thumb_dir):
                os.makedirs(thumb_dir)
        
            thumb_name = os.path.join(thumb_dir, base_name)
            if not os.path.exists(thumb_name):
                im = Image.open(picture_dir + '/' + base_name)
                try:
                    im.thumbnail(size, Image.ANTIALIAS)
                except i_o_error:
                    raise i_o_error("Unexpected error for file " + base_name)
                
                im.save(thumb_name, "JPEG")


def get_thumbnail( filename, size = (128,128) ):
    """Get a thumbnail image of filename
    :param filename: the filename to get the thumbnail image of
    :param size: the size of the thumbnail (default (128, 128))
    """
    
    im = Image.open(filename)
    im.thumbnail(size, Image.ANTIALIAS)
    newim = Image.new('RGB', size)
    x,y = im.size
    newim.paste(im, ((size[0]-x)/2, (size[1]-y)/2))
    return newim


