# Importing necessary libraries:

import streamlit as st

# Creating main page title:

st.markdown("# Analysing Stock Performance and Social Media Sentiment")

# Creating main page text:

st.write("""For this project we aimed to find out if social media sentiment,
news sentiment and social media engagement have correlations with stock 
market price movements. Do human emotions that are  broadcast online, 
through text-based messages such as those on Twitter, influence the buying 
and selling patterns of others? Is the network effect of media amplifying 
market behaviours such as loss-aversion or FOMO (Fear of Missing Out)? 
We also wondered if analysis of this data could be incorporated into a 
buying and selling strategy for stock market investment.

So, what is sentiment data? Sentiment analysis (or opinion mining) is a 
Natural Language Processing technique (which is a field of Artificial 
Intelligence) used assign a score, or grading, indicating whether the 
sample text is positive, negative, or neutral. Although it isn’t just 
a tally of good and bad words, it also attempts to understand the syntax 
and sentence construction around those words. It allows us to view the 
sentiment of huge samplings of text, more than what humans could sort 
through individually, and find patterns around different groupings, 
like hashtag mentions. 

In our initial research we identified the 'Finance and Social Sentiment 
for Twitter API' on rapidapi.com that gives a real-time feed of sentiment 
scores for individual tweets that mention stock market tickers. It also 
has feeds that group this information with changes in the stock price 
for up to 200 tickers across specified timeframes. We also used News API 
to source headlines by stock ticker and then had those headlines analysed
by Vader Lexicon a lexicon and rule-based sentiment analysis tool for 
Python.""")

st.markdown("## The Team")

st.write("""Owen Harris

Omar Ismail

Asan Yusuf

Vima Chen

Douglas Tait""")











