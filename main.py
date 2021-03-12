#!/usr/bin/env python3

import investpy
import datetime
import json
from numpy.core.numeric import True_
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

country = 'Turkey'
date_frmt = '%d/%m/%Y'
today = datetime.datetime.today().strftime(date_frmt)


def getStocks(stock_file='stocks.json'):
    with open(stock_file, 'r') as json_file:
        return json.load(json_file)


if __name__ == "__main__":

    conf = getStocks()

    fig = plt.figure()

    count = 211

    for stk in conf['stocks']:
        df = investpy.get_stock_historical_data(stock=stk['code'],
                                                country=conf['country'],
                                                from_date=stk['purchase_date'],
                                                to_date=today)

        stk_mean = df["Close"].mean()
        stk_max = df["Close"].max()
        stk_min = df["Close"].min()

        print("\n******\nStock Code: {}\n".format(stk['code']))
        print("{:>10} {:<5} TRY".format("Cost:", stk['price']))
        print("{:>10} {:<5} TRY".format("Current:", df['Close'].iloc[-1]))
        print("{:>10} {:<5} TRY".format("Gain:", round(df['Close'].iloc[-1]-stk['price'], 2)))
        print("{:>10} {:<5}".format("Gain %:", round(100*(df['Close'].iloc[-1]/stk['price']-1), 2)))
        print("{:>10} {:<5} TRY".format("Mean:", round(stk_mean, 2)))
        print("{:>10} {:<5} TRY".format("Max:", stk_max))
        print("{:>10} {:<5} TRY\n".format("Min:", stk_min))
        print(pd.concat([df.head(1), df.tail(1)]))

        ax = fig.add_subplot(count)
        df.plot(y='Close', ylabel='Price', title=stk['code'], grid=True, legend=False, ax=ax)
        count += 1

    plt.show()
