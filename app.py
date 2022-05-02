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
pred_num = str(st.sidebar.number_input('Type in the number',min_value=7000000000,max_value=9999999999
         ))
output = ''
if pred_num[0:3] in ['703','704','706','803','806','810','813','814','816','903','906','913','916']:
    output ='MTN'
elif pred_num[0:4] in ['7025','7026']:
    output ='MTN'
elif pred_num[0:3] in [ '701','708','802','808','812','901','902','904','907','912']:
    output ='Airtel'
elif pred_num[0:3] in ['705','805','807','811','815','905','915']:
    output ='Globacom' 
elif pred_num[0:3] in ['809','817','818','909','908']:
    output ='9mobile'
elif pred_num[0:3] in ['804']:
    output ='MTEL'
else:
    output ='invalid'
st.sidebar.text(output+ " number ")        
Service_providers = st.sidebar.selectbox('Name Of Service provider',
           ['MTN', 'Airtel', '9mobile', 'Globacom', 'MTEL']
        )
phones = jb.load('phones.pkl')
num_ = len(phones[phones['lines']==Service_providers])
st.sidebar.text("The total of "+ str(Service_providers)+ f" users is "+str(num_))

####plot for summary report
st.subheader('Service providers summary')
servce_summ =[]
for i in ['MTN', 'Airtel', '9mobile', 'Globacom', 'MTEL']:
    servce_summ.append(len(phones[phones['lines']==i]))
st.write(pd.DataFrame({
    'Service providers': ['MTN', 'Airtel', '9mobile', 'Globacom', 'MTEL'],
    'Total users': servce_summ}))
fig1, ax1 = plt.subplots()
explode = (0.1, 0, 0, 0,0)
ax1.pie(servce_summ, explode=explode, labels=['MTN', 'Airtel', '9mobile', 'Globacom', 'MTEL'],
        shadow=False, startangle=90,colors=['yellow','red','#99ff99','green','black'])
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)


