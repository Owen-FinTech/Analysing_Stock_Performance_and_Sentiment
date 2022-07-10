# Importing the necessary libraries:

import streamlit as st
import requests
import json
import pandas as pd
import holoviews as hv
import hvplot.pandas
from pathlib import Path

# Creating a page title:

st.markdown("# Comparing Timeframes Part 2")

# Creating text:

st.write("""For this second part I will be examining 
the same  24hr, 72hr, 1 week, 2 week, 1 month and 3 month 
timeframes but instead of dividing the tickers into quartiles 
I will be filtering out the non-trending tickers.""")

# Accessing the csv and reading it into the dataframe:

tickers_data = Path('/app/project_1/Timeframes_Resources/tickers.csv')
dataframe_tickers = pd.read_csv(tickers_data)

# Setting index as "ticker":

dataframe_tickers = dataframe_tickers.set_index("ticker")

# Accessing the csv and reading it into the dataframe:

bull_24h_data = Path('./app/project_1/Timeframes_Resources/bull_24h.csv')
dataframe_bull_24h = pd.read_csv(bull_24h_data)

# Setting index as "ticker":

dataframe_bull_24h = dataframe_bull_24h.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bull_24h_trend = pd.concat([dataframe_bull_24h, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bull_24h_trend = dataframe_bull_24h_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bull_24h_trend = correlation_matrix_bull_24h_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_72h_data = Path('./app/project_1/Timeframes_Resources/bull_72h.csv')
dataframe_bull_72h = pd.read_csv(bull_72h_data)

# Setting index as "ticker":

dataframe_bull_72h = dataframe_bull_72h.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bull_72h_trend = pd.concat([dataframe_bull_72h, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bull_72h_trend = dataframe_bull_72h_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bull_72h_trend = correlation_matrix_bull_72h_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_1w_data = Path('/app/project_1/Timeframes_Resources/bull_1w.csv')
dataframe_bull_1w = pd.read_csv(bull_1w_data)

# Setting index as "ticker":

dataframe_bull_1w = dataframe_bull_1w.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bull_1w_trend = pd.concat([dataframe_bull_1w, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bull_1w_trend = dataframe_bull_1w_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1w_trend = correlation_matrix_bull_1w_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_2w_data = Path('/app/project_1/Timeframes_Resources/bull_2w.csv')
dataframe_bull_2w = pd.read_csv(bull_2w_data)

# Setting index as "ticker":

dataframe_bull_2w = dataframe_bull_2w.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bull_2w_trend = pd.concat([dataframe_bull_2w, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bull_2w_trend = dataframe_bull_2w_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bull_2w_trend = correlation_matrix_bull_2w_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_1m_data = Path('/app/project_1/Timeframes_Resources/bull_1m.csv')
dataframe_bull_1m = pd.read_csv(bull_1m_data)

# Setting index as "ticker":

dataframe_bull_1m = dataframe_bull_1m.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bull_1m_trend = pd.concat([dataframe_bull_1m, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bull_1m_trend = dataframe_bull_1m_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1m_trend = correlation_matrix_bull_1m_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_3m_data = Path('/app/project_1/Timeframes_Resources/bull_3m.csv')
dataframe_bull_3m = pd.read_csv(bull_3m_data)

# Setting index as "ticker":

dataframe_bull_3m = dataframe_bull_3m.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bull_3m_trend = pd.concat([dataframe_bull_3m, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bull_3m_trend = dataframe_bull_3m_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bull_3m_trend = correlation_matrix_bull_3m_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_24h_data = Path('/app/project_1/Timeframes_Resources/bear_24h.csv')
dataframe_bear_24h = pd.read_csv(bear_24h_data)

# Setting index as "ticker":

dataframe_bear_24h = dataframe_bear_24h.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bear_24h_trend = pd.concat([dataframe_bear_24h, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bear_24h_trend = dataframe_bear_24h_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bear_24h_trend = correlation_matrix_bear_24h_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_72h_data = Path('./app/project_1/Timeframes_Resources/bear_72h.csv')
dataframe_bear_72h = pd.read_csv(bear_72h_data)

# Setting index as "ticker":

dataframe_bear_72h = dataframe_bear_72h.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bear_72h_trend = pd.concat([dataframe_bear_72h, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bear_72h_trend = dataframe_bear_72h_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bear_72h_trend = correlation_matrix_bear_72h_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_1w_data = Path('/app/project_1/Timeframes_Resources/bear_1w.csv')
dataframe_bear_1w = pd.read_csv(bear_1w_data)

# Setting index as "ticker":

dataframe_bear_1w = dataframe_bear_1w.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bear_1w_trend = pd.concat([dataframe_bear_1w, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bear_1w_trend = dataframe_bear_1w_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1w_trend = correlation_matrix_bear_1w_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_2w_data = Path('/app/project_1/Timeframes_Resources/bear_2w.csv')
dataframe_bear_2w = pd.read_csv(bear_2w_data)

# Setting index as "ticker":

dataframe_bear_2w = dataframe_bear_2w.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bear_2w_trend = pd.concat([dataframe_bear_2w, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bear_2w_trend = dataframe_bear_2w_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bear_2w_trend = correlation_matrix_bear_2w_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_1m_data = Path('/app/project_1/Timeframes_Resources/bear_1m.csv')
dataframe_bear_1m = pd.read_csv(bear_1m_data)

# Setting index as "ticker":

dataframe_bear_1m = dataframe_bear_1m.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bear_1m_trend = pd.concat([dataframe_bear_1m, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bear_1m_trend = dataframe_bear_1m_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1m_trend = correlation_matrix_bear_1m_trend["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_3m_data = Path('/app/project_1/Timeframes_Resources/bear_3m.csv')
dataframe_bear_3m = pd.read_csv(bear_3m_data)

# Setting index as "ticker":

dataframe_bear_3m = dataframe_bear_3m.set_index("ticker")

# Concatenating top 200 by inner join with top trending so as to drop non-trending tickers:
dataframe_bear_3m_trend = pd.concat([dataframe_bear_3m, dataframe_tickers], 
    axis = "columns", join = "inner")

# Creating a correlation matrix:

correlation_matrix_bear_3m_trend = dataframe_bear_3m_trend.corr()

# Isolating the final figure I will use in visualisations:

corr_bear_3m_trend = correlation_matrix_bear_3m_trend["price change percent"][0]

# Creating a list for the indexes:

timeframes = ["24hr", "72hr", "1 week", "2 weeks", "1 month", "3 months"] 

# Creating a list of the correlations

bullish_sentiment_and_trending = [corr_bull_24h_trend, corr_bull_72h_trend,
                                  corr_bull_1w_trend, corr_bull_2w_trend,
                                  corr_bull_1m_trend, corr_bull_3m_trend]

# Setting the data into a dataframe:

bullish_sentiment_and_trending_df = pd.DataFrame(data = bullish_sentiment_and_trending,
    index = timeframes, columns = ["correlation"])

# Creating a list of the correlations

bearish_sentiment_and_trending = [corr_bear_24h_trend, corr_bear_72h_trend,
                                  corr_bear_1w_trend, corr_bear_2w_trend,
                                  corr_bear_1m_trend, corr_bear_3m_trend]

# Setting the data into a dataframe:

bearish_sentiment_and_trending_df = pd.DataFrame(data = bearish_sentiment_and_trending,
    index = timeframes, columns = ["correlation"])

# Formatting the bullish line plot:

bullish_sentiment_and_trending_plot = bullish_sentiment_and_trending_df.hvplot.line(
    x = "timeframes", y = "correlation", height = 400, width = 800, xlabel = "Timeframes", 
    label = "Bullish", 
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Timeframes for Most Bullish and Bearish Trending Tickers")

# Formatting the bearish line plot:

bearish_sentiment_and_trending_plot = bearish_sentiment_and_trending_df.hvplot.line(
    x = "timeframes", y = "correlation", height = 400, width = 800, xlabel = "Timeframes", 
    label = "Bearish", 
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Timeframes for Most Bullish and Bearish Trending Tickers")

# Combining the plots:

combined_sentiment_and_trending_plot = (bullish_sentiment_and_trending_plot *
    bearish_sentiment_and_trending_plot)

# Plotting to streamlit dashboard:

st.bokeh_chart(hv.render(combined_sentiment_and_trending_plot))

st.write("""This plot provides greater opportunity to draw conclusions 
than the busy plots created in part 1. We can see that for all the 
different timeframes plotted, bearish sentiment had a higher correlation 
than bullish sentiment. We can see this peaking at the 2 weeks timeframe, 
so that would be the optimal span of time for sentiment data collection.""")









































































































