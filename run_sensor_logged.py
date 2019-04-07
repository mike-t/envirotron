#!/usr/bin/python
# Copyright 2019 Mike Walton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# NOTE!: to get the google pickle token use the returned uri in another temrinal and wget (this script willrun local webserver if needed) 

# imports 
from __future__ import print_function
import pickle
import os.path
import Adafruit_DHT
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying the scope, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
CREDENTIALS_FILE = '/home/pi/pi-sensor-temperature/google_credentials.json'
SHEET_ID = '1Kqox-0vK86VwS_UvGU0r72tfFbXQoNScXlbH_NKVOFU'
SHEET_RANGE = 'Data!A2:C'
TOKEN_PICKLE = '/home/pi/pi-sensor-temperature/token.pickle'

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
SENSOR = Adafruit_DHT.DHT22

# Set the Raspberry Pi GPIO pin atttached to sensor
IOPIN = 4

## Main function
def main():

    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, IOPIN)

    # grab the timestamp of reading
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

    # try and get a reading from the sensor
    if humidity is not None and temperature is not None:
        print('Temp: {0:0.1f}*C  Humidity: {1:0.1f}% Time: {2}'.format(temperature, humidity, timestamp))

        # Authenticate to Google and add the new row
        creds = None
        if os.path.exists(TOKEN_PICKLE):
            with open(TOKEN_PICKLE, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server()
    
            # Save the credentials for the next run
            with open(TOKEN_PICKLE, 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # set the values for the sheet
        values = [[temperature, humidity, timestamp]]
        body = {'values': values}

        # insert the new reading into the Google Sheet
        result = service.spreadsheets().values().append(
                spreadsheetId=SHEET_ID, range=SHEET_RANGE,
                valueInputOption='USER_ENTERED', body=body).execute()
        print('{0} cells appended to Google Sheet.'.format(result \
                .get('updates') \
                .get('updatedCells')))
    
    else:
        # CONSIDER LOGGING THIS AS 0
        print('Failed to get reading from sensor. Try again!')

    # END MAIN

if __name__ == '__main__':
    main()
