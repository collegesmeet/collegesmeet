import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
app = Flask(__name__)
# run_with_ngrok(app) 

@app.route("/", methods=['GET'])
def sign_in():
  f=open("sign_in/sign_in.html","r")
  text=f.read()
  f.close()
  return text

@app.route("/sign_up", methods=['GET'])
def sign_up():
  f=open("signup/sign_up.html","r")
  text=f.read()
  f.close()
  return text

@app.route("/sign_up_submit", methods=['GET','POST'])
def PROFILE():
  f=open("profile/Profile.html","r")
  text=f.read()
  f.close()
  return text
