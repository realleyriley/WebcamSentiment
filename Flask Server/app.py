# Flask Server code
# adapted from https://stackoverflow.com/questions/58931854/how-to-stream-live-video-frames-from-client-to-flask-server-and-back-to-the-clie
# and from https://github.com/PrettyPrinted/flask-socketio-chat/blob/master/index.html


import os
import sys
from flask import Flask, render_template, request, Response
from flask_socketio import SocketIO, emit
import inference
from PIL import Image    # from pillow
import cv2
import numpy as np

# I've never used these before
import io
from io import StringIO
import base64

import inference


# this is useful for handling multiple clients (multiple tabs)
# lock = threading.Lock()

app = Flask(__name__)
socketio = SocketIO(app)


# this is the url to be used while predicting the label of the test video
# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.data

#     return json_dict

# We can use this url extension to send files to the server
# https://mydomain.com/do_something
# @app.route('/do_something', methods=['POST'])
# def upload():
#     file = request.files['myfile']


@app.route('/', methods=['POST', 'GET'])
def index():
    print('new client... returning index.html', flush=True)
    return render_template('index.html')

import pdb

@socketio.on('image')
def image(data_image):
    # for some reason the image doesn't always send.
    # I think it takes the camera a second to warm up.
    # Its best to handle this in javascript for optimizations
    if len(data_image) < 30:
        return

    sbuf = StringIO()
    sbuf.write(data_image)


    headers, base64_image = data_image.split(',', 1) 

    # decode and convert into image
    b = io.BytesIO(base64.b64decode(base64_image))
    pimg = Image.open(b)

    # converting RGB to BGR, as opencv standards
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    # Process the image frame
    frame = inference.run_inference(frame)
    imgencode = cv2.imencode('.jpg', frame)[1]

    # base64 encode
    stringData = base64.b64encode(imgencode).decode('utf-8')
    b64_src = 'data:image/jpg;base64,'
    stringData = b64_src + stringData

    # emit the frame back
    emit('response_back', stringData)


# if we are running this file directly rather than importing it:
if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', debug=True)