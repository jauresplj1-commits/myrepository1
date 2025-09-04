import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('File uploader')
st.subheader('Import csv')
uploaded = st.file_uploader('Choose a CSV')

if uploaded is not None :
    df = pd.read_csv(uploaded)
    st.subheader('Dataframe')
    st.write(df)
    col1,col2 = st.columns(2)
    with col1:
        fig1 = plt.figure()
        sns.scatterplot(x='EstimatedSalary',y='Age',hue='Purchased',data=df)
        st.pyplot(fig1)
    with col2:
        fig2 = plt.figure()
        sns.histplot(x='Age',data=df)
        st.pyplot(fig2)