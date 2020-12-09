import picamera, time, os.path
from config import camera # Import all the global variables that we define in the configuration file.
from os import path
from flask import Flask, render_template, Response, request
from camera_pi import Camera
app = Flask(__name__)

directoryName = "data/timelapse"
imageFormat = ".jpg"
delayInSeconds = 0

def setup():
    getFreeFolder()

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


def captureImage():
    #  Do something with the camera
    numberOfFrames = 0
    while(True):
        camera.capture(directoryName + "capture" + str(numberOfFrames) + imageFormat)
        print("Capturing frame " + str(numberOfFrames))
        numberOfFrames += 1
        time.sleep(1)
        if (numberOfFrames > 10):
            break

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/data', methods=['POST'])
def acceptData():
    if request.method == "POST":
        print("Data recieved: " + request.form['interval'])
        delayInSeconds = int(request.form['interval'])
        captureImage()
    return ""


@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture')
def capture():
    return render_template('capture.html')

if __name__ == '__main__':
    setup()
    app.run(host='0.0.0.0', debug=True, threaded=True)
