#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import glob
import time
import stat

def pami_links():
    return '''<ul>
    <li><a href="https://mc.manuscriptcentral.com/tpami-cs">PAMI Manuscript Central</a></li>
    <li><a href="http://jmlr.csail.mit.edu/manudb/center/manulist?action">JMLR Editing</a></li>
    <li></li>
    </ul>'''
def search_box():
    return '''<table><tr><td><form method="get" action="http://www.google.com/search">

<input type="text"   name="q" size="31"
 maxlength="255" value="" />
<input type="submit" value="Google Search" /></td>
<tr>
<td>
<input type="radio"  name="sitesearch" value="" />
 The Web
<input type="radio"  name="sitesearch"
 value="cs.man.ac.uk" checked /> Manchester Computer Science<br />
</td>
</tr>
</table>
</form>'''

def useful_local_links():
    return '''<ul>
    <li><a href="http://intranet.cs.man.ac.uk/ACSO/rooms/">Room Bookings</a></li>
    <li><a href="http://www.cs.man.ac.uk/~jls/rota.html">MLO Lunch Meetings</a></li>
    <li><a href="../seminars/seminars.cgi">Machine Learning Seminars</a></li>
    <li><a href="http://intranet.cs.man.ac.uk/Events_subweb/admin/">Workshop Registration List</a></li>
    </ul>'''

def google_scholar_box():
    return '''<!-- Google Scholar -->
    <form method="get" action="http://scholar.google.com/scholar">
      <table bgcolor="#FFFFFF">
        <tr>
          <td>
          <a href="http://scholar.google.com/"> <img src="http://scholar.google.com/scholar/scholar_sm.gif" alt="Google Scholar" width="105" height="40" border="0" align="absmiddle" /></a>
          <input type="hidden" name="hl" value="en">
          <input type="text" name="q" size="25" maxlength="255" value="" />
          <input type="submit" name="btnG" value="Search" />
          </td>
        </tr>
      </table>
    </form>
    <!-- Google Scholar --> '''

def js_import_script():
    return '<script src="../../lib/formLib.js"></script>'

def js_validate_form(form_name, required_texts, required_selects):
    out = '''<script><!--
    function validateForm ( form ) {
    requiredText = new Array('''
    while(len(required_texts)>1):
        out += '"' + required_texts.pop() + '"' + ', '
    if(len(required_texts)):
        out += '"' + required_texts.pop() + '"'
    out += ''');
    requiredSelect = new Array('''
    while(len(required_selects)>1):
        out += '"' + required_selects.pop() + '"' + ', '
    if(len(required_texts)):
        out += '"' + required_selects.pop() + '"'
    out += ''');
          return requireValues ('''
    out += form_name
    out += ''', requiredText   ) &&
    requireSelects ( '''
    out += form_name +''', requiredSelect  ) &&
                 checkProblems (  );
    }
    // -->
    </script>'''
    return out


def form_date_entry(form_name, day_field, day_val, month_field, month_val, year_field, year_val):
    out = '''<td><b>Day</b></td>
    <td><select name="''' + day_field + '''" value=''' + str(day_val) + '''></select></td>
    <td><b>Month</b></td>
    <td><select name="''' + month_field + '''" value=''' + str(month_val) + '''
    onChange="dateFormChangeMonth(''' + form_name + ''', ''' + day_field + ''', ''' + month_field + ''', ''' + year_field + ''')">
    <Option value=1>January</Option>
    <Option value=2>February</Option>
    <Option value=3>March</Option>
    <Option value=4>April</Option>
    <Option value=5>May</Option>
    <Option value=6>June</Option>
    <Option value=7>July</Option>
    <Option value=8>August</Option>
    <Option value=9>September</Option>
    <Option value=10>October</Option>
    <Option value=11>November</Option>
    <Option value=12>December</Option>
    </select></td>
    <td><b>Year</b></td>
    <td><select name="''' + year_field + '''" ''' + '''value=''' + str(year_val) + '''></select></td>'''
    return out



def form_input(form_name, type, name, value, size, hidden=0):
    if hidden:
        return '<input type="hidden" name="' + name + '" value="' + value + '">'
    else:
        return '<input type="' + type + '" name="' + name + '" value="' + value + '"size="' + str(size) + '">'


def form_text_area(form_name, name, value, rows, cols, hidden=0):
    if hidden:
        return '<input type="hidden" name="' + name + '" value="' + value + '">'
    else:
        return '<textarea name="' + name + '" rows="' + str(rows) + ' cols="' + str(cols) + '">' + value + '</textarea>'


def month_name(number):
    months={
        '01':'January',
        '02':'February',
        '03':'March',
        '04':'April',
        '05':'May',
        '06':'June',
        '07':'July',
        '08':'August',
        '09':'September',
        '10':'October',
        '11':'November',
        '12':'December'
        }
    return months[number]

def read_txt_file(file):
    str_ret = ''
    if os.path.exists(file):
        file_handle = open(file, 'r');
        file_lines = file_handle.readlines()
        file_handle.close()
        for line in file_lines:
            str_ret += line
    return str_ret

def read_txt_lines_file(file):
    str_ret = ''
    if os.path.exists(file):
        file_handle = open(file, 'r');
        file_lines = file_handle.readlines()
        file_handle.close()
        for line in file_lines:
            str_ret += line
    return str_ret

def read_txt_lines_file_break(file):
    str_ret = ''
    if os.path.exists(file):
        file_handle = open(file, 'r');
        file_lines = file_handle.readlines()
        file_handle.close()
        for line in file_lines:
            str_ret += line + '<br>'
    return str_ret

def extract_file_details(file, seperator=","):

    details = []
    if os.path.exists(file):
        file_handle = open(file, 'r');
        file_lines = file_handle.readlines()
        file_handle.close()
        for line in file_lines:
            if line[0]=='#':
                continue
            else:
                details.append(string.splitfields(line, seperator))
    else:
        sys.exit(0)

    for i in range(len(details)):
        for j in range(len(details[i])):
            details[i][j] = details[i][j].strip()

    return details


def write_to_screen(string, style = '', title='', header='', footer='', time=''):
    if len(string)>0:
	if len(title)>0:
       	    string = "<head><title>" + title + "</title></head>\n" + string
	if len(header)>0:
            string = header + string
	if len(style)>0:
            string = style + string
	if len(time)>0:
            string += "<p align=\"center\">Page generated on " + time + ", maintained by Neil D. Lawrence" + "</p>"
	if len(footer)>0:
            string += footer
	       print "Content-type: text/html\n"
	       sys.stdout.write(string)


def get_reference(key_name):
    h = httplib.h_t_t_p('www.cs.man.ac.uk')
    print "Getting publication " + key_name + ".\n"
    h.putrequest('GET', '/neill-bin/publications/bibpage.cgi?keyName=' + key_name + '&header=0&printAbstract=1')
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    if errcode == 200:
        print "... succesful."
    else:
        print "Error " + errcode + ", " + errmsg
    f = h.getfile()
    lines = f.read()
    f.close()
    return lines
    
def read_txt_file(file):
    str_ret = ''
    if os.path.exists(file):
        file_handle = open(file, 'r');
        file_lines = file_handle.readlines()
        file_handle.close()
        for line in file_lines:
            str_ret += line
    return str_ret
    
def extract_file_details(file, seperator=","):
    details = []
    if os.path.exists(file):
        file_handle = open(file, 'r');
        file_lines = file_handle.readlines()
        file_handle.close()
        for line in file_lines:
            if line[0]=='#':
                continue
            else:
                details.append(string.splitfields(line, seperator))
    else:
        sys.exit(0)

    for i in range(len(details)):
        for j in range(len(details[i])):
            details[i][j] = details[i][j].strip()

    return details


def write_to_file(file, string, style = '', title='', header='', footer='', time=''):
    if len(string)>0:
	if len(title)>0:
       	    string = "<head><title>" + title + "</title></head>\n" + string
	if len(header)>0:
            string = header + string
	if len(style)>0:
            string = style + string
	if len(time)>0:
            string += "<p align=\"center\">Page last updated on " + time + " by Neil D. Lawrence" + "</p>"
	if len(footer)>0:
            string += footer
	       file_handle = open(file, 'w')
	       file_handle.write(string)
	       file_handle.close()


def novel_file_name(base_name, directory):

    file_name = os.path.join(directory, base_name)
    counter = 0
    while os.path.exists(file_name):
        counter = counter + 1
        parts = os.path.splitext(base_name)
        base_name = parts[0] + '_' + str(counter) + parts[1]
        file_name = os.path.join(directory, base_name)
    return base_name


