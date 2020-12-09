# Configuration file is a collection of all global variables that need to be accessible across multiple files,
# as explain in this StackOverflow post:
# https://stackoverflow.com/questions/13034496/using-global-variables-between-files

# To use the global variables in these files, there are two options:
# 1. import config # imports everything from the config file
# 2. from config import $variableName$

import picamera

camera = picamera.PiCamera()
# This is required so that we only have a single instance of the picamera.PiCamera()
# Issue documented here:
# https://github.com/MattPChoy/RaspberryPiTimelapse/wiki/Part-4:-Capturing-Images-with-Interval#mmal-out-of-resources-error
