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

@app.route("/wait_on working", methods=['GET'])
def sign_up():
  f=open("signup/sign_up.html","r")
  text=f.read()
  f.close()
  return text

@app.route("/sign_up", methods=['GET'])
def PROFILE():
  f=open("profile/Profile.html","r")
  text=f.read()
  f.close()
  return text

@app.route("/profile_submit", methods=['POST'])
def PROFILE_SUBMIT():
  try: first_name = request.form['first_name']
  except: first_name="can't_read"
  try: last_name = request.form['last_name']
  except: last_name="can't_read"
#   try: password = request.form['password']
#   except: password="can't_read"
#   try: confirm_password = request.form['confirm_password']
#   except: confirm_password="can't_read"
#   try: University_Roll = request.form['University_Roll']
#   except: University_Roll="can't_read"
#   try: gender = request.form['gender']
#   except: gender="can't_read"
#   try: email = request.form['email']
#   except: email="can't_read"
#   try: phone_number = request.form['phone_number']
#   except: phone_number="can't_read"
#   try: University = request.form['University']
#   except: University="can't_read"
#   try: Branch = request.form['Branch']
#   except: Branch="can't_read"
#   try: College = request.form['College']
#   except: College="can't_read"
  
  text=f"first_name = {first_name} \n"+f"last_name = {last_name} \n"#+f"password = {password} \n"+f"confirm_password = {confirm_password} \n"+f"University_Roll = {University_Roll} \n"+f"gender = {gender} \n"+f"email = {email} \n"+f"phone_number = {phone_number} \n"+f"University = {University} \n"+f"Branch = {Branch} \n"++f"College = {College} \n"
  
  return text



