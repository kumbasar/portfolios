#!/usr/bin/env python3

import investpy
import datetime
import json
from numpy.core.numeric import True_
import pandas as pd
import matplotlib.pyplot as plt

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
                                                from_date=stk['date'],
                                                to_date=today)

        stk_mean = df["Close"].mean()
        stk_max = df["Close"].max()
        stk_min = df["Close"].min()
        df_temp = pd.concat([df.head(1), df.tail(1)])

        print("\n******\n{}\n".format(stk['code']))
        print("Cost: {} TRY".format(stk['price']))
        print("Mean: {} TRY".format(round(stk_mean, 2)))
        print("Max: {} TRY".format(stk_max))
        print("Min: {} TRY\n".format(stk_min))
        print(df_temp)

        ax = fig.add_subplot(count)
        df.plot(y='Close', ylabel='Price', title=stk['code'], grid=True, legend=False, ax=ax)
        count += 1

    plt.show()
