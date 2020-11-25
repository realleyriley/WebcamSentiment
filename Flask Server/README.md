# Flask Server
This folder contains necessary files to run the server

Run the server with `python app.py` inside of a conda environment or with the appropriate packages installed.


# Conda env
In this folder you will find `webcam.yml` which is an Anaconda file. It can automatically create a conda environment with this command: 
```
conda env create --file webcam.yml
```
YOU WILL NEED TO CHANGE THE LAST LINE OF THE FILE TO FIT YOUR COMPUTER. 
This is the last line: `prefix: C:\Users\rptal\miniconda3\envs\webcam` but you must change that to wherever your miniconda or anaconda is installed I think.

I have had problems with that in the past though, so you can always create a conda environment by hand using these commands:
```
conda create -n webcam python=3.7 flask opencv eventlet
conda activate webcam
conda install -c conda-forge imutils
conda install -c conda-forge flask-socketio
conda install pillow
```
There are probably more packages than just those to install though.

# Links
Tutorial from pytorch about server-side inference:
https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html

Flask video stream: 
https://stackoverflow.com/questions/58931854/how-to-stream-live-video-frames-from-client-to-flask-server-and-back-to-the-clie
