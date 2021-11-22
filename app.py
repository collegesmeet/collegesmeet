import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import sqlite3
import mysql.connector
import requests
from firebase import firebase

def profile_data_save(First_Name, Last_Name,Password,University_Roll,Gender,Email,Phone_Number,University,Branch,College):
    firebase=firebase.FirebaseApplication("https://collegesmeet-d973b-default-rtdb.firebaseio.com/",None)
    data={
        "first_name" : First_Name,
        "last_name" : Last_Name,
        "password" : Password,
        "University_Roll" : University_Roll,
        "gender" : Gender,
        "email" : Email,
        "phone_number" : Phone_Number,
        "University" : University,
        "Branch" : Branch,
        "College" : College
    }
    result=firebase.post("/collegesmeet-d973b-default-rtdb/profile",data)
    return result

def profile_data_read_and_conv_to_table():
    r=firebase.get("/collegesmeet-d973b-default-rtdb/profile","")
    Branch =[i["Branch"] for i in r.values()]
    College =[i["College"] for i in r.values()]
    University =[i["University"] for i in r.values()]
    University_Roll =[i["University_Roll"] for i in r.values()]
    # confirm_password =[i["confirm_password"] for i in r.values()]
    email =[i["email"] for i in r.values()]
    first_name =[i["first_name"] for i in r.values()]
    gender =[i["gender"] for i in r.values()]
    last_name =[i["last_name"] for i in r.values()]
    password =[i["password"] for i in r.values()]
    phone_number =[i["phone_number"] for i in r.values()]
    df=pd.DataFrame()
    df['first_name']=first_name
    df['last_name']=last_name
    df['password']=password
    # df['confirm_password']=confirm_password
    df['University_Roll']=University_Roll
    df['gender']=gender
    df['email']=email
    df['phone_number']=phone_number
    df['Branch']=Branch
    df['College']=College
    df['University']=University
    return df

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

@app.route("/profile_submit", methods=['GET', 'POST'])
def PROFILE_SUBMIT():
    try: first_name = request.form['first_name']
    except: first_name="can't_read"
    try: last_name = request.form['last_name']
    except: last_name="can't_read"
    try: password = request.form['password']
    except: password="can't_read"
    try: confirm_password = request.form['confirm_password']
    except: confirm_password="can't_read"
    try: University_Roll = request.form['University_Roll']
    except: University_Roll="can't_read"
    try: gender = request.form['gender']
    except: gender="can't_read"
    try: email = request.form['email']
    except: email="can't_read"
    try: phone_number = request.form['phone_number']
    except: phone_number="can't_read"
    try: University = request.form['University']
    except: University="can't_read"
    try: Branch = request.form['Branch']
    except: Branch="can't_read"
    try: College = request.form['College']
    except: College="can't_read"

    #text=f"first_name = {first_name} \n"+f"last_name = {last_name} \n"+f"password = {password} \n"+f"confirm_password = {confirm_password} \n"+f"University_Roll = {University_Roll} \n"+f"gender = {gender} \n"+f"email = {email} \n"+f"phone_number = {phone_number} \n"+f"University = {University} \n"+f"Branch = {Branch} \n"+f"College = {College} \n"
    #   try:
    #     conn = sqlite3.connect("collegesmeeet.db")
    #     cursor = conn.cursor()
    #     cursor.execute(f"""INSERT INTO profile VALUES ('{first_name}', '{last_name}', '{password}', '{University_Roll}', '{gender}', '{email}', '{phone_number}', '{University}', '{Branch}', '{College}' ) """)
    #     table=pd.read_sql_query("SELECT * FROM profile", conn)
    #     table.to_sql('profile', con=conn,index=None, if_exists='replace')
    #     conn.close()
    #     return table.to_html()
    #   except:
    #     return "SORRY CANT SAVE YOUR DATA"
    try:
        r=profile_data_save(first_name, last_name,	password,	University_Roll,	gender,	email,	phone_number,	University,	Branch,	College)
        table=profile_data_read_and_conv_to_table()
        return table.to_html()
    except:
        return "SORRY CAN'T SAVE YOUR DATA"
  
  
  
