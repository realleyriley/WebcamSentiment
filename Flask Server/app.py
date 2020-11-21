# Flask Server code
# adapted from https://stackoverflow.com/questions/58931854/how-to-stream-live-video-frames-from-client-to-flask-server-and-back-to-the-clie
# and from https://github.com/PrettyPrinted/flask-socketio-chat/blob/master/index.html


import os
from flask import Flask, render_template, request, Response
from flask_socketio import SocketIO, emit
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
    return render_template('index.html')

@socketio.on('image')
def image(data_image):
    sbuf = StringIO()
    sbuf.write(data_image)

    # decode and convert into image
    b = io.BytesIO(base64.b64decode(data_image))
    pimg = Image.open(b)

    # converting RGB to BGR, as opencv standards
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    # Process the image frame
    print('run_inf')
    frame = run_inference(frame)
    imgencode = cv2.imencode('.jpg', frame)[1]

    # base64 encode
    stringData = base64.b64encode(imgencode).decode('utf-8')
    b64_src = 'data:image/jpg;base64,'
    stringData = b64_src + stringData

    # emit the frame back
    emit('response_back', stringData)


# if we are running this file directly rather than importing it:
if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    socketio.run(app, host='127.0.0.1', debug=True)