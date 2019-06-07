
#!/usr/bin/env python

# HTML utilities

import os
import sys
import re
import shutil
import time
import string
import glob
import datetime
import httplib

def get_reference(key_name):
    request_u_r_l = 'ml.sheffield.ac.uk'
    request_string = '/~neil/cgi-bin/publications/bibpage.cgi?keyName=' + key_name + '&header=0&printAbstract=1'
    print "Getting publication " + key_name 
    print "Using " + request_u_r_l + request_string
    h = httplib.h_t_t_p(request_u_r_l)
    h.putrequest('GET', request_string)
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    if errcode == 200:
        print "... succesful."
    else:
        print "Error " + str(errcode) + ", " + errmsg
    f = h.getfile()
    lines = f.read()
    f.close()
    return lines
    
def write_to_file(file, string, style = '', title='', header='', footer='', navigation=''):
    header = '<html>\n' + header
    if len(title)>0:
        header += "<head>\n  <title>" + title + "</title>\n</head>\n"
    header += "<body>\n\n"
    header += navigation
    header += '<section id="content" class="three-col">\n<div id="inner">'
    string = header + string 
    string += "<p>This document last modified <!--#flastmod file=\"" + file + "\" --></p>"
    string += "\n</div>\n</section>"
    if len(footer)>0:
        string += footer
    string += "\n</html>"
    file_handle = open(file, 'w')
    file_handle.write(string)
    file_handle.close()


