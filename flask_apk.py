


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(gender,ssc,hsc,cet,branch,intership,aptitude,degree):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: gender
        in: query
        type: char
        required: true
      - name: ssc
        in: query
        type: number
        required: true
      - name: hsc
        in: query
        type: number
        required: true
      - name: cet
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[gender,ssc,hsc,cet,branch,intership,aptitude,degree]])
    print(prediction)
    return prediction



def main():
    st.title("Student Placement Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Student Placement Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    gender = st.text_input("Gender","Type Here")
    ssc = st.text_input("SSC%","Type Here")
    hsc = st.text_input("HSC%","Type Here")
    cet = st.text_input("cet%","Type Here")
    branch = st.text_input("Branch","Type Here")
    intership = st.text_input("Intership","Type Here")
    aptitude = st.text_input("Aptitude","Type Here")
    degree = st.text_input("Degree","Type Here")
    status=""  
    salary="" 
    if st.button("Predict"):
        result=predict_note_authentication(gender,ssc,hsc,cet,branch,intership,aptitude,degree)
    st.success('Student Status is {} and salary is {}'.format(status,salary))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
