# Import CAM2 Image Archiver and CAM2 Camera Database Client:
from CAM2CameraDatabaseAPIClient.client import Client
from CAM2ImageArchiver.CAM2ImageArchiver import CAM2ImageArchiver

if __name__ == '__main__':
        # Connect to API
        clientID = "<insert clientID here>"
        clientSecret = "<insert clientSecret here>"
        db = Client(clientID, clientSecret)

        # Create an CAM2 Image Archiver Object:
        archiver = CAM2ImageArchiver(num_processes=10)

        # Search the API for cameras from West Lafayette
        cams = db.search_camera(city='West Lafayette', offset=offset)

        # Add an additional camera of your own:
        camera2 = [{'camera_type': 'stream', 'cameraID':'2', 'm3u8_url':'<The .m3u8 playlist file URL>'}] 
        cams = cams + camera2

        # Archive data from the cameras every 20 min for an hour.
        archiver.archive(cams, duration=60*60, interval=20*60)