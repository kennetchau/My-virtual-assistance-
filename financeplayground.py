import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader as web
import pickle
import requests
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import generalfunction as gf

style.use('ggplot')
yf.pdr_override()

## function to get all ticket of s&p 500
def save_tickers(link,filename,row):
    if not os.path.exists('ticker/'):
        os.makedirs('ticker/')
    idx = int(row)
    resp = requests.get(link) #getting s&p 500 list from wikipedia
    soup = bs.BeautifulSoup(resp.text,"lxml")
    table = soup.find('table',{'id':'constituents'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[idx].text.strip()
        mapping = str.maketrans('.', '-')
        ticker = ticker.translate(mapping)
        tickers.append(ticker)
    filenames = 'ticker/{}'.format(filename)
    with open(filenames,"wb") as f:
        pickle.dump(tickers,f)
    return tickers

## function to get all s&p 500 data from yahoo
def get_data_from_yahoo(input,link,filename,filepath,row):
    if input =='y':
        tickers = save_tickers(link,filename,row)
    else:
        with open(filename,"rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    start = dt.datetime(2000,1,1)
    end = dt.datetime.now()

    for ticker in tickers:
            df = web.DataReader(ticker,'yahoo',start,end)
            df.to_csv('{}/{}.csv'.format(filepath,ticker))
            print('{} downloaded'.format(ticker))

#Combine all stock adj close into 1 dataframe
def compile_data(filename,filepath):
    fileloc = 'ticker/{}'.format(filename)
    with open(fileloc,'rb') as f:
        tickers = pickle.load(f)
    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        df = pd.read_csv('{}/{}.csv'.format(filepath,ticker))
        df.set_index('Date',inplace = True)
        df.rename(columns={'Adj Close': ticker},inplace = True)
        df.drop(['Open','High','Low','Close','Volume'],1,inplace =True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df,how='outer')

        if count%10 == 0:
            print(count)

    if not os.path.exists('joined_closed'):
        os.makedirs('joined_closed')
    print(main_df.head())
    main_df.to_csv('joined_closed/{}_joined_closed.csv'.format(filename))

def visualize_data(filename):
    if not os.path.exists('corr'):
        os.makedirs('corr')
    cfilepath = 'joined_closed/{}'.format(filename)
    df = pd.read_csv(cfilepath)
    df_corr = df.corr()
    df_corr.to_csv('corr/{}_corr.csv'.format(filename))
    print(df_corr.head())
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn) #RdYlGn is Red, Yellow, Green (Which mean show the range from red to green)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False) #setting ticks
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation = 90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()

def get_index():
    str = ''
    index = gf.getnumber(
        "Which index do you want to compare?\n1) S&P \n2) NASDAQ \n3) Dows Jones\n4) Hang Seng index\n5) Euronext 100\n6) S&P TSX ")
    if index == 1:
        str = '^GSPC'
    if index == 2:
        str = '^IXIC'
    if index == 3:
        str = '^DJI'
    #if index == 4:
        #str = '^SSEC'
    if index == 4:
        str = '^HSI'
    #if index == 6:
       # str = '^FTSE 100'
    if index == 5:
        str = '^N100'
    if index == 6:
        str = '^GSPTSE'
    return str

#visualize_data()
