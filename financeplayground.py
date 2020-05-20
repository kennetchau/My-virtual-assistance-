import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader as web
import pickle
import requests
import yfinance as yf
yf.pdr_override()

## function to get all ticket of s&p 500
def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies') #getting s&p 500 list from wikipedia
    soup = bs.BeautifulSoup(resp.text,"lxml")
    table = soup.find('table',{'id':'constituents'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.find('td').text.strip()
        mapping = str.maketrans('.', '-')
        ticker = ticker.translate(mapping)
        tickers.append(ticker)
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
    return tickers

## function to get all s&p 500 data from yahoo
def get_data_from_yahoo(input):
    if input =='y':
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stocks_dfs'):
        os.makedirs('stocks_dfs')

    start = dt.datetime(2000,1,1)
    end = dt.datetime.now()

    for ticker in tickers:
            df = web.DataReader(ticker,'yahoo',start,end)
            df.to_csv('stocks_dfs/{}.csv'.format(ticker))
            print('{} downloaded'.format(ticker))

#Combine all stock adj close into 1 dataframe
def compile_data():
    with open('sp500tickers.pickle','rb') as f:
        tickers = pickle.load(f)
    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        df = pd.read_csv('stocks_dfs/{}.csv'.format(ticker))
        df.set_index('Date',inplace = True)
        df.rename(columns={'Adj Close': ticker},inplace = True)
        df.drop(['Open','High','Low','Close','Volume'],1,inplace =True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df,how='outer')

        if count%10 == 0:
            print(count)

    print(main_df.head())
    main_df.to_csv('sp500_joined_closed.csv')






