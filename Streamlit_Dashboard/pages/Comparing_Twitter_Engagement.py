# importing data
import requests
import json
import pandas as pd
from pathlib import Path
import seaborn as sns
import hvplot.pandas
from pathlib import Path
import streamlit as st
import matplotlib.pyplot as plt

# Creating a heading:

st.markdown("# Comparing Twitter Engagement")

# Creating text:

st.write("""For this section of the project, we have created 
visualisations to show the correlations between the different 
kinds of Twitter engagement: posts, likes, impressions (or views)
and retweets with the changes in the price of the top 200 trending 
tickers.""")

# subtracting CSV file from desktop through jupyter notebook
csvpath = Path("../Engagement_Resources/Tweeter Engagement Data.csv")
tweeter_df = pd.read_csv(csvpath)

# dropping extra columns that are irrelevant to our analysis
tweeter_df = tweeter_df.drop(columns = ["Unnamed: 0", "lastPosts",
"lastLikes","lastImpressions","rank","lastRetweets","price","change",
"volume","previousClose"])

# setting ticker symbol as Dataframe index
tweeter_df = tweeter_df.set_index("ticker")

# re-ordering columns
tweeter_df = tweeter_df[["name","marketCap","posts","likes","impressions",
"retweets","changePercent"]]

# sorting data in highest to lowest order base off price change in percentage
tweeter_df = tweeter_df.sort_values("changePercent", ascending = False)

# correlation matrix
price_corelation = tweeter_df.corr()

# plotting the heatmap to the dashboard
fig, ax = plt.subplots()
sns.heatmap(price_corelation, vmin = -1, vmax = 1, ax = ax)
st.write(fig)

# ploting data to anlayst the price impact from each tweeter engagement

fig, ax = plt.subplots()
tweeter_df.plot(kind='scatter', x='changePercent', y='posts', 
title = 'Effect of "twitter posts" on the price', ax = ax)
st.write(fig)

fig, ax = plt.subplots()
tweeter_df.plot(kind='scatter', x='changePercent', y='likes', 
title = 'Effect of "twitter likes" on the price', ax = ax)
st.write(fig)

fig, ax = plt.subplots()
impressions_corr_plot = tweeter_df.plot (kind='scatter', x='changePercent', y='impressions', 
title = 'Effect of "twitter impressions" on the price', ax = ax)
st.write(fig)

fig, ax = plt.subplots()
tweeter_df.plot(kind='scatter', x='changePercent', y='retweets', 
title = 'Effect of "twitter retweets" on the price', ax = ax)
st.write(fig)

st.write("""Comparing scatter plots on each kind of twitter engagement, we can 
see that it is difficult to confirm there is a very strong correlation on the positive 
price movement from the volume of twitter engagement. In contrast, negative 
price movement is strongly correlated to the volume of tweeter engagement.""")







