# Importing the necessary libraries:

import streamlit as st
import requests
import json
import pandas as pd
import holoviews as hv
import hvplot.pandas
from pathlib import Path

# Creating a heading:

st.markdown("# Comparing Timeframes Part 1")

# Creating text:

st.write("""For this section of the project, we have created 
visualisations in order to see how the correlations 
between sentiment change and price change differ when data is 
collected for different lengths of time. We requested data from 
the API on 24hr, 72hr, 1 week, 2 week, 1 month and 3 month 
timeframes for both of the top 200 most bullish tickers 
(ordered by positive change in sentiment) and 
the top 200 most bearish tickers (ordered by negative change 
in sentiment).""")

# Accessing the csv and reading it into the dataframe:

bull_24h_data = Path('../Timeframes_Resources/bull_24h.csv')
dataframe_bull_24h = pd.read_csv(bull_24h_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_24h_1st_qtile = dataframe_bull_24h[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_24h_1st_qtile = correlation_matrix_bull_24h_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_24h_2nd_qtile = dataframe_bull_24h[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_24h_2nd_qtile = correlation_matrix_bull_24h_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_24h_3rd_qtile = dataframe_bull_24h[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_24h_3rd_qtile = correlation_matrix_bull_24h_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_24h_4th_qtile = dataframe_bull_24h[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_24h_4th_qtile = correlation_matrix_bull_24h_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_72h_data = Path('../Timeframes_Resources/bull_72h.csv')
dataframe_bull_72h = pd.read_csv(bull_72h_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_72h_1st_qtile = dataframe_bull_72h[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_72h_1st_qtile = correlation_matrix_bull_72h_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_72h_2nd_qtile = dataframe_bull_72h[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_72h_2nd_qtile = correlation_matrix_bull_72h_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_72h_3rd_qtile = dataframe_bull_72h[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_72h_3rd_qtile = correlation_matrix_bull_72h_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_72h_4th_qtile = dataframe_bull_72h[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_72h_4th_qtile = correlation_matrix_bull_72h_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_1w_data = Path('../Timeframes_Resources/bull_1w.csv')
dataframe_bull_1w = pd.read_csv(bull_1w_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_1w_1st_qtile = dataframe_bull_1w[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1w_1st_qtile = correlation_matrix_bull_1w_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_1w_2nd_qtile = dataframe_bull_1w[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1w_2nd_qtile = correlation_matrix_bull_1w_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_1w_3rd_qtile = dataframe_bull_1w[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1w_3rd_qtile = correlation_matrix_bull_1w_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_1w_4th_qtile = dataframe_bull_1w[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1w_4th_qtile = correlation_matrix_bull_1w_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_2w_data = Path('../Timeframes_Resources/bull_2w.csv')
dataframe_bull_2w = pd.read_csv(bull_2w_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_2w_1st_qtile = dataframe_bull_2w[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_2w_1st_qtile = correlation_matrix_bull_2w_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_2w_2nd_qtile = dataframe_bull_2w[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_2w_2nd_qtile = correlation_matrix_bull_2w_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_2w_3rd_qtile = dataframe_bull_2w[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_2w_3rd_qtile = correlation_matrix_bull_2w_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_2w_4th_qtile = dataframe_bull_2w[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_2w_4th_qtile = correlation_matrix_bull_2w_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_1m_data = Path('../Timeframes_Resources/bull_1m.csv')
dataframe_bull_1m = pd.read_csv(bull_1m_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_1m_1st_qtile = dataframe_bull_1m[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1m_1st_qtile = correlation_matrix_bull_1m_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_1m_2nd_qtile = dataframe_bull_1m[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1m_2nd_qtile = correlation_matrix_bull_1m_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_1m_3rd_qtile = dataframe_bull_1m[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1m_3rd_qtile = correlation_matrix_bull_1m_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_1m_4th_qtile = dataframe_bull_1m[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_1m_4th_qtile = correlation_matrix_bull_1m_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bull_3m_data = Path('../Timeframes_Resources/bull_3m.csv')
dataframe_bull_3m = pd.read_csv(bull_3m_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_3m_1st_qtile = dataframe_bull_3m[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_3m_1st_qtile = correlation_matrix_bull_3m_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_3m_2nd_qtile = dataframe_bull_3m[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_3m_2nd_qtile = correlation_matrix_bull_3m_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_3m_3rd_qtile = dataframe_bull_3m[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_3m_3rd_qtile = correlation_matrix_bull_3m_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bull_3m_4th_qtile = dataframe_bull_3m[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bull_3m_4th_qtile = correlation_matrix_bull_3m_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_24h_data = Path('../Timeframes_Resources/bear_24h.csv')
dataframe_bear_24h = pd.read_csv(bear_24h_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_24h_1st_qtile = dataframe_bear_24h[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_24h_1st_qtile = correlation_matrix_bear_24h_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_24h_2nd_qtile = dataframe_bear_24h[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_24h_2nd_qtile = correlation_matrix_bear_24h_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_24h_3rd_qtile = dataframe_bear_24h[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_24h_3rd_qtile = correlation_matrix_bear_24h_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_24h_4th_qtile = dataframe_bear_24h[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_24h_4th_qtile = correlation_matrix_bear_24h_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_72h_data = Path('../Timeframes_Resources/bear_72h.csv')
dataframe_bear_72h = pd.read_csv(bear_72h_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_72h_1st_qtile = dataframe_bear_72h[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_72h_1st_qtile = correlation_matrix_bear_72h_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_72h_2nd_qtile = dataframe_bear_72h[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_72h_2nd_qtile = correlation_matrix_bear_72h_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_72h_3rd_qtile = dataframe_bear_72h[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_72h_3rd_qtile = correlation_matrix_bear_72h_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_72h_4th_qtile = dataframe_bear_72h[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_72h_4th_qtile = correlation_matrix_bear_72h_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_1w_data = Path('../Timeframes_Resources/bear_1w.csv')
dataframe_bear_1w = pd.read_csv(bear_1w_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_1w_1st_qtile = dataframe_bear_1w[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1w_1st_qtile = correlation_matrix_bear_1w_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_1w_2nd_qtile = dataframe_bear_1w[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1w_2nd_qtile = correlation_matrix_bear_1w_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_1w_3rd_qtile = dataframe_bear_1w[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1w_3rd_qtile = correlation_matrix_bear_1w_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_1w_4th_qtile = dataframe_bear_1w[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1w_4th_qtile = correlation_matrix_bear_1w_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_2w_data = Path('../Timeframes_Resources/bear_2w.csv')
dataframe_bear_2w = pd.read_csv(bear_2w_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_2w_1st_qtile = dataframe_bear_2w[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_2w_1st_qtile = correlation_matrix_bear_2w_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_2w_2nd_qtile = dataframe_bear_2w[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_2w_2nd_qtile = correlation_matrix_bear_2w_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_2w_3rd_qtile = dataframe_bear_2w[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_2w_3rd_qtile = correlation_matrix_bear_2w_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_2w_4th_qtile = dataframe_bear_2w[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_2w_4th_qtile = correlation_matrix_bear_2w_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_1m_data = Path('../Timeframes_Resources/bear_1m.csv')
dataframe_bear_1m = pd.read_csv(bear_1m_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_1m_1st_qtile = dataframe_bear_1m[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1m_1st_qtile = correlation_matrix_bear_1m_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_1m_2nd_qtile = dataframe_bear_1m[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1m_2nd_qtile = correlation_matrix_bear_1m_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_1m_3rd_qtile = dataframe_bear_1m[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1m_3rd_qtile = correlation_matrix_bear_1m_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_1m_4th_qtile = dataframe_bear_1m[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_1m_4th_qtile = correlation_matrix_bear_1m_4th_qtile["price change percent"][0]

# Accessing the csv and reading it into the dataframe:

bear_3m_data = Path('../Timeframes_Resources/bear_3m.csv')
dataframe_bear_3m = pd.read_csv(bear_3m_data)

# Isolating the first 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_3m_1st_qtile = dataframe_bear_3m[0:50].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_3m_1st_qtile = correlation_matrix_bear_3m_1st_qtile["price change percent"][0]

# Isolating the second 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_3m_2nd_qtile = dataframe_bear_3m[50:100].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_3m_2nd_qtile = correlation_matrix_bear_3m_2nd_qtile["price change percent"][0]

# Isolating the third 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_3m_3rd_qtile = dataframe_bear_3m[100:150].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_3m_3rd_qtile = correlation_matrix_bear_3m_3rd_qtile["price change percent"][0]

# Isolating the fourth 50 entires ordered by 'sentiment change percent' and creating a correlation matrix:

correlation_matrix_bear_3m_4th_qtile = dataframe_bear_3m[150:200].corr()

# Isolating the final figure I will use in visualisations:

corr_bear_3m_4th_qtile = correlation_matrix_bear_3m_4th_qtile["price change percent"][0]

# Creating a list for the indexes:

timeframes = ["24hr", "72hr", "1 week", "2 weeks", "1 month", "3 months"] 

# Creating a list of the correlations

qtile_1_bull = [corr_bull_24h_1st_qtile, corr_bull_72h_1st_qtile,
                corr_bull_1w_1st_qtile, corr_bull_2w_1st_qtile,
                corr_bull_1m_1st_qtile, corr_bull_3m_1st_qtile] 

# Setting the data into a dataframe:

qtile_1_bull_df = pd.DataFrame(data = qtile_1_bull, index = timeframes, columns = ["correlation"])

# Creating a list of the correlations

qtile_2_bull = [corr_bull_24h_2nd_qtile, corr_bull_72h_2nd_qtile,
                corr_bull_1w_2nd_qtile, corr_bull_2w_2nd_qtile,
                corr_bull_1m_2nd_qtile, corr_bull_3m_2nd_qtile] 

# Setting the data into a dataframe:

qtile_2_bull_df = pd.DataFrame(data = qtile_2_bull, index = timeframes, columns = ["correlation"])

# Creating a list of the correlations

qtile_3_bull = [corr_bull_24h_3rd_qtile, corr_bull_72h_3rd_qtile,
                corr_bull_1w_3rd_qtile, corr_bull_2w_3rd_qtile,
                corr_bull_1m_3rd_qtile, corr_bull_3m_3rd_qtile] 

# Setting the data into a dataframe:

qtile_3_bull_df = pd.DataFrame(data = qtile_3_bull, index = timeframes, columns = ["correlation"])

# Creating a list of the correlations

qtile_4_bull = [corr_bull_24h_4th_qtile, corr_bull_72h_4th_qtile,
                corr_bull_1w_4th_qtile, corr_bull_2w_4th_qtile,
                corr_bull_1m_4th_qtile, corr_bull_3m_4th_qtile] 

# Setting the data into a dataframe:

qtile_4_bull_df = pd.DataFrame(data = qtile_4_bull, index = timeframes, columns = ["correlation"])

# Creating a list of the correlations

qtile_1_bear = [corr_bear_24h_1st_qtile, corr_bear_72h_1st_qtile,
                corr_bear_1w_1st_qtile, corr_bear_2w_1st_qtile,
                corr_bear_1m_1st_qtile, corr_bear_3m_1st_qtile] 

# Setting the data into a dataframe:

qtile_1_bear_df = pd.DataFrame(data = qtile_1_bear, index = timeframes, columns = ["correlation"])

# Creating a list of the correlations

qtile_2_bear = [corr_bear_24h_2nd_qtile, corr_bear_72h_2nd_qtile,
                corr_bear_1w_2nd_qtile, corr_bear_2w_2nd_qtile,
                corr_bear_1m_2nd_qtile, corr_bear_3m_2nd_qtile] 

# Setting the data into a dataframe:

qtile_2_bear_df = pd.DataFrame(data = qtile_2_bear, index = timeframes, columns = ["correlation"])

# Creating a list of the correlations

qtile_3_bear = [corr_bear_24h_3rd_qtile, corr_bear_72h_3rd_qtile,
                corr_bear_1w_3rd_qtile, corr_bear_2w_3rd_qtile,
                corr_bear_1m_3rd_qtile, corr_bear_3m_3rd_qtile] 

# Setting the data into a dataframe:

qtile_3_bear_df = pd.DataFrame(data = qtile_3_bear, index = timeframes, columns = ["correlation"])

# Creating a list of the correlations

qtile_4_bear = [corr_bear_24h_4th_qtile, corr_bear_72h_4th_qtile,
                corr_bear_1w_4th_qtile, corr_bear_2w_4th_qtile,
                corr_bear_1m_4th_qtile, corr_bear_3m_4th_qtile] 

# Setting the data into a dataframe:

qtile_4_bear_df = pd.DataFrame(data = qtile_4_bear, index = timeframes, columns = ["correlation"])


# Formatting the bullish line plots:

first_quartile_bullish = qtile_1_bull_df.hvplot.line(x = "timeframes", y = "correlation",
    height = 400, width = 800, xlabel = "Timeframes", label = "1-50 Most Bullish", 
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Different Timeframes for Top 200 Most Bullish Tickers")

second_quartile_bullish = qtile_2_bull_df.hvplot.line(x = "timeframes", y = "correlation",
    height = 400, width = 800, xlabel = "Timeframes", label = "51-100 Most Bullish",
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Different Timeframes for Top 200 Most Bullish Tickers")

third_quartile_bullish = qtile_3_bull_df.hvplot.line(x = "timeframes", y = "correlation",
    height = 400, width = 800, xlabel = "Timeframes", label = "101-150 Most Bullish",
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Different Timeframes for Top 200 Most Bullish Tickers")

fourth_quartile_bullish = qtile_4_bull_df.hvplot.line(x = "timeframes", y = "correlation",
    height = 400, width = 800, xlabel = "Timeframes", label = "151-200 Most Bullish",
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Different Timeframes for Top 200 Most Bullish Tickers")

# Combining the bullish plots:

bullish_combined = (first_quartile_bullish * second_quartile_bullish * 
    third_quartile_bullish * fourth_quartile_bullish)

# Formatting the bearish line plots:

first_quartile_bearish = qtile_1_bear_df.hvplot.line(x = "timeframes", y = "correlation",
    height = 400, width = 800, xlabel = "Timeframes", label = "1-50 Most Bearish", 
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Different Timeframes for Top 200 Most Bearish Tickers")

second_quartile_bearish = qtile_2_bear_df.hvplot.line(x = "timeframes", y = "correlation",
    height = 400, width = 800, xlabel = "Timeframes", label = "51-100 Most Bearish",
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Different Timeframes for Top 200 Most Bearish Tickers")

third_quartile_bearish = qtile_3_bear_df.hvplot.line(x = "timeframes", y = "correlation",
    height = 400, width = 800, xlabel = "Timeframes", label = "101-150 Most Bearish",
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Different Timeframes for Top 200 Most Bearish Tickers")

fourth_quartile_bearish = qtile_4_bear_df.hvplot.line(x = "timeframes", y = "correlation",
    height = 400, width = 800, xlabel = "Timeframes", label = "151-200 Most Bearish",
    ylabel = "Correlation Between Change In Sentiment and Price"
    ).opts(xticks = [(0, "24hr"), (1, "72hr"), (2, "1 week"), (3, "2 weeks"), (4, "1 month"), 
    (5, "3 months")], fontsize = {'title': 12, 'ylabel': 11, 'xlabel': 14, 'ticks': 12}, 
    title = "Correlations Across Different Timeframes for Top 200 Most Bearish Tickers")

# Combining the bearish plots:

bearish_combined = (first_quartile_bearish * second_quartile_bearish * 
    third_quartile_bearish * fourth_quartile_bearish)

# Plotting to streamlit dashboard:

st.bokeh_chart(hv.render(bullish_combined))

st.bokeh_chart(hv.render(bearish_combined))




































































































































































































































