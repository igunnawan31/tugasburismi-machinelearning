import streamlit as st

st.title('Unsupervised Learning - Machine Learning')
st.info('K-Means Clustering with Wine Dataset')

df = pd.read_csv('https://raw.githubusercontent.com/igunnawan31/data/refs/heads/main/winequality-red.csv')
df
