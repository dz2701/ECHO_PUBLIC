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
SAMPLE_SPREADSHEET_ID = # removed due to security/privacy issues!
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
result = sheet.values().get(spreadsheetId='',
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])


class Course:
    def __init__(self,name,semester,capacity):
        self.name = name
        self.semester = semester
        self.capacity = capacity
        self.curcap = 0
arr = []
for i in range(1,len(values)-1):
    arr.append(Course(values[i][3],values[i][12],values[i][13]))


#arr contains all the ECHO classes with its capacity and semester.
