import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# load model 
with open('model.pickle','rb') as temp:
    model = pickle.load(temp)

# load gambar
img = plt.imread('titanic.jpg')
st.image(img,width=700)

st.title('Predicting the Survival of Titanic Passengers')
st.text("")
st.text("")

# Variabel
gender = ('Male','Female')
male = 0
female = 0

# menerima inputan Age	Fare	Parch	Pclass	Sex_female	Sex_male	SibSp
age = st.number_input('Your Age : ')

Fare = st.number_input('Your Fare : ')

Parch = st.number_input('Your Parch : ')

Pclass = st.number_input('Your Pclass : ')

electedGender = st.selectbox('Select Your Gender : ',gender)
if electedGender == 'Male':
    male = 1.0
    female = 0.0
else:
    male - 0.0
    female = 1.0

SibSp = st.number_input('Your SibSp : ')

# prediction
predict  = model.predict([[age,Fare,Parch,female,male,SibSp]])

if predict == 1.0:
    temp = 'You are Survived'
elif predict == 0.0:
    temp = 'Rest in Peace :('

button = st.button('Predicton',key=1)

if button==True:
    st.write(temp)