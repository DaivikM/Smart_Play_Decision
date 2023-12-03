#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder

# In[2]:


import streamlit as st
import pickle
import string


# In[5]:

st.header("Original Data:")
model = pickle.load(open('model.pkl','rb'))
# Load the DataFrame from the pickle file
with open('weather_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

loaded_data


# In[11]:


st.title("Should You Play Outside??")
# label_encoder = LabelEncoder()
# User input for weather conditions
outlook = st.selectbox('Select Outlook:', loaded_data['Outlook'].unique())
# temperature = st.selectbox('Select Temperature:', loaded_data['Temperature'].min(), loaded_data['Temperature'].max())
# humidity = st.selectbox('Select Humidity:', loaded_data['Humidity'].min(), loaded_data['Humidity'].max())
temperature = st.selectbox('Select Temperature:', loaded_data['Temperature'].unique())
humidity = st.selectbox('Select Humidity:', loaded_data['Humidity'].unique())
wind = st.selectbox('Select Wind:', loaded_data['Windy'].unique())

# Make a prediction
input_data = pd.DataFrame({'Outlook': [outlook], 'Temperature': [temperature], 'Humidity': [humidity], 'Windy': [wind]})
# input_data['Outlook'] = label_encoder.transform(input_data['Outlook'])

input_data['Outlook'] = input_data['Outlook'].map({'Overcast':0,'Rain':1,'Sunny':2})
input_data['Temperature'] = input_data['Temperature'].map({'Cool':0,'Hot':1,'Mild':2})
input_data['Humidity'] = input_data['Humidity'].map({'High':0,'Normal':1})
input_data['Windy'] = input_data['Windy'].map({'Strong':0,'Weak':1})


# prediction = model.predict(input_data)

# Display the prediction
st.subheader('Prediction:')
if st.button('Predict'):
    
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.header('You can Play Outside!')
    else:
        st.header("It's not suitable for Playing Outside.")


# In[ ]:




