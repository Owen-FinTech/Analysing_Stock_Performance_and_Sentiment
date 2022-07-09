# Project_1: Analysing Stock Performance and Sentiment

![Intro Image](Images/Intro_Image.png "Analysing Stock Performance and Sentiment")

## Introduction

For this project we aimed to find out if social media sentiment, news sentiment and social media engagement have correlations with stock market price movements. Do human emotions that are  broadcast online, through text-based messages such as those on Twitter, influence the buying and selling patterns of others? Is the network effect of media amplifying market behaviours such as loss-aversion or FOMO (Fear of Missing Out)? We also wondered if analysis of this data could be incorporated into a buying and selling strategy for stock market investment.

So, what is sentiment data? Sentiment analysis (or opinion mining) is a Natural Language Processing technique (which is a field of Artificial Intelligence) used assign a score, or grading, indicating whether the sample text is positive, negative, or neutral. Although it isn’t just a tally of good and bad words, it also attempts to understand the syntax and sentence construction around those words. It allows us to view the sentiment of huge samplings of text, more than what humans could sort through individually, and find patterns around different groupings, like hashtag mentions.

In our initial research we identified the [Finance and Social Sentiment for Twitter API](https://rapidapi.com/UtradeaAPI/api/finance-social-sentiment-for-twitter-and-stocktwits/) on [rapidapi.com](https://rapidapi.com/hub) that gives a real-time feed of sentiment scores for individual tweets that mention stock market tickers. It also has feeds that group this information with changes in the stock price for up to 200 tickers across specified timeframes. We also used [News API](https://newsapi.org/) to source news headlines by stock ticker and then had those headlines analysed by [Vader Lexicon](https://www.kaggle.com/datasets/nltkdata/vader-lexicon) a lexicon and rule-based sentiment analysis tool for Python.

In order find out if there were correlations in the data, we broke the analysis into 5 main tasks:
-	Comparing Correlations in Bullish and Bearish Sentiment.
-	Comparing Correlations Across Different Timeframes.
-	Comparing Correlations Across Market Sectors.
-	Comparing Correlations Across Different Market Capitalisation. 
-	Comparing Different Kinds of Twitter Engagement. 

## Technologies
Modules and libraries required to run the Jupyter Notebook files:

Requests, Json, Pandas, Holoviews, Hvplot, Pathlib, Numpy, Seaborn, Matplotlib, and Vader Lexicon.

Follow [this link]() to view the project dashboard created with Streamlit.

## Conclusions

While we did find some small degrees of correlation between sentiment and price movement in some specific subsets of the data, the overall picture we got was that sentiment data couldn’t be consistently relied upon as an indicator of price movement. Therefore, we would not recommend that sentiment analysis be included as part of a trading strategy. One of the main problems is that the small degrees of correlation we found do not amount to causation. In other words, these sentiment scores are just as likely to be a reaction to price movement in the market than they are a predictor of that movement. Furthermore, Twitter users that include stock tickers in their hashtag mentions are a niche within the overall community of Twitter users. So, a tweet commenting on a company in general may contain valuable sentiment but unfortunately it wouldn’t be analysed by a stock sentiment API if it doesn’t also include the company ticker in the hashtag mentions.

There were topics of analysis that emerged during the project that may be worthy of further investigation. For example, we looked at news sentiment and twitter sentiment but what is the relationship between them? Can news headlines simply be categorized as highly influential tweets, for the purpose of analysis? Or do news reports precede the reactions of the public in their timing and therefore better predict the price changes than tweets? Also, would sentiment data that is collected from particularly influential or trusted Twitter users be more correlated than data that is simply collected from anyone and which potentially includes spam accounts?  
 

## The Team

Owen Harris

Omar Ismail

Asan Yusuf

Vima Chen

Douglas Tait







