#python library
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS


st.write("""
#sentimentall Analysis of Twitter dataset
# using Streamlit
""")
data=pd.read_csv("data/clean_processed_tweet.csv")
#title
st.title('Tweet Sentiment Analysis')
#markdown
st.markdown('This application is all about tweet sentiment analysis of airlines. ')
#sidebar
st.sidebar.title('Sentiment analysis of airlines')
# sidebar markdown 
st.sidebar.markdown("Twitter review from this application.")
#loading the data (the csv file is in the same folder)
#if the file is stored the copy the path and paste in read_csv method.
#checkbox to show data 
if st.checkbox("Show Data"):
    st.write(data.head(50))
#subheader
st.sidebar.subheader('Tweets Analyser')
#radio buttons
tweets=st.sidebar.radio('Sentiment Type',('positive','negative','neutral'))
