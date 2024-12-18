import streamlit as st
import pandas as pd

st.title('Unsupervised Learning - Machine Learning')
st.info('K-Means Clustering with Wine Dataset')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/igunnawan31/data/refs/heads/main/winequality-red.csv')
  df
