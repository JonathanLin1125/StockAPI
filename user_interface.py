'''
Created on May 18, 2017

@author: jonathanlin
'''

import iex_api
import stock_obj

def get_list_symbols() ->str:
    list_symbols = []
    symbol = input().strip()
    while(symbol.strip() != ""):
        list_symbols.append(symbol)
        symbol = input().strip()
    
    symbol_string = ",".join(list_symbols)
    return symbol_string

def get_list_stock_info(json_obj:"json")->list:
    list_stock_info = []
    for json in json_obj:
        stock = stock_obj.Stock()
        stock.analyze_simple(json)
        list_stock_info.append(stock)
    return list_stock_info

def print_stock_list(list_stock_info:list):
    for stock_info in list_stock_info:
        stock_info.print_all()
        print()

if __name__ == "__main__":
    symbol_string = get_list_symbols()
    
    
    json_obj = iex_api.return_json_simple(symbol_string)
    
    list_stock_info = get_list_stock_info(json_obj)
    
    print_stock_list(list_stock_info)