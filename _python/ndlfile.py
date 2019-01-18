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
import subprocess

def get_cvs_version(file_name, full_path):
    # extract CVS version.
    base_dir = os.path.dirname(full_path)
    cvs_file_name = os.path.join(base_dir, 'CVS', 'Entries')    
    cvs_ver=''
    if os.path.exists(cvs_file_name):
        file = open(cvs_file_name, 'r')
        cvs_lines = file.readlines()
        for line in cvs_lines:
            split_vals = line.split('/')        
            if len(split_vals)>2 and split_vals[1]==file_name:
                cvs_ver = split_vals[2] 
    return cvs_ver

def get_svn_version(file_name, full_path):
    # extract SVN version.
    base_dir = os.path.dirname(full_path)
    svn_file_name = os.path.join(base_dir, '.svn', 'entries')
    
    file_lines = []
    svn_ver ={}
    in_file = 0
    counter = 11
    if os.path.exists(svn_file_name):
        file = open(svn_file_name, 'r')
        svn_lines = file.readlines()
        for line in svn_lines:
            if re.findall(re.compile(r'^' + file_name), line):
                in_file = 1
            if in_file:
                file_lines.append(line)
                counter = counter - 1
                if counter == 0:
                    break
    if in_file:
        svn_ver['type'] = file_lines[1][0:-1]            
        svn_ver['textLastUpdate'] = file_lines[6][0:-1]            
        svn_ver['checkSum'] = file_lines[7][0:-1]            
        svn_ver['lastChange'] = file_lines[8][0:-1]            
        svn_ver['version'] = file_lines[9][0:-1]            
        svn_ver['userName'] = file_lines[10][0:-1]
    else:
        svn_ver = []
    return svn_ver

def get_git_version(file_name, full_path, git_path):
    # extract GIT version.
    base_dir = os.path.dirname(full_path)
    git_file_name = os.path.join(base_dir, file_name)
    
    file_lines = []
    svn_ver = {}
    in_file = 0
    counter = 11
    if os.path.exists(git_file_name):
        out_repo = subprocess.call(["git", "--git-dir", os.path.join(git_path,'.git'), '--work-tree', base_dir, "ls-files", file_name, "--error-unmatch"])
        print out_repo
        if out_repo != 1:
            output = subprocess.check_output(["git", "--git-dir", os.path.join(git_path,'.git'), '--work-tree', base_dir, "ls-files", file_name, "--error-unmatch"])
            print output
            git_ver = 0.1
        else:
            git_ver = []
    return git_ver

def read_txt_file(file, dir_name="."):
    file = os.path.join(dir_name, file)
    str_ret = ''
    if os.path.exists(file):
        file_handle = open(file, 'r');
        file_lines = file_handle.readlines()
        file_handle.close()
        for line in file_lines:
            if line[0]=='#':
                continue
            else:
                str_ret += line
    return str_ret

def extract_file_details(file, seperator=",", dir_name="."):

    details = []
    file = os.path.join(dir_name, file);
    if os.path.exists(file):
        file_handle = open(file, 'r');
        file_lines = file_handle.readlines()
        file_handle.close()
        for line in file_lines:
            if line[0]=='#':
                continue
            elif line[0]=='\n':
                continue
            else:
                details.append(string.splitfields(line, seperator))
    else:
        sys.exit(0)

    for i in range(len(details)):
        for j in range(len(details[i])):
            details[i][j] = details[i][j].strip()

    return details



