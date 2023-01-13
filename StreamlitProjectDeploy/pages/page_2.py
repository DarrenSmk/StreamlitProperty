import streamlit as st
import pandas as pd


st.markdown("# Local Factors")
st.sidebar.markdown("# Local factors")
st.sidebar.write("Population by type of house")
st.sidebar.write("Tenure of Accomodation ")
st.sidebar.write("Long-term Housing Strategy")
st.sidebar.write("Median Monthly Income")
st.sidebar.write("Prime Rate")
st.sidebar.write("Stamp Duty")
st.sidebar.write("Mortgage Calculator")

st.header('Population by type of house')
st.write('Majority of the people live in private permanent housing')
st.write('About 30 percent of the people live in public rental housing with the median monthly rent of $2090 HKD')
st.image('StreamlitProjectDeploy/img/populationByTypeofHouse.png')



st.header('Domestic Households by Tenure of Accomodation')
st.markdown("About 30 percent of the households are in private permanent housing and :green[without] mortgage and loan")
st.markdown("About 15 percent of the households are in private permanent housing and :red[with] mortgage and loan")
st.write('About 30 percent of the households are in public rental housing')
st.write('About 17 percent of the households are sole tenant')
st.image('StreamlitProjectDeploy/img/2021DomesticHousholds.png')

st.header('Long-term Housing Strategy')
st.write('the Long Term Housing Strategy Annual Progress Report 2022 (the Progress Report).')
st.write('The gross total housing demand for the next 10-year period (i.e. 2023-24 to 2032-33) is 421,000 units, hence the Government set the supply target at 430,000 units.')
st.image('StreamlitProjectDeploy/img/construction.jpg')

st.header('Median Monthly Income')
st.markdown("The median monthly income is :red[doubled] from 1997 to 2022")
st.write('From 10 thousand to 20 thousand per month')
st.image('StreamlitProjectDeploy/img/SalaryValue.png')


st.header('Prime Rate')
st.write('It does not show a strong relationship between prime rate and the properties market.')
st.write('If the prime rate keep increasing in the coming years, it is believed that it will become the last straw that break the camel\'s back')
st.image('StreamlitProjectDeploy/img/P-rateValue.png')

st.header('Stamp Duty')
data = [['Special Stamp Duty, SSD','between 20% to 10%','To prevent the buyer resell it within 3 years','27 Oct 2012'],['Double Stamp Duty, DSD','15%','To those non-first time buyer','5 Nov 2016'],['Buyer Stamp Duty, BSD','15%','Not HKPR and conpany buyers','19 Oct 2022']]
df = pd.DataFrame(data,
    columns=['Type','Rate','Target','Effective Date'],
    index=[1,2,3]
)
st.table(df)
st.image('StreamlitProjectDeploy/img/stampduty.jpg')



