import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Данные
path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
path = pd.read_csv(path)


st.write(tips)

# 4

st.subheader('4.total_bill')
plt.hist(path['total_bill'])
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
st.pyplot()

# 5
st.subheader('Cвязь между total_bill and tip')
plt.scatter(tips['total_bill'], tips['tip'])
plt.xlabel('Total Bill')
plt.ylabel('Tip')
st.pyplot()

# 7
st.subheader('График связывающий total_bill, tip, и size')
plt.scatter(path['total_bill'], path['tip'], s=path['size']**3, c='blue')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
st.pyplot()

# 8
st.subheader('Cвязь между днем недели и размером счет')
plt.bar(path['day'],path['tip'], )
plt.xlabel('Day')
plt.ylabel('Tip')

st.pyplot()

# 9
st.subheader('scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу')
clr=['red' if i =='Female' else 'blue' for i in path['sex']]
plt.scatter(path['tip'], path['day'], c=clr)
plt.xlabel('Tip')
plt.ylabel('Day')
st.pyplot()




