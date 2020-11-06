# Flask Server code

import os
from flask import Flask, render_template, request

app = Flask(__name__)

# this is called when just the root domain is requested, ie https://mydomain.com/
@app.route('/')
def index():
    return render_template('index.html')

# this is the url to be used while predicting the label of the test video
@app.route('/predict', methods=['POST'])
def predict():
    data = request.data

    return json_dict

# We can use this url extension to send files to the server
# https://mydomain.com/do_something
@app.route('/do_something', methods=['POST'])
def upload():
    file = request.files['myfile']


# if we are running this file directly rather than importing it:
if __name__ == '__main__':
    app.run(port=5000, debug=True)
