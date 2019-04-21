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

from picamera import PiCamera
from time import sleep
from datetime import datetime

# path to save photos
PHOTO_PATH = '/home/pi/pi-sensor-temperature/photos'

# create the camera object
camera = PiCamera()

# grab the date and time
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') 

# give time to focus and adjust light, then take a photo and save it
camera.rotation = 270
camera.start_preview()
camera.annotate_text_size = 10
camera.annotate_text = timestamp
sleep(5)
camera.capture(PHOTO_PATH + '/photo_' + timestamp + '.jpg')
camera.capture(PHOTO_PATH + '/photo_latest.jpg')
camera.stop_preview()
