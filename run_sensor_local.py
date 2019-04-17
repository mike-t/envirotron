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

# imports 
import Adafruit_DHT
import time
import logging

# Set IO pin and Sensor 
# should be set to Adafruit_DHT.DHT11,# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
SENSOR = Adafruit_DHT.DHT22
IOPIN = 4

# file for logging
LOGFILE = '/home/pi/pi-sensor-temperature/pi-sensor-temperature-humidity.log'

## Main function
def main():

    # set the logging format
    logging.basicConfig(filename=LOGFILE, filemode='a', format='%(created)f %(message)s', level=logging.INFO)

    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, IOPIN)

    # if we got a hit, log it!
    if humidity is not None and temperature is not None:
        logging.info('{0:0.2f}C {1:0.2f}%'.format(temperature, humidity))
    else:
        # CONSIDER LOGGING THIS AS 0
        print('Failed to get reading from sensor. Try again!')

    # END MAIN

if __name__ == '__main__':
    main()
