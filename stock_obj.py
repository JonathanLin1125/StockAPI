'''
Created on May 18, 2017

@author: jonathanlin
'''
import last10k_api
LIST_STOCK_QUOTE = ["StockExchange", "PeRatio", "Name", "LastTradePrice", "YearlyHigh", "YearlyLow", "DailyHigh", "DailyLow", "EarningsShare","Change", "Symbol"]

class Stock:
    def __init__(self, symbol):
        self.list_info = {}
        self.symbol = symbol
        
    def get_info(self, option:str, time:str):
        json_obj = last10k_api.return_json(option, self.symbol, time)
        for info in json_obj.keys():
            self.list_info[info] = json_obj[info]
            
    def print_stock_quote(self):
        for info in LIST_STOCK_QUOTE:
            print(info + ": " + str(self.list_info[info]))