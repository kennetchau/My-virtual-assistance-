import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader as web
import pickle
import requests
import yfinance as yf
yf.pdr_override()


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
    print(tickers)
    return tickers


def get_data_from_yahoo(reload_sp500 = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stocks_dfs'):
        os.makedirs('stocks_dfs')

    start = dt.datetime(2000,1,1)
    end = dt.datetime.now()

    for ticker in tickers:
        if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker,'yahoo',start,end)
            df.to_csv('stocks_dfs/{}.csv'.format(ticker))
            print('{} downloaded'.format(ticker))
        else:
            print('Already have {}'.format(ticker))


