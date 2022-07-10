import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path
import itertools as it

#matplotlib
import matplotlib.pyplot as plt

# Import the hvPlot library
import hvplot.pandas

# Vader Sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(snt)))


# This is the body of the sentiment analysis

header = st.container()
hypothesis = st.container()
apple_inc = st.container()
jp_morgan = st.container()
jll = st.container()




with header:
    st.title('Analysing 3 blue chip stocks in different industries against media sentiment')
    st.write('For this project, 3 blue chip stocks were analysed over the period of a month. The project was to assessed if sentiment analysis could play a pivotal role in forecasting stock activity. Initially the data was')

with hypothesis: 
    st.header('Hypothesis')
    st.write('Sentiment from media does not create stock volatility for blue-chip stocks, and should not be used as a driver to predict movements.')
    st.subheader('So how did we approach this analysis? ')
    st.write('During this section of the analysis, blue-chip stocks were isolated against newsfeed. The newsfeed was source from NewsAPI, where it provided 30-days of searches for free.')
    st.write('VADER Sentiment Analysis was used to analyse the newsfeed. VADER = Valence Aware Dictionary and sEntiment Reasoner is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains.')

with apple_inc:
    st.header('Apple Inc')

    st.subheader('Trade volumes over a 30-day period')
    # Read CSV files and prepare DF for volume
    Compare_volume_AAPL = Path("../Blue_Chip_Resources/Streamlit/Compare_Vol_AAPL.csv")
    Compare_volume_AAPL_df = pd.read_csv(Compare_volume_AAPL)
    Compare_volume_AAPL_df.set_index(pd.to_datetime(Compare_volume_AAPL_df['Date'], infer_datetime_format=True), inplace=True)
    Compare_volume_AAPL_df.drop(columns=['Date'], inplace=True)    
    st.line_chart(Compare_volume_AAPL_df)

    st.subheader('Sentiment Analysis and Newsfeed Count')
    # Access the CSV and rename the columns
    AAPL_news = Path ('../Blue_Chip_Resources/Streamlit/AAPL.csv')
    AAPL_news_df = pd.read_csv(AAPL_news)
    AAPL_news_df1 = AAPL_news_df.rename(columns={'publishedAt': 'Date', 'title': 'Title'})

    # Need to convert the date time into dates so it can be sortby
    AAPL_news_df1["Date"] = AAPL_news_df1["Date"].str.replace("T", " ", regex=True).str.replace("Z", "", regex=True).astype(str)
    AAPL_news_df1['Date'] = pd.to_datetime(AAPL_news_df1['Date']).dt.strftime('%d/%m/%Y')
    AAPL_news_df1.head()

    # Remove irrelevant columns and set the 'publishedAt' as the index
    AAPL_news_df1.set_index(pd.to_datetime(AAPL_news_df1['Date'], infer_datetime_format=True), inplace=True)
    AAPL_news_df1.drop(columns=['Date', 'status', 'Unnamed: 0', 'totalResults', 'source', 'author', 'url', 'urlToImage', 'description', 'content'], inplace=True)

    # Sentiment analysis: AAPL 
    AAPL_news_df1['Neg'] = AAPL_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['neg'])
    AAPL_news_df1['Neu'] = AAPL_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['neu'])
    AAPL_news_df1['Pos'] = AAPL_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['pos'])
    AAPL_news_df1['Compound'] = AAPL_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['compound'])

    # Groupby index (date)
    AAPL_news_df_grp = AAPL_news_df1.groupby('Date')['Compound'].describe()
    
    # Drop columns to create a better plot
    AAPL_news_df_grp.drop(columns=['std','min','25%','50%','75%','max'], inplace=True)

    # Display line chart of the count and mean sentiment
    st.line_chart(AAPL_news_df_grp)

    st.subheader('Summary of findings from analysing Apple Inc')
    st.write('There was no correlation in trading volumes and the newsfeed sentiments for Apple. While there was a significant amount of newsfeeds for the period, reaching a count of 17 newsfeed globally on 06 June 2022, the volume of trade days was one of the lowest for the period.')

with jp_morgan: 
    st.header('JP Morgan')
    st.write('Media feeds collected from NewsAPI for the previous 30-days.')

    st.subheader('Trade volumes over a 30-day period')
    # Read CSV files and prepare DF
    Compare_volume_AMJ = Path("../Blue_Chip_Resources/Streamlit/Compare_Vol_AMJ.csv")
    Compare_volume_AMJ_df = pd.read_csv(Compare_volume_AMJ)
    Compare_volume_AMJ_df.set_index(pd.to_datetime(Compare_volume_AMJ_df['Date'], infer_datetime_format=True), inplace=True)
    Compare_volume_AMJ_df.drop(columns=['Date'], inplace=True)    
    st.line_chart(Compare_volume_AMJ_df)

    st.subheader('Sentiment Analysis and Newsfeed Count')
    # Access the CSV and rename the columns
    AMJ_news = Path ('../Blue_Chip_Resources/Streamlit/AMJ.csv')
    AMJ_news_df = pd.read_csv(AMJ_news)
    AMJ_news_df1 = AMJ_news_df.rename(columns={'publishedAt': 'Date', 'title': 'Title'})

    # Need to convert the date time into dates so it can be sortby
    AMJ_news_df1["Date"] = AMJ_news_df1["Date"].str.replace("T", " ", regex=True).str.replace("Z", "", regex=True).astype(str)
    AMJ_news_df1['Date'] = pd.to_datetime(AMJ_news_df1['Date']).dt.strftime('%d/%m/%Y')

    # Remove irrelevant columns and set the 'publishedAt' as the index
    AMJ_news_df1.set_index(pd.to_datetime(AMJ_news_df1['Date'], infer_datetime_format=True), inplace=True)
    AMJ_news_df1.drop(columns=['Date', 'status', 'Unnamed: 0', 'totalResults', 'source', 'author', 'url', 'urlToImage', 'description', 'content'], inplace=True)
    
    #Sentiment analysis
    AMJ_news_df1['Neg'] = AMJ_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['neg'])
    AMJ_news_df1['Neu'] = AMJ_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['neu'])
    AMJ_news_df1['Pos'] = AMJ_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['pos'])
    AMJ_news_df1['Compound'] = AMJ_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['compound'])

    # Groupby index (date)
    AMJ_news_df_grp = AMJ_news_df1.groupby('Date')['Compound'].describe()

    # Drop columns to create a better plot
    AMJ_news_df_grp.drop(columns=['std','min','25%','50%','75%','max'], inplace=True)

    # Display line chart of the count and mean sentiment
    st.line_chart(AMJ_news_df_grp)

with jll: 
    st.header('Jones Lang Lasalle')
    st.write('Media feeds collected from NewsAPI for the previous 30-days.')

    st.subheader('Trade volumes over a 30-day period')
    # Read CSV files and prepare DF
    Compare_volume_JLL = Path("../Blue_Chip_Resources/Streamlit/Compare_Vol_JLL.csv")
    Compare_volume_JLL_df = pd.read_csv(Compare_volume_JLL)
    Compare_volume_JLL_df.set_index(pd.to_datetime(Compare_volume_JLL_df['Date'], infer_datetime_format=True), inplace=True)
    Compare_volume_JLL_df.drop(columns=['Date'], inplace=True)    
    st.line_chart(Compare_volume_JLL_df)

    st.subheader('Sentiment Analysis and Newsfeed Count')
    # Access the CSV and rename the columns
    JLL_news = Path ('../Blue_Chip_Resources/Streamlit/JLL.csv')
    JLL_news_df = pd.read_csv(JLL_news)
    JLL_news_df1 = JLL_news_df.rename(columns={'publishedAt': 'Date', 'title': 'Title'})

    # Need to convert the date time into dates so it can be sortby
    JLL_news_df1["Date"] = JLL_news_df1["Date"].str.replace("T", " ", regex=True).str.replace("Z", "", regex=True).astype(str)
    JLL_news_df1['Date'] = pd.to_datetime(JLL_news_df1['Date']).dt.strftime('%d/%m/%Y')

    # Remove irrelevant columns and set the 'publishedAt' as the index
    JLL_news_df1.set_index(pd.to_datetime(JLL_news_df1['Date'], infer_datetime_format=True), inplace=True)
    JLL_news_df1.drop(columns=['Date', 'status', 'Unnamed: 0', 'totalResults', 'source', 'author', 'url', 'urlToImage', 'description', 'content'], inplace=True)

    # Sentiment analysis
    JLL_news_df1['Neg'] = JLL_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['neg'])
    JLL_news_df1['Neu'] = JLL_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['neu'])
    JLL_news_df1['Pos'] = JLL_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['pos'])
    JLL_news_df1['Compound'] = JLL_news_df1['Title'].apply(lambda x:analyser.polarity_scores(x)['compound'])

    # Groupby index (date)
    JLL_news_df_grp = JLL_news_df1.groupby('Date')['Compound'].describe()

    # Drop columns to create a better plot
    JLL_news_df_grp.drop(columns=['std','min','25%','50%','75%','max'], inplace=True)

    # Display line chart of the count and mean sentiment
    st.line_chart(JLL_news_df_grp)










