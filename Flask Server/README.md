# Flask Server
This folder contains necessary files to run the server

Run the server with `python app.py` inside of a conda environment or with the appropriate packages installed.


# Conda env
In this folder you will find `webcam.yml` which is an Anaconda file. It can automatically create a conda environment with this command: 
```
conda env create --file webcam.yml
```

I have had problems with that in the past though, so you can always create a conda environment by hand using these commands:
```
conda create -n webcam python=3.7 flask opencv eventlet
conda activate webcam
conda install -c conda-forge imutils
conda install -c conda-forge flask-socketio
```

# ngrok
"One command for an instant, secure URL to your localhost server through any NAT or firewall."

It allows our flask server to be accessible by anyone. 

Download it here: https://ngrok.com/

Unzip the folder anywhere and open a command prompt and cd into the folder. Then type `ngrok http <port>` 

For example, `ngrok http 5000`

# Links
Tutorial from pytorch about server-side inference:
https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html

Flask video stream: 
https://stackoverflow.com/questions/58931854/how-to-stream-live-video-frames-from-client-to-flask-server-and-back-to-the-clie
