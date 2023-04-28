

# from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
# import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# @app.route('/')
def welcome():
    return "Welcome All"

# @app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
   
    gender=request.args.get("gender")
    ssc=request.args.get("ssc")
    hsc=request.args.get("hsc")
    cet=request.args.get("cet")
    branch=request.args.get("branch")
    branch=request.args.get("branch")
    intership=request.args.get("intership")
    aptitude=request.args.get("aptitude")
    degree=request.args.get("degree")
    prediction=classifier.predict([[gender,ssc,hsc,cet,branch,intership,aptitude,degree]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    
