#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import os
import time
import datetime
sys.path.append('..')
import ndlcgi


base_appointment_dir = os.path.join("/home/neil/mlprojects", "appointments")
base_todo_dir = os.path.join("/home/neil/mlprojects", "todo")
base_seminar_dir = os.path.join("/home/neil/mlprojects", "seminars")
app_num = {'Appointment':1,
          'Conference':2,
          'Deadline':3,
          'Dentist':4,
          'Diary':5,
          'Holiday':6,
          'Flight':7,
          'Talk':8,
          'Todo':9,
          'Visit':10,
          'Visitor':11}


def print_additional_keys(app_details):
  del app_details['notesFile']
  del app_details['notesHtmlFile']
  del app_details['startTime']
  del app_details['endTime']
  del app_details['length']
  del app_details['title']
  del app_details['venue']
  del app_details['type']
  del app_details['speaker']
  del app_details['user']
  del app_details['done']
  string = ''
  keys = app_details.keys()
  keys.sort()
  for key in keys:
    if app_details[key]:
      string += '<br>' + key + ': ' + str(app_details[key])
  string += app_details['extra']
  return string

def appointment_details(requested_file, dir_to_show):
  file_to_show = os.path.join(dir_to_show, requested_file)
  details = ndlcgi.extract_file_details(file_to_show, '|')
  app_details = {}
  app_details['affiliation'] = ''
  app_details['webpage'] = ''
  app_details['user'] = ''
  app_details['extra'] = ''
  app_details['title'] = ''
  app_details['venue'] = ''
  app_details['speaker'] = ''
  app_details['type'] = 'Appointment'
  app_details['length'] = ''
  app_details['slides'] = ''
  app_details['notes'] = ''
  app_details['notesFile'] = 'None'
  app_details['notesHtml'] = ''
  app_details['notesHtmlFile'] = 'None'
  app_details['done'] = 0
  for detail in details:
    if detail[0] == "notesFile" or detail[0] == "notes":
      app_details['notesFile'] = detail[1]
      app_details['notes'] += ndlcgi.read_txt_lines_file(os.path.join(dir_to_show, 'notes', app_details['notesFile']))
    elif detail[0] == "notesHtmlFile":
      app_details['notesHtmlFile'] = detail[1]
      app_details['notesHtml'] += ndlcgi.read_txt_lines_file(os.path.join(dir_to_show, 'notesHtml', app_details['notesHtmlFile']))
    elif detail[0] == "type":
      app_details['type'] = app_num[detail[1]]
    else:
      app_details[detail[0]] = detail[1]

  appointment_length = datetime.timedelta(float(app_details['length'])/24)
  base_file = os.path.splitext(requested_file)
  file_parts = base_file[0].split('_')
  date_time_string = file_parts[0] + '_' + file_parts[1] + '_' + file_parts[2] + '_' + file_parts[3]
  start_time_tuple = time.strptime(date_time_string, '%Y_%m_%d_%H%M')
  app_details['startTime'] = datetime.datetime(start_time_tuple[0], start_time_tuple[1], start_time_tuple[2], start_time_tuple[3], start_time_tuple[4])
  app_details['endTime'] = app_details['startTime'] + appointment_length
  app_details['ordinalEnd'] = app_details['endTime'].toordinal()
  return app_details

def reverse_app(number):
  for key in app_num.keys():
    if int(number) == app_num[key]:
      app_type = key
      break
  return app_type


