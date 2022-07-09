import streamlit as st
from pathlib import Path
import pandas as pd
import hvplot.pandas
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
plt.style.use('ggplot')
from matplotlib.pyplot import figure

#Access data
bullish_csv_path = Path("../Market_Cap_Resources/market cap in bullish sentiment 72h.csv")
df_bullish = pd.read_csv(bullish_csv_path)
df_bullish = df_bullish.set_index("ticker").drop(columns = ["sentiment", "lastSentiment", "price", "rank", "change", "name", "previousClose"])
df_bullish["volume change"] = (df_bullish["volume"] - df_bullish["previousVolume"])/df_bullish["previousVolume"]
df_bullish = df_bullish.rename(columns = {"sentimentChange": "sentiment change", "changePercent": "price change", "marketCap": "market cap"}).drop(columns = ["volume", "previousVolume"])

df_bull_large_cap = df_bullish.loc[df_bullish['market cap'] >= 10000000000]
df_bull_med_cap = df_bullish.loc[(df_bullish['market cap'] >= 2000000000) & (df_bullish['market cap'] < 10000000000)]
df_bull_small_cap = df_bullish.loc[df_bullish['market cap'] <= 2000000000]


corr_large_cap_bull = df_bull_large_cap.corr()
corr_med_cap_bull = df_bull_med_cap.corr()
corr_small_cap_bull = df_bull_small_cap.corr()

#put on Streamlit dashboard
st.markdown("# Market Cap Correlation")
st.write("""Across different size of market capitalizations, we will analyze if there is any correlation 
between sentiment change and market cap. For my dataset, I used the 200 companies with the most bullish 
and most bearish sentiment changes in the last 72 hours, since 72 hours is a reasonable time period for 
investors to absorb information and take action in the market. The correlation analysis will be examined 
respectively for large-cap (market cap > 10 billion), medium-cap (market cap between 2 billion and 10 billion) 
and small-cap (market cap < 2 billion). This allows us to investigate the relationship between social media 
sentiment and share price fluctuation in various contexts.""")

st.subheader("Correlation Comparison for Different Market Caps in Bullish Sentiment")

#Heatmap matrix
fig, ax = plt.subplots()
plt.title("Large Cap")
sns.heatmap(corr_large_cap_bull, annot = True, ax = ax)
st.write(fig)

fig, ax = plt.subplots()
plt.title("Medium Cap")
sns.heatmap(corr_med_cap_bull, annot = True, ax = ax)
st.write(fig)

fig, ax = plt.subplots()
plt.title("Small Cap")
sns.heatmap(corr_small_cap_bull, annot = True, ax = ax)
st.write(fig)


st.subheader("Findings")

st.write("""
By comparing the three market cap correlation vs bullish sentiment matrix, we found that the correlations across all three markets are all very weak. 

Med cap stocks are relatively more sensitive to sentiment changes. In medium cap market, price is more sensitive to sentiment change comparing to volume. 
The positive sentiment change gave a little push to the stock prices in med cap market. Most of the med cap companies didn't act efficiently with the 
sentiment change, there are only a few stocks had dramatic change in price and volume, which means the social media sentiment influence more in an individual 
stocks than the whole market. 
""")