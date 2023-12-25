# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 12:16:57 2023

@author: c surya vamsi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

crop_model=pickle.load(open('C:/Users/c surya vamsi/1trainedmodel.sav','rb'))
nutri_model=pickle.load(open('C:/Users/c surya vamsi/Downloads/trainedmodel1.sav','rb'))

with st.sidebar:
    selected = option_menu('CHOOSING MODELS', ['NUTRIENTS PREDICTION','CROP RECOMMENDATION'],default_index=0)
 
if ( selected == 'NUTRIENTS PREDICTION'):
    def prediction1(input_data):
        new_data = pd.DataFrame({'rainfall': [input_data[0]], 'temperature': [input_data[1]], 'humidity': [input_data[2]], 'ph': [input_data[3]], 'label': [input_data[4]]})
        new_predictions = nutri_model.predict(new_data)
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
            output=prediction1([rainfall,temp,humidity,ph,label])
        
        st.success(output) 


    if __name__=='__main__':
        main()

if ( selected =='CROP RECOMMENDATION'):
    def prediction(input_data):
        newValues1=np.array(input_data)
        newValues1=newValues1.reshape(1,-1)
        return ('The recommended model for your data is',crop_model.predict(newValues1))
        
    def main():
        st.title("CROP RECOMMENDATION SYSTEM WEB APP")
        #N	P	K	temperature	humidity	ph	rainfall	label
        N=st.text_input('enter value of N')
        P=st.text_input('enter value of P')
        K=st.text_input('enter value of k')
        temp=st.text_input('enter value of temprature')
        humidity=st.text_input('enter value of humidity')
        ph=st.text_input('enter value of ph')
        rainfall=st.text_input('enter value of rainfall')
        
        output=''
        if st.button('recommended crop'):
            output=prediction([N,P,K,temp,humidity,ph,rainfall])
        
        st.success(output) 


    if __name__=='__main__':
        main()       