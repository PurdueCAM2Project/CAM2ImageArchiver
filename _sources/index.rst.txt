.. Cam2ImageArchiver documentation master file, created by
   sphinx-quickstart on Mon Oct 23 04:29:51 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CAM2 Image Archiver 
====================================================

Welcome to the CAM2 Image Archiver Documentation! 

This is documentation for the
`CAM2 Image Archiver <https://purduecam2project.github.io/CAM2ImageArchiver/>`_, which is part of the `CAM2 Project <https://www.cam2project.net/>`_. 


Overview
---------

Thousands of network cameras are connected to the Internet and provide real-time visual data (image or video). Even though the data is publicly available to anyone interested seeing, there are several problems that prevents researchers and developers from effeciently query or retrievel camera information and their data. 

Even though the data is publicly available to anyone interested seeing, there are several problems. First, there is no central repository where network cameras must register. Thus, significant efforts must be taken to find various sources of data. Second, different brands of network cameras need different methods to retrieve the data. The cameas may also provide different data formats: some provide individual JPEG images; some provide motion JPEG (MJPEG) video; some others provide H.264 video.

To solve these problems, researchers at Purdue University maintains a network camera database and developed an API to retrieve data from heterogeneous sources. See `CAM2 Project <https://www.cam2project.net/>`_ website for more information.

The `CAM2 Camera API Database <https://purduecam2project.github.io/CAM2ImageArchiver/>`_ also has a `Python client <https://purduecam2project.github.io/CAM2ImageArchiver/>`_ avalable for those with a CAM2 Database API account. This allows developers and researchers to access the large collection of public network camera data with ease. CAM2 team can also manage camera data and accesses to the database through this client.

.. seealso::

    For more information on retrieving images and/or video from network cameras, please see the below section on :ref:`image-archiver-ref`, and `CAM2 Camera API Database Documentation <https://purduecam2project.github.io/CAM2ImageArchiver/>`_.


Installation
====================================================

.. toctree::
   :maxdepth: 2
   
   INSTALL.rst


Usage
====================================================

.. toctree::
   :maxdepth: 3
   
   tutorial.rst   

Modules
====================================================
.. toctree::
   :maxdepth: 2
   
   CAM2ImageArchiver.rst



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`