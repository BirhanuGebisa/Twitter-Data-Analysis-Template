#python library
import pandas as pd
import numpy as np
import streamlit as st


st.write("""
#sentimentall Analysis of Twitter dataset
# using Streamlit
""")
tweet_df=pd.read_csv("../data/clean_processed_tweet.csv")
st.line_chart(tweet_df)