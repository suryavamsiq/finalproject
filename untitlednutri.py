# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:01:08 2023

@author: c surya vamsi
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 10:56:34 2023

@author: c surya vamsi
"""

import pickle
import numpy as np
loaded_model=pickle.load(open('C:/Users/c surya vamsi/Downloads/trainedmodel1.sav','rb'))
import streamlit as st
from sklearn.preprocessing import LabelEncoder
import pandas as pd
encoder=LabelEncoder()

def prediction(input_data):
    new_data = pd.DataFrame({'rainfall': [input_data[0]], 'temperature': [input_data[1]], 'humidity': [input_data[2]], 'ph': [input_data[3]], 'label': [input_data[4]]})
    new_predictions = loaded_model.predict(new_data)
    predictions_array = np.array(new_predictions)
    final_array = predictions_array.tolist()
   # final_array[0][2]=abs(final_array[0][2]-1.78)
    return ('Predicted N,K,P values:', final_array[0][0],final_array[0][1],final_array[0][2]) 
    

    
def main():
    st.title("NUTRIENTS SYSTEM WEB APP")
    #rainfall', 'temperature', 'humidity','ph','label
    rainfall=st.text_input('enter value of rainfall')
    temp=st.text_input('enter value of temperature')
    humidity=st.text_input('enter value of humidity')
    ph=st.text_input('enter value of ph')
    labell=st.text_input('enter name of crop')
    label=''
    if labell=='rice':
        label=20
    elif labell=='maize':
        label=11
    elif labell=='chickpea':
        label=3
    elif labell=='kidneybeans':
        label=9
    elif labell=='pigeonpeas':
        label=18
    elif labell=='mothbeans':
        label=13
    elif labell=='mungbean':
        label=14
    elif labell=='blackgram':
        label=2
    elif labell=='lentil':
        label=10
    elif labell=='pomegranate':
        label=19
    elif labell=='banana':
        label=1
    elif labell=='mango':
        label=12
    elif labell=='grapes':
        label=7
    elif labell=='watermelon':
        label=21
    elif labell=='muskmelon':
        label=15
    elif labell=='apple':
        label=0
    elif labell=='orange':
        label=16
    elif labell=='papaya':
        label=17
    elif labell=='coconut':
        label=4
    elif labell=='cotton':
        label=6
    elif labell=='jute':
        label=8
    elif labell=='coffee':
        label=5
        
        

    
    output=''
    if st.button('recommended crop'):
        output=prediction([rainfall,temp,humidity,ph,label])
    
    st.success(output) 


if __name__=='__main__':
    main()
    
    
    

