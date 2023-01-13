import streamlit as st

st.markdown("# Global Factors")
st.sidebar.markdown("# Global Factors")
st.sidebar.write("China GDP and PPI")
st.sidebar.write("Hang Seng Index")
st.sidebar.write("US Index")



st.header('China GDP and PPI')
st.write('China GDP remained about 8 percent cumulative quarterly year-on-year growth from 2012 to 2019')
st.write('PPI drop under zero recently mirroring a sluggish global economic environment ')
st.write('Due to the China and US trade war recently, the political issue is uncertain, China is losing its advantage on the subcontract business.')
st.image('StreamlitProjectDeploy/img/PPIvsGDP12-22.png')

st.header('Hang Seng Index and value of overall properties')
st.write('The property market is highly correlated to the HSI')
st.image('StreamlitProjectDeploy/img/HSIvsPropertiesValue.png')

st.header('US Index')
st.write('US Indexes price slumped in 2008 and 2019 due to the financial crisis and COVID-19 recession ')
st.write('US Indexes is one of the factors that influence Hong Kong property market')
st.write('The stock market is flooded with money since the QE in 2020, assuming that a long high interest rate period is coming to against the high inflation. Therefore, the stock market will go into a bear market in 2023.')
st.image('StreamlitProjectDeploy/img/USstockIndex.png')
