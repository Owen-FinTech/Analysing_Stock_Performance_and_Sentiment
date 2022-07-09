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
bearish_csv_path = Path("../Market_Cap_Resources/market cap in bearish sentiment 72h.csv")
df_bearish = pd.read_csv(bearish_csv_path)
df_bearish.head()
df_bearish = df_bearish.set_index("ticker").drop(columns = ["sentiment", "lastSentiment", "price", "rank", "change", "name", "previousClose"])
df_bearish["volume change"] = (df_bearish["volume"] - df_bearish["previousVolume"])/df_bearish["previousVolume"]
df_bearish = df_bearish.rename(columns = {"sentimentChange": "sentiment change", "changePercent": "price change", "marketCap": "market cap"}).drop(columns = ["volume", "previousVolume"])

df_bear_large_cap = df_bearish.loc[df_bearish['market cap'] >= 10000000000]
df_bear_med_cap = df_bearish.loc[(df_bearish['market cap'] >= 2000000000) & (df_bearish['market cap'] < 10000000000)]
df_bear_small_cap = df_bearish.loc[df_bearish['market cap'] <= 2000000000]


corr_large_cap_bear = df_bear_large_cap.corr()
corr_med_cap_bear = df_bear_med_cap.corr()
corr_small_cap_bear = df_bear_small_cap.corr()



#put on Streamlit dashboard
st.subheader("Correlation Comparison for Different Market Caps in Bearish Sentiment")

#Heatmap matrix
fig, ax = plt.subplots()
plt.title("Large Cap")
sns.heatmap(corr_large_cap_bear, annot = True, ax = ax)
st.write(fig)

fig, ax = plt.subplots()
plt.title("Medium Cap")
sns.heatmap(corr_med_cap_bear, annot = True, ax = ax)
st.write(fig)

fig, ax = plt.subplots()
plt.title("Small Cap")
sns.heatmap(corr_small_cap_bear, annot = True, ax = ax)
st.write(fig)

st.subheader("Conclusion")

st.write("""
From the marix above, we can find that the large cap has stonger correlation with the negative 
sentiment change. Price decreased on increasing volume change along with the negative sentiment 
change. In bullish sentiment analysis, it shows that the large cap had a slight price decrease 
even with the positive sentiment. It is a clear sign that the investors are now at a high level of pessimism.

Over time, large-cap, med-cap, and small-cap stocks have taken turns leading the market as each 
can be affected differently by market or economic developments. That's why many investors diversify, 
maintaining a mix of market caps in their portfolios. When large caps are declining in value, small 
caps or med caps may be on the way up and could potentially help compensate for any losses.

To build a portfolio with a proper mix of small-cap, med-cap, and large-cap stocks, you'll need to 
evaluate your financial goals, risk tolerance, and time horizon. A diversified portfolio that contains 
a variety of market caps may help reduce investment risk in any one area and support the pursuit of 
your long-term financial goals.

However, the correlations with the three markets are all very weak. Analysis of market cap correlation 
does not suffice as a determining factor in investment strategy. Obviously, it's better to use sentiment 
analysis when we evaluate a specific stock or industry.
""")
