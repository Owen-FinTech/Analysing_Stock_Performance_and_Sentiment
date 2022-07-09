# Importing necessary libraries:

import streamlit as st

# Creating page title:

st.markdown("# Conclusions")

# Creating page text:

st.write("""While we did find some small degrees of correlation between 
sentiment and price movement in some specific subsets of the data, the 
overall picture we got was that sentiment data couldn’t be consistently 
relied upon as an indicator of price movement. Therefore, we would not 
recommend that sentiment analysis be included as part of a trading strategy. 
One of the main problems is that the small degrees of correlation we found 
do not amount to causation. In other words, these sentiment scores are just 
as likely to be a reaction to price movement in the market than they are a 
predictor of that movement. Furthermore, Twitter users that include stock 
tickers in their hashtag mentions are a niche within the overall community 
of Twitter users. So, a tweet commenting on a company in general may contain 
valuable sentiment but unfortunately it wouldn’t be analysed by a stock 
sentiment API if it doesn’t also include the company ticker in the hashtag mentions.

There were topics of analysis that emerged during the project that may be 
worthy of further investigation. For example, we looked at news sentiment and 
twitter sentiment but what is the relationship between them? Can news headlines 
simply be categorized as highly influential tweets, for the purpose of analysis? 
Or do news reports precede the reactions of the public in their timing and therefore 
better predict the price changes than tweets? Also, would sentiment data that is 
collected from particularly influential or trusted Twitter users be more correlated 
than data that is simply collected from anyone and which potentially includes 
spam accounts?""")  
