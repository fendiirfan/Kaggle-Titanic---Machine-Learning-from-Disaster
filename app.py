import streamlit as st
import pickle
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
pclass = [1,2,3]
parch = [0,1,2,3,4,5,6]
sibsp = [0,1,2,3,4,5]
male = 0
female = 0

# menerima inputan Age	Fare	Parch	Pclass	Sex_female	Sex_male	SibSp
age = st.number_input('Passenger Age : ')

Fare = st.number_input('Passenger Fare : ')
Fare = int(Fare)

selectedSibSp = st.selectbox('Passenger SibSp : ',sibsp)

selectedParch = st.selectbox('Passenger Parch : ',parch)

selectedPclass = st.selectbox('Passenger Pclass : ',pclass)

selectedGender = st.selectbox('Select Passenger Gender : ',gender)
if selectedGender == 'Male':
    male = 1.0
    female = 0.0
else:
    male = 0.0
    female = 1.0

# prediction
predict  = model.predict([[age,Fare,selectedParch,selectedPclass,female,male,selectedSibSp]])

if predict == 1.0:
    temp = 'Alhamdulillah, Passenger are Survived'
elif predict == 0.0:
    temp = 'Rest in Peace :('

button = st.button('Prediction',key=1)

if button==True:
    st.write(temp)
