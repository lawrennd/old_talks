#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import os
import shutil
import time
import datetime
sys.path.append('..')
import ndlcgi
import ndlcal

def print_todo(base_name, todo_details):
    string = '<li><a href="../today/todo.cgi?file=' + base_name + '">' + todo_details['title'] + '</a> by ' + todo_details['endTime'].strftime('%A, %d %b') + ' [<a href="../today/editTodo.cgi?file=' + base_name + '">edit</a>]' + ' [<a href="../today/doneTodo.cgi?file=' + base_name + '">done</a>][<a href="../today/today.cgi?today=' + todo_details['endTime'].strftime('%Y_%m_%d') + '">today</a>]</li>'
    return string


def print_appointment(base_name, appoint_dir, app_details):
  string = ''
  if app_details['type'] == ndlcal.app_num['Diary']:
    string += '<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + '</a>'
  elif app_details['type'] == ndlcal.app_num['Conference']:
    string += 'Conference:\t<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + ' (finishes ' + app_details['endTime'].strftime('%A, %d') + ')</a>'
  elif app_details['type'] == ndlcal.app_num['Deadline']:
    string += 'Deadline:\t<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + '</a>'
  elif app_details['type'] == ndlcal.app_num['Holiday']:
    string += 'Holiday:\t<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + '</a>'
  elif app_details['type'] == ndlcal.app_num['Visit']:
    string += 'Visit:\t<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + ' (finishes ' + app_details['endTime'].strftime('%A, %d') + ')</a>'
  elif app_details['type'] == ndlcal.app_num['Visitor']:
    string += 'Visitor:\t<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + ' (finishes ' + app_details['endTime'].strftime('%A, %d') + ')</a>'
  elif int(app_details['length']) < 24:
    if int(app_details['length']) == 0:
      string += app_details['startTime'].strftime('%H:%M') + '\t<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + '</a>'

    else:
      string += app_details['startTime'].strftime('%H:%M') + '-' + app_details['endTime'].strftime('%H:%M') + '\t<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + '</a>'
  elif int(app_details['length']) == 24:
    string += '<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + '</a>'
  else:
    string += '<a href="../calendar/appointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '">' + app_details['title'] + ' (finishes ' + app_details['endTime'].strftime('%A, %d') + ')</a>'
  string += '&nbsp;[<a href="../calendar/editAppointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '&return=../today/today.cgi">edit</a>]'
  string += ' [<a href="../calendar/doneAppointment.cgi?file=' + base_name + '&dir=' + appoint_dir + '&return=../today/today.cgi">done</a>]'
  string += ' [<a href="../today/today.cgi?today=' + app_details['startTime'].strftime('%Y_%m_%d') + '">today</a>]'
  string += '<br>'
  return string

def js_prepare_form(form_name, app_details):
  out = '''<script><!--
  function loadCalEditor() 
  {
    dateFormPopulate(''' + form_name + ''', ''' + form_name + '''.startDay, ''' + str(app_details['startTime'].day) + ''', ''' + form_name + '''.startMonth, ''' + str(app_details['startTime'].month) + ''', ''' + form_name + '''.startYear, ''' + str(app_details['startTime'].year) + ''');
    dateFormPopulate(''' + form_name + ''', ''' + form_name + '''.endDay, ''' + str(app_details['endTime'].day) + ''', ''' + form_name + '''.endMonth, ''' + str(app_details['endTime'].month) + ''', ''' + form_name + '''.endYear, ''' + str(app_details['endTime'].year) + ''');
    selectFormSet(''' + form_name + ''', ''' + form_name + '''.type, ''' + str(app_details['type']) + ''');
  }
  // -->
  </script>'''
  return out

def print_form_html(form_name, app_details, dir_to_show, requested_file, submit_script):
  
  out = '''<form method="POST" action="./''' + submit_script + '''" onSubmit="return validateForm( this );" name="'''
  out += form_name
  out += '''">

  <blockquote>
  <table>
  <tr>'''
  out += ndlcgi.form_date_entry(form_name, 'startDay', app_details['startTime'].day, 'startMonth', app_details['startTime'].month, 'startYear', app_details['startTime'].year)
  out += '''<td><b>Time</b>*</td>
  <td>'''
  out += ndlcgi.form_input(form_name, 'text', 'startHour', app_details['startTime'].strftime('%H'), 10)
  out += ndlcgi.form_input(form_name, 'text', 'startMin', app_details['startTime'].strftime('%M'), 10)
  out += '''</td>
  </tr>'''
  out += ndlcgi.form_date_entry(form_name, 'endDay', app_details['endTime'].day, 'endMonth', app_details['endTime'].month, 'endYear', app_details['endTime'].year)
  out += '''<td><b>Time</b>*</td>
  <td>'''
  out += ndlcgi.form_input(form_name, 'text', 'endHour', app_details['endTime'].strftime('%H'), 10)
  out += ndlcgi.form_input(form_name, 'text', 'endMin', app_details['endTime'].strftime('%M'), 10)
  out += '''</td>
  </tr>
  </table>
  <table>
  <tr>
  <td align = "left"><b>Title</b>*</td>
  <td>'''
  out += ndlcgi.form_input(form_name, 'text', 'title', app_details['title'], 20)
  out += '''</td>
  <td align = "left"><b>Type</b>*</td>
  <td><select name="type" size="1"'''
  out += ' value=' + str(app_details['type']) + '>'
  out += '''              '''
  keys = ndlcal.app_num.keys()
  keys.sort()
  for key in keys:
    out += '<option value=' + str(ndlcal.app_num[key]) + '>' + key + '</option>\n'

  out +='''</select>
  </td>
  </tr>
  <tr>
  <td align = "left"><b>Venue</b>*</td>
  <td>'''
  out += ndlcgi.form_input(form_name, 'text', 'venue', app_details['venue'], 20)
  out += '''</td>'''
  out += '''<td align="left"><b>Length</b>*</td>
  <td>'''
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Speaker</b>*</td>
  <td>'''
  out += ndlcgi.form_input(form_name, 'text', 'speaker', app_details['speaker'], 20)
  out += '''</td>
  </tr>
  <tr>
  <td align="left"><b>Length</b>*</td>
  <td>'''
  out += ndlcgi.form_input(form_name, 'text', 'length', app_details['length'], 20)
  out += '''</td>
  </tr>
  </table>
  <table width=80%>
  <tr>
  <td align = "left"><b>Notes File</b>*</td>
  <td>'''
  out += ndlcgi.form_input(form_name, 'text', 'notesFile', app_details['notesFile'], 20, 1)
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Notes</b>*</td>
  <td colspan="6">'''
  out += ndlcgi.form_text_area(form_name, 'notes', app_details['notes'], 5, 40, 1)
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Notes File</b>*</td>
  <td>'''
  out += ndlcgi.form_input(form_name, 'text', 'notesHtmlFile', app_details['notesHtmlFile'], 20)
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Notes</b>*</td>
  <td colspan="6">'''
  out += ndlcgi.form_text_area(form_name, 'notesHtml', app_details['notesHtml'], 5, 40)
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Extra</b>*</td>
  <td colspan="6">'''
  out += ndlcgi.form_text_area(form_name, 'extra', app_details['extra'], 5, 40, 1)
  out += '''</td>
  </tr>'''
  #<tr>
  #<td align = "left"><b>E-mail</b>*</td>
  #<td colspan="3">
  #<input type=text name="email" onchange="checkEmail( this );" SIZE=25>
  #</td>
  #</tr>
  out += '''</table>
  * Indicates required field.
  </blockquote>
  <input type=submit value="Submit Form">
  <input type=reset value="Reset Form">'''
  if requested_file:
    out += '''<input type="hidden" name="origFileName" value="''' + os.path.join(dir_to_show, requested_file) + '''">'''    
    out += '''<input type="hidden" name="origNotesFile" value="''' + os.path.join(dir_to_show, 'notes', app_details['notesFile']) + '''">'''    
    out += '''<input type="hidden" name="origNotesHtmlFile" value="''' + os.path.join(dir_to_show, 'notesHtml', app_details['notesHtmlFile']) + '''">'''    
  else:
    out += '''<input type="hidden" name="origFileName" value="">'''
    out += '''<input type="hidden" name="origNotesFile" value="">'''    
    out += '''<input type="hidden" name="origNotesHtmlFile" value="">'''    
  out += '''<input type="hidden" name="user" value="''' + os.environ['REMOTE_USER'] + '''">'''
  out += '''</form>'''
  return out

def read_form_keys(form):

  field_dict = {}
  for key in form.keys():
    field_dict[key] = form[key];

  start_min = int(field_dict['startMin'].value)
  del field_dict['startMin']
  start_hour = int(field_dict['startHour'].value)
  del field_dict['startHour']
  start_day = int(field_dict['startDay'].value)
  del field_dict['startDay']
  start_month = int(field_dict['startMonth'].value)
  del field_dict['startMonth']
  start_year = int(field_dict['startYear'].value)
  del field_dict['startYear']
  end_min = int(field_dict['endMin'].value)
  del field_dict['endMin']
  end_hour = int(field_dict['endHour'].value)
  del field_dict['endHour']
  end_day = int(field_dict['endDay'].value)
  del field_dict['endDay']
  end_month = int(field_dict['endMonth'].value)
  del field_dict['endMonth']
  end_year = int(field_dict['endYear'].value)
  del field_dict['endYear']
  if field_dict['notesFile'].value == 'None':
    field_dict['notesText'] = ''
  else:
    field_dict['notesText'] = field_dict['notes'].value
  if field_dict.has_key('notes'):
    del field_dict['notes']
  if field_dict['notesHtmlFile'].value == 'None':
    field_dict['notesHtmlText'] = ''
  else:
    field_dict['notesHtmlText'] = field_dict['notesHtml'].value
  if field_dict.has_key('notesHtml'):
    del field_dict['notesHtml']

  if not field_dict.has_key('origFileName'):
    field_dict['origFileName'] =  ''
  if not field_dict.has_key('origNotesFile'):
    field_dict['origNotesFile'] = ''
  app_type = 'Appointment'
  if field_dict.has_key('type'):
    app_type = ndlcal.reverse_app(int(field_dict['type'].value))
  field_dict['type'].value = app_type

  if not field_dict.has_key('origNotesHtmlFile'):
    field_dict['origNotesHtmlFile'] = ''

  field_dict['startTime'] = datetime.datetime(start_year, start_month, start_day, start_hour, start_min)
  field_dict['endTime'] = datetime.datetime(end_year, end_month, end_day, end_hour, end_min)
  length_tuple = field_dict['endTime'] - field_dict['startTime']
  length = length_tuple.days*24 + length_tuple.seconds/(60*60)
  field_dict['length'].value = length
  return field_dict

def move_orig_files(field_dict):
  # Check whether original file exists ... move if it does.
  if field_dict['origFileName']:
    if os.path.exists(field_dict['origFileName'].value):
      shutil.move(field_dict['origFileName'].value, field_dict['origFileName'].value + '~')
  if field_dict['origNotesFile']:
    if os.path.exists(field_dict['origNotesFile'].value):
      shutil.move(field_dict['origNotesFile'].value, field_dict['origNotesFile'].value + '~')
  if field_dict['origNotesHtmlFile']:
    if os.path.exists(field_dict['origNotesHtmlFile'].value):
      shutil.move(field_dict['origNotesHtmlFile'].value, field_dict['origNotesHtmlFile'].value + '~')

  del field_dict['origFileName']
  del field_dict['origNotesFile']
  del field_dict['origNotesHtmlFile']
  return field_dict

def write_notes(field_dict, notes_path):
  if not field_dict['notesFile'].value == 'None':
    write_path = os.path.join(notes_path, 'notes')
    if not os.path.exists(write_path):
      os.mkdir(write_path)
    field_dict['notesFile'].value = ndlcgi.novel_file_name(field_dict['notesFile'].value, write_path)
    file_name = os.path.join(write_path, field_dict['notesHtmlFile'].value)
    f = open(file_name, 'w')
    f.write(field_dict['notesText'])
    f.close()
  del field_dict['notesText']

  if not field_dict['notesHtmlFile'].value == 'None':
    write_path = os.path.join(notes_path, 'notesHtml')
    if not os.path.exists(write_path):
      os.mkdir(write_path)
    field_dict['notesHtmlFile'].value = ndlcgi.novel_file_name(field_dict['notesHtmlFile'].value, write_path)
    file_name = os.path.join(write_path, field_dict['notesHtmlFile'].value)
    f = open(file_name, 'w')
    f.write(field_dict['notesHtmlText'])
    f.close()
  del field_dict['notesHtmlText']
  return field_dict

def write_appointment(field_dict, file_name):
  del field_dict['startTime']
  del field_dict['endTime']

  time_stamp = time.strftime('%A %d %b %Y at %H:%M')
  file_out = '# Created at ' + time_stamp + '\n'

  keys = field_dict.keys()
  keys.sort()
  for key in keys:
    file_out += key + '|' + str(field_dict[key].value) + '\n'

  # Write to file
  f = open(file_name, 'w')
  f.write(file_out)
  f.close()

def return_today():
  url = '''../today/today.cgi'''
  string = '''<div class="section"><META HTTP-EQUIV="Refresh" CONTENT="0; URL=''' + url + '''">'''
  #string = message
  string += '''<a href="''' + url + '''">Click here if not forwarded</a></div>'''
  #todayHeader.txt contains the pages' headers
  today_header = ndlcgi.read_txt_file('./today/todayHeader.txt')
  #todayFooter.txt contains the pages' footers
  today_footer = ndlcgi.read_txt_file('./today/todayFooter.txt')
  #todayStyle.txt contains the pages' style
  today_style = ndlcgi.read_txt_file('./today/todayStyle.txt')
  time_stamp = time.strftime('%A %d %b %Y at %H:%M')

  ndlcgi.write_to_screen(string, today_style, 'Edit Succesful', today_header, today_footer, time_stamp)

