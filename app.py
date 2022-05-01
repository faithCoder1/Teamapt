#####import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import joblib as jb

####streamlit settings for sidebar and main page
st.title("Mobile phone number summary report")
st.header("Made by Oluyemisi Yesufu ")
st.sidebar.markdown('<p class="header-style">Mobile number data summary</p>',
            unsafe_allow_html=True
        )
Service_providers = st.sidebar.selectbox('Name Of Service provider',
           ['MTN', 'Airtel', '9mobile', 'Globacom', 'MTEL']
        )
phones = jb.load('phones.pkl')
num_ = len(phones[phones['lines']==Service_providers])
st.text("The total of "+ str(Service_providers)+ f" users is "+str(num_))

####plot for summary report
st.subheader('Service providers summary')
servce_summ =[]
for i in ['MTN', 'Airtel', '9mobile', 'Globacom', 'MTEL']:
    servce_summ.append(len(phones[phones['lines']==i]))
st.write(pd.DataFrame({
    'Service providers': ['MTN', 'Airtel', '9mobile', 'Globacom', 'MTEL'],
    'Total users': servce_summ}))
fig1, ax1 = plt.subplots()
explode = (0, 0.1, 0, 0,0)
ax1.pie(servce_summ, explode=explode, labels=['MTN', 'Airtel', '9mobile', 'Globacom', 'MTEL'],
        shadow=False, startangle=90,)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)


