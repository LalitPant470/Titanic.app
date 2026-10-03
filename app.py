import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
st.title("Titanic Data Analysis")
df=sns.load_dataset("titanic")
#print(df.head())
fig, ax=plt.subplots(figsize=(10,6))
sns.countplot(data=df,x='class', hue='survived',ax=ax)
st.pyplot(fig)

