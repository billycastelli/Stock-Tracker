

import json
import urllib.parse
import urllib.request
import requests
import re

BASE_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&apikey=NU6YJ74M4X3U3UKP&symbol="

class InvalidSymbol(Exception):
    pass

class APIException(Exception):
    pass

def create_url(symbol: str):
    return BASE_URL + symbol


def get_data(url: str)->dict:
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        json_text = json.loads(json_text)
        return json_text
    except:
        raise APIException

    finally:
        if response != None:
            response.close()

def check_valid(data):
    pass
    

    
def get_current_close(json: dict):
    #print(type(json))
    date = json["Meta Data"]["3. Last Refreshed"]
    #print(date)
    return [json["Time Series (1min)"][date]["4. close"], date]
    
