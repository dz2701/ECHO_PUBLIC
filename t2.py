#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
high_grade = 2019
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = # removed to protect privacy.
SAMPLE_RANGE_NAME = 'A1:AL999'
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId='', #removed
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])
df = pd.DataFrame(values)

from fetchclass import arr
#arr contains all the echo modules and semester, name and capacity

Fall, Winter, Spring = [], [], []
for i in range(len(arr)):
    if arr[i].semester == 'Fall': Fall.append(i)
    if arr[i].semester == 'Winter': Winter.append(i)
    if arr[i].semester == 'Spring': Spring.append(i)


class Student:
    def __init__(self,arr):
        self.Timestamp = arr[0]
        self.Email = arr[1]
        self.Last = arr[2]
        self.First = arr[3]
        self.PName = arr[4]
        self.Year = arr[5]
        self.FallS = arr[6]
        self.WinterS = arr[7]
        self.SpringS = arr[8]
        self.ECHO1P = arr[9]
        self.ECHO2P = arr[10]
        self.Backup = arr[11]
        self.Fall = [arr[12],arr[13],arr[14],arr[15],arr[16],arr[17],arr[18]]
        self.conf1 = arr[19]
        self.Winter = [arr[20],arr[21],arr[22],arr[23],arr[24],arr[25],arr[26]]
        self.conf2 = arr[27]
        self.Spring = [arr[28],arr[29],arr[30],arr[31],arr[32],arr[33],arr[34]]
        self.conf3 = arr[35]
        self.c1 = 'TBD'
        self.c2 = 'TBD'

def Check(cn):
    ind = -1
    for i in range(len(arr)):
        if cn == arr[i].name: ind = i
    if arr[ind].curcap < arr[ind].capacity: return True
    else: return False

def incind(cn):
    ind = -1
    for i in range(len(arr)):
        if cn == arr[i].name: ind = i
    arr[ind].curcap = arr[ind].curcap +1

new = df.to_numpy()
std = []
for i in range(len(new)):
    std.append(Student(new[i]))

#std index should be used from 1, 0 is index list

for i in range(1,len(std)):
    if std[i].ECHO1P == 'Fall':
        for j in range(7):
            if Check(std[i].Fall[j]):
                std[i].c1 = std[i].Fall[j]
                incind(std[i].Fall[j])
                break
    elif std[i].ECHO1P == 'Winter':
        for j in range(7):
            if Check(std[i].Winter[j]):
                std[i].c1 = std[i].Winter[j]
                incind(std[i].Winter[j])
                break
    elif std[i].ECHO1P == 'Spring':
        for j in range(7):
            if Check(std[i].Spring[j]):
                std[i].c1 = std[i].Spring[j]
                incind(std[i].Spring[j])
                break
    else: print("{} did not select their first ECHO.\n".format(i))



for i in range(1,len(std)):
    if std[i].ECHO2P == 'Fall':
        for j in range(7):
            if Check(std[i].Fall[j]):
                std[i].c2 = std[i].Fall[j]
                incind(std[i].Fall[j])
                break
    elif std[i].ECHO2P == 'Winter':
        for j in range(7):
            if Check(std[i].Winter[j]):
                std[i].c2 = std[i].Winter[j]
                incind(std[i].Winter[j])
                break
    elif std[i].ECHO2P == 'Spring':
        for j in range(7):
            if Check(std[i].Spring[j]):
                std[i].c2 = std[i].Spring[j]
                incind(std[i].Spring[j])
                break
    else: print("{} did not select their second ECHO.\n".format(i))
