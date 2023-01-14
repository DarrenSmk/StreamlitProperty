import streamlit as st
import pandas as pd



st.markdown("# Hong Kong Real Estate")
st.write('by Darren Shum & Tracy Cheung')
st.sidebar.markdown("# Main page")
st.sidebar.write("Purpose")
st.sidebar.write("Dataset")
st.sidebar.write("HK Population")
st.sidebar.write("Property Transaction History")



st.image('StreamlitProjectDeploy/img/HK.jpg')
st.write('The most expensive residential property market in the world')
st.header('Purpose:')
"""
1. Is it a bubble !?
2. What are the major factors that affect the Hong Kong property value?
3. To predict Hong Kong property market's performance in the coming year.
"""


st.header('Dataset')
datasetTable = pd.read_csv('StreamlitProjectDeploy/dataset.csv')
st.table(datasetTable)


st.header('The Population history ')
st.write('The population from 6.5 million in 1997 raise to 7.3 million in 2022.')
st.write('Increased 800 thousand pepole (about 12%➚) ')
st.image('StreamlitProjectDeploy/img/population97to22.png')

st.header('2022 Population distribution by age group')
st.write('Entering into an ageing society due to the increased life expectancies and declining birth rate')
st.image('StreamlitProjectDeploy/img/2022PopulationDistribution.png')


st.header('Property transaction history ')
st.write('Property price slumped after asian financial crisis in 1997 ')
st.write('The Primary residential market raised alongside the Secondary residential market')
st.write('The transaction value of secondary residential market in 2021 reached the peak in the history and declined rapidly in 2022')
st.write('The transaction volume is relatively steady in the past 10 years')
st.write('*Overall property included residential property, industrial, office, retail, carpark & others')
st.image('StreamlitProjectDeploy/img/PropertyOverall.png')

