# The main point of this code is to show how to call the Computer Vision API from Python

import os

# use json library to read data passsed back and the web serv
import sys
import json
import io
import logging

# Hide your keys protect it with your life
from dotenv import load_dotenv
load_dotenv(dotenv_path='C:/Users/jessiereddjr./venv/keys.env')

#import the requests library
import requests
