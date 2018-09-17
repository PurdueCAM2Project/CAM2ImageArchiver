'''
Copyright 2017 Purdue University

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import time
import csv
import os

from utils import check_file_exists, check_result_path_writable
from camera import NonIPCamera, IPCamera, StreamCamera
from CameraHandler import CameraHandler

"""
Created on 5 September 2017
@author: Sam Yellin

Full documentation available at https://purduecam2project.github.io/CAM2ImageArchiver/index.html

See README for database setup information.
"""

class CAM2ImageArchiver:
    '''
    Retrieves images from cameras specified through a csv file.  The csv file either contains the urls of the cameras, or the ID numbers of each camera in the database.
    remove_duplicates_threshold: Percentage difference between two frames
    '''
    def __init__(self, num_processes=1, result_path='results/', remove_duplicates_threshold=10):
        self.num_processes = num_processes
        self.result_path = result_path
        self.remove_duplicates_threshold = remove_duplicates_threshold

    def retrieve_csv(self, camera_url_file, duration, interval, result_path, remove_after_failure=True):
        '''
        Reads camera urls from csv file and archives the images at the requested directory.
        '''

        #verify file exists and can be read
        if not check_file_exists(camera_url_file):
            raise IOError("The given camera url file does not exist.")

        if not check_result_path_writable(result_path):
            raise IOError("Insufficient permissions to write results to result path.")

        with open(camera_url_file, 'r') as camera_file:
            camera_reader=csv.reader(camera_file)
            id=1
            cams=[]
            for camera_url in camera_reader:
                #These cameras do not come from the database and so have no ID.  Assign one to them so they can be placed in a result folder.
                camera_type = camera_url[0].split(".")[-1]
                if (camera_type == "m3u8"):
                    camera = {'type': 'stream', 'id': id, 'm3u8_url': camera_url[0]}
                else:
                    camera = {'type': 'non_ip', 'id': id, 'snapshot_url': camera_url[0]}
                id+=1
                cams.append(camera)
        if len(cams):
            self.archive(cams, duration, interval, result_path, remove_after_failure)

    def archive(self, camObjects, duration=1, interval=1, result_path=None, remove_after_failure=True):
        '''
        Archives images from array of cameras.  Places directory of all results at the given path.
        '''
        if result_path == None:
            result_path = self.result_path

        cams = []
        for cam in camObjects:
            cams.append(self.__get_camera_from_object(cam))

        camera_handlers = []
        # Create result directories for all cameras
        for camera in cams:
            cam_directory = os.path.join(result_path, str(camera.id))
            try:
                os.makedirs(cam_directory)
            except OSError as e:
                pass

        # Split cameras into chunks for threading
        camera_lists = [cams[i::self.num_processes] for i in range(self.num_processes)]

        # Get rid of empty lists that may result from splitting into more threads than cameras
        camera_lists = [camera_list for camera_list in camera_lists if camera_list != []]

        chunk = 0
        for camera_list in camera_lists:
            # Increment chunk number
            chunk += 1
            # Create a new process to handle the camera.
            camera_handler = CameraHandler(camera_list, chunk, duration, interval, result_path, remove_after_failure, remove_duplicates_threshold=self.remove_duplicates_threshold)
            # Run the process.
            camera_handler.start()
            # Add the process to the array of process.
            camera_handlers.append(camera_handler)

            # Sleep to shift the starting time of all the process.
            # time.sleep(interval / len(cams)) # Old
            time.sleep(0.5)

        # Wait for all the process to finish execution.
        for camera_handler in camera_handlers:
            camera_handler.join()

        

    def __get_camera_from_object(self, cam):
        '''
        Reads converts CAM2 Camera API Camera Object to Archiver Camera Object
        '''
        if cam['camera_type'] == 'ip':
            camera = IPCamera(cam['cameraID'], cam['ip'], cam['image_path'],
                              cam['video_path'], cam['port'])
        elif cam['camera_type'] == 'non_ip':
            camera = NonIPCamera(cam['cameraID'], cam['snapshot_url'])
        elif cam['camera_type'] == 'stream':
            camera = StreamCamera(cam['cameraID'], cam['m3u8_url'])
        else:
            raise ExpectedCAM2APIClientCameraObject()

        return camera