import picamera
import time
import os.path
from os import path


# Create directory to store images from current session
directoryName = "data/timelapse"
imageFormat = ".jpg"

def setup():
    getFreeFolder()

def captureImage():
    with picamera.PiCamera() as camera:
        #  Do something with the camera
        numberOfFrames = 0
        while(True):
            camera.capture(directoryName + "capture" + str(numberOfFrames) + imageFormat)
            print("Capturing frame " + str(numberOfFrames))
            numberOfFrames += 1
            time.sleep(1)
            if (numberOfFrames > 10):
                break
    # Automatically close the camera


def getFreeFolder():
    global directoryName
    count = 0
    while(True):
        if (os.path.exists(directoryName + str(count))):
            count += 1
        else:
            print("data/timelapse" + str(count) + " is free")
            break
    os.mkdir(directoryName + str(count) + "/")
    print("Making directory: " + directoryName + str(count))
    directoryName = directoryName + str(count) + "/"

setup()
captureImage()
