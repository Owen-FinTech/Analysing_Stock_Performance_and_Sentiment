# Importing all the relative libraries 

import seaborn as sns
import streamlit as st
import requests
import json
import pandas as pd
import holoviews as hv
import hvplot.pandas
from pathlib import Path

# Reading the bullish_trending csv file from local directory 
bullish_trending_df = pd.read_csv(Path('../Bullish_Bearish_Resources/bullish_trending_df.csv'))

#Dropping the unrelated columns
bullish_trending_df = bullish_trending_df.drop(columns =['Unnamed: 0','rank','price','change','volume','previousVolume',
                                                         'previousClose','name','marketCap'])

# Checking the dataframe 
bullish_trending_df.head()

# Creating new column with the sentiment change for correlation with change in price
bullish_trending_df["Sentiment Change"] = bullish_trending_df["sentiment"] - bullish_trending_df["lastSentiment"]

#Checking the dataframe
bullish_trending_df.head()

# Dropping the other columns 
bullish_trending_df = bullish_trending_df.drop(columns =['sentiment', 'lastSentiment'])

# Dropping the null
bullish_trending_df = bullish_trending_df.dropna()

#Setting the index as the ticker
bullish_trending_df = bullish_trending_df.set_index('ticker')
bullish_trending_df.head()

# Sorting the dataframe accoring to the change in price 
bullish_trending_df = bullish_trending_df.sort_values('changePercent')

#Checking for any major outlier to see if need to be dropped 
bullish_trending_df.describe()

# One major outlier that might affect the data interpretation
# Dropping the main outlier 
bullish_trending_df.drop(bullish_trending_df.tail().index,inplace=True)

# Using the hv scatter plot
bullish_trending_plot = bullish_trending_df.hvplot(x='Sentiment Change', y='changePercent', kind='scatter',
                          title='Bullish Trending Sentiment and the effect on price',
                          )


# Checking the correlation between the change in price with the change in sentiment
bullish_trending_corr = bullish_trending_df.corr()


# Using the heatmap to visualize the bullish correlation data 
# bullish_trending_heatmap = sns.heatmap(bullish_trending_corr, vmin=-1, vmax=1, cmap='PuOr', annot = True)

# Reading the bearish_trending csv file from local directory 
bearish_trending_df = pd.read_csv(Path('../Bullish_Bearish_Resources/bearish_trending_df.csv'))

#Dropping columns 

bearish_trending_df = bearish_trending_df.drop(columns =['Unnamed: 0','rank','price','change','volume','previousVolume',
                                                         'previousClose','name','marketCap'])
# Checking the dataframe 
bearish_trending_df.head()

# Creating new column with the sentiment change for correlation with change in price
bearish_trending_df["Sentiment Change"] = bearish_trending_df["sentiment"] - bearish_trending_df["lastSentiment"]

#Checking the dataframe
bearish_trending_df.head()

# Dropping the other columns 
bearish_trending_df = bearish_trending_df.drop(columns =['sentiment', 'lastSentiment'])

# Dropping the null
bearish_trending_df = bearish_trending_df.dropna()

#Setting the index as the ticker
bearish_trending_df = bearish_trending_df.set_index('ticker')
bearish_trending_df.head()

# Sorting the dataframe accoring to the change in price 
bearish_trending_df = bearish_trending_df.sort_values('changePercent')

#Checking for any major outlier to see if need to be dropped 
bearish_trending_df.describe()

# One major outlier that might affect the data interpretation
# Dropping the main outlier 
bearish_trending_df.drop(bearish_trending_df.head().index,inplace=True)

# Using the hv scatter plot
bearish_trending_plot = bearish_trending_df.hvplot(x='Sentiment Change', y='changePercent', kind='scatter',
                          title='Bearish Trending Sentiment and the effect on price',
                          )


bearish_trending_corr = bearish_trending_df.corr()
# bearish_trending_heatmap = sns.heatmap(bearish_trending_corr, vmin=-1, vmax=1, cmap='PuOr', annot = True)

bullish_bearish_sentiment_plot = bearish_trending_df.hvplot(x='Sentiment Change', y='changePercent', kind='scatter', label = ' Bullish sentiment'
                          ) * bullish_trending_df.hvplot(x='Sentiment Change', y='changePercent', kind='scatter', 
                                                         label = 'Bearish sentiment',
                          title='Bullish and Bearish Trending Sentiment and the correlation with the price',
                          )

# Streamlit dashboard

st.markdown('# Comparing Bullish and Bearish Sentiments')

st.write("In this section, we are trying to analyse and plot the top 50 tickers by bullish and bearish sentiments and their correlation with the change in price")

st.bokeh_chart(hv.render(bullish_bearish_sentiment_plot))

st.write('As we can see, in general the change in price is too small in both bullish and bearish sentiment to assume there is an actual correlation. But for comparison purposes the bearish sentiment correlates with more bearish change in price.')

