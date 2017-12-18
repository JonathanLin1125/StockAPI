'''
Created on May 18, 2017

@author: jonathanlin
'''
import urllib.request
import json

#https://www.iextrading.com/developer/docs/#iex-api-1-0
URL = "https://api.iextrading.com/1.0/tops/last?symbols="
IEX_KEY = "AWtLNZPkpytGvYW2Q_hw"



def return_json_simple(url_end:str)->json:
    url = URL + url_end
    http_obj = urllib.request.urlopen(url)
    json_obj = json.loads(http_obj.read().decode(encoding = "utf-8"))
    http_obj.close()
    
    return json_obj



