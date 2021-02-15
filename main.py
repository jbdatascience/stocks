### this section represents a pipeline to return news data as a df of sentiment scores
from utilities.get_data import *
from utilities.clean_data import *
from utilities.sentiment_data import *
from utilities.run_arima import *
from utilities.prep_stock_data import *

news_df = get_news_dummies()
news_df = cleaner(news_df, 'title')
news_df = score_sentiment(news_df, 'title')

stock_df = get_stock_dummies()

# uncomment below to run arima model
# train_arima(timeseries=stock_df, time_col='t')

# split data into train, validation, and testing
train, valid, test = split_stock_data(df=stock_df, time_col='t')

# run dev against by-the-minute closing prices c and time t
train_data = train[['t', 'c']]

# develop lstm model approach #1 on train_data, then do again with scaled data
print(train_data)

# scale stock data
train_scaled, valid_scaled, test_scaled = scale_stock_data(train=train
                                                           , valid=valid
                                                           , test=test
                                                           )

###

#TODO get reddit and or twitter data for at least 1-2020 to 1-2021, more is better, if possible.

#TODO make cleaner module (for social media data)

#TODO prepare stock data for time series analysis

#TOD prepare nueral network for sentiment/stock price learning
