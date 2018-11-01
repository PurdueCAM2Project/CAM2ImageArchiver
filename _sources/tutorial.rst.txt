====================================
Quickstart
====================================

We will present here some basic usage examples.

You may want to use the CAM2 Image Archiver with the `CAM2 Camera Database Python Client <https://purduecam2project.github.io/CameraDatabaseClient/build/html/index.html>`_.


Create a CAM2 Image Archiver Instance
------------------------------------------------

After installing, import the CAM2 Image Archvier class from the CAM2 Image Archiver module. 

>>> from CAM2ImageArchiver import CAM2ImageArchiver

Then, create a CAM2 Image Archiver Instance. Optionally, you can specify the following parameters:

:num_processes: The number of archiving processes you wish to start during the archiving process. The archiver can download images much faster if you increase the number of processes. Usually the archiver is bandwidth limited so you should pay attention to the amount of bandwidth you have to work with. The default value is 1.

:results_path: This parameter is a string to the path at which you wish to save your results. All images that the archiver downloads will be stored at: *<results_path>/<cameraID>/<datetime string>.png* The datetime string has the following format: *<Year>-<Month>-<Day>_<Hour>-<Minuet>-<Secound>-<Microsecond>'*. The default value is 'results/'. 

:image_difference_percentage: This parameter is the threshold percentage at which to discard the image. The archiver will download a new image in the specified time interval and then compare the image to the previous image using: :math:`\sum_{i = 0}^{frameSize}{(| lastFrame[i] - currentFrame[i] | > 0)} * \frac{100}{frameSize}` to sum up the percentage of pixels between the images that have changed. If the percentage is greater than or equal to *image_difference_percentage* then the image will be saved. To disable this feature set *image_difference_percentage* to *0* or *False*. The default value is if at least 90% of the pixels have changed between the images, the image will be saved.

>>> archiver = CAM2ImageArchiver(num_processes=1, result_path='results/', image_difference_percentage=90)

Creating Camera Objects
------------------------------------------------

We then need to specify a list of :class:`~CAM2ImageArchiver.camera.Camera` objects to pass to the archiver. Camera objects from the `CAM2 Camera Database Python Client <https://purduecam2project.github.io/CameraDatabaseClient/build/html/index.html>`_ can be passed directly to the archiver. Camera objects can also manually created as shown in the example below. 

>>> cam = [{'camera_type': 'non_ip', 'cameraID':'1', 'snapshot_url':'<The URL to the Camera Image Data>'}]

This is an example of a *non_ip* camera. At a minimum, each *non_ip* camera object must contain the information shown above. 

:camera_type: field determines how the camera data will be downloaded. Review the :class:`~CAM2ImageArchiver.StreamParser.StreamParser` module for more details on how the camera data is downloaded.

:cameraID: is a unique identifier for the camera. The file name of the saved image will have contain the cameraID.

:snapshot_url: if the camera is a *non_ip* camera, the camera must contain the *snapshot_url* field. non_ip cameras are those who's image data can be downloaded using a HTTP GET request to a static URL.

The CAM2 Image Archiver supports two other formats of camera data. The other types of cameras are defined as *IP* cameras and *Stream* cameras. Below are examples of camera objects of these types. 

>>> cam2 = [{'camera_type': 'stream', 'cameraID':'2', 'm3u8_url':'<The .m3u8 playlist file URL>'}] # Stream Camera Example
>>> cam3 = [{'camera_type': 'ip', 'cameraID':'3', 'image_path':'<The path to a static image>',
	'video_path':'<A video path such as an .mjpeg>'}, 'port':'<The port of the camera>'] # IP Camera Example

If you use the CAM2 Camera Database Client to retrieve Camera objects, all the necessary fields will be defined for you. 


Downloading Images
------------------------------------------------

To download images use the :meth:`~CAM2ImageArchiver_class.CAM2ImageArchiver.archive` method as shown below.

>>> archiver.archive(cam, duration=<duration(sec) to archive data>, interval=<interval(sec) to archive data>)

The archiver will then begin to download images from the cameras specified in the list and saving them to the *results_path* directory. 

.. _camera-by-city-ref:

Using the CAM2 Image Archiver with the CAM2 Camera Database Client
---------------------------------------------------------------------

Below is a sample script that will allow you to use both the CAM2 Image Archiver and the CAM2 Database Client togather. Please note that you must have the *clientID* and *clientSecret* from the CAM2 Camera Database API. For more information on the CAM2 Database Client please see `the documentation <https://purduecam2project.github.io/CameraDatabaseClient/build/html/index.html>`_.


.. literalinclude:: CAM2ArchiverClientExample.py
   :language: python


