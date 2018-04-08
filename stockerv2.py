from __future__ import print_function
import datetime
import sys
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

import matplotlib.pyplot as plt
import numpy as np

from pandas_datareader.nasdaq_trader import get_nasdaq_symbols

yf.pdr_override() # <== that's all it takes :-)

# download Panel
# data2 = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")

# data = pdr.get_data_yahoo( tickers = ["SPY"],   start = "2017-01-01", end = "2017-04-30", as_panel = False, group_by = 'ticker',           auto_adjust = True,           actions = True,threads =1)

# download dataframe

now = str(sys.argv[2])
before = str(sys.argv[1])
print ("Current date and time using str method of datetime object:")
print (str(now))
print (str(before))




l = []

with open('YAH_codes.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        l.append(line)
        line = f.readline()

print(l[0])
i = 0
hash_data = {}
while i < len(l):
    data1 = pdr.get_data_yahoo(str(l[i]), start=before, end=now)

    #symbols = get_nasdaq_symbols()
    #print(symbols.ix[str(l[i])])

    #print(data1)
    

    hashr = {}
    lt = []
    for d in data1['Open']:
        lt.append(str(d))
        hashr.update({"Open":lt})

    lt = []
    for f in data1['Close']:
        lt.append(str(f))
        hashr.update({"Close":lt})

    lt = []
    for g in data1['High']:
        lt.append(str(g))
        hashr.update({"High":lt})
    
    lt = []
    for h in data1['Low']:
        lt.append(str(h))
        hashr.update({"Low":lt})
        
    lt = []
    for j in data1['Volume']:
        lt.append(str(j))
        hashr.update({"Volume":lt})

    hash_data.update({str(l[i]) : hashr})

    print(hash_data)

    i+=1


plt.plot( hash_data["SPY"]["Open"] )
plt.ylabel('Spy open price')
plt.show()
