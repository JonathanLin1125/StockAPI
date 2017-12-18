'''
Created on May 19, 2017

@author: jonathanlin
'''

import urllib.request
import json


#https://dev.last10k.com
LAST10K_KEY = "key=604b5878b836426fb30986a8d0db4492"
STOCK_QUOTE = "https://services.last10k.com/v1/company/{ticker}/quote?"
OPERATIONS = "https://services.last10k.com/v1/company/{ticker}/operations?formType=10-Q&filingOrder=0?"
INCOME = "https://services.last10k.com/v1/company/{ticker}/income?formType=10-Q&filingOrder=0?"
HISTORICAL_STOCK_PRICES = "https://services.last10k.com/v1/company/{ticker}/prices?"
CASH_FLOWS = "https://services.last10k.com/v1/company/{ticker}/cashflows?formType=10-Q&filingOrder=0?"
BALANCE_SHEET = "https://services.last10k.com/v1/company/{ticker}/balancesheet?formType=10-Q&filingOrder=0?"
"""
Too change url to search for annual report, change formType=10-Q to formType=10-K
"""

#https://services.last10k.com/v1/company/AAPL/quote

def build_url(data:str, ticker:str, time:str) ->str:
    if(data == "STOCK_QUOTE"):
        return (f"https://services.last10k.com/v1/company/{ticker}/quote?" + LAST10K_KEY)
    elif(data == "OPERATIONS"):
        return(f"ttps://services.last10k.com/v1/company/{ticker}/operations?" + LAST10K_KEY)

    
def return_json(data:str, symbol:str, time:str) ->json:
    url = build_url(data, symbol, time)
    http_obj = urllib.request.urlopen(url)
    json_obj = json.loads(http_obj.read().decode(encoding = "utf-8"))
    http_obj.close()
    return json_obj
    
        