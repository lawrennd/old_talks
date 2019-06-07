#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import os
import shutil
import time
import datetime

import ndlcgi
import ndlcal

base_expenses_dir = os.path.join("/home/neil/mlprojects", "expenses")

def account_entry():
    out = '''<td>&nbsp;Account Number:'''
    out += '''<select name="accountNumber", value=1>'''
    out += '''<Option value=1>AA000</option>'''
    out += '''<Option value=2>R01</option>'''
    out += '''<Option value=3>R201</option>'''
    out += '''<Option value=4>External</option>'''
    out += '''</select></td>'''
    return out

def category_entry():
    out = '''<td>&nbsp;Expense Category:'''
    out += '''<select name="accountNumber", value=1>'''
    out += '''<Option value=1>Travel</option>'''
    out += '''<Option value=2>Accommodation</option>'''
    out += '''<Option value=3>Subsistence</option>'''
    out += '''</select></td>'''
    return out

def reason_entry():
    out ='''<td>Reason Incurred <input type="text", name="reasonIncurred", value="", size=15></td>'''
    return out

def expense_box(form_name, app_details, submit_script):
    out = '<!-- Expense Box -->\n'
    out += '''<table><tr><td><form method="POST" action="./''' + submit_script + '''" onSubmit="return validateForm( this );" name="'''
    out += form_name
    out += '''">'''
    out += ndlcgi.form_date_entry(form_name, 'expenseTime', app_details['endTime'].day, 'endMonth', app_details['endTime'].month, 'endYear', app_details['endTime'].year)

    out += reason_entry()
    out += category_entry()
    out += account_entry()
    out +='''</form></td></tr></table>'''
    return out

