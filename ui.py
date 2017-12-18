'''
Created on May 19, 2017

@author: jonathanlin
'''
import stock_obj
import last10k_api

if __name__ == "__main__":
    symbol = input()
    s = stock_obj.Stock(symbol)
    s.get_info("STOCK_QUOTE", "q")
    s.print_stock_quote()