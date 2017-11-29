import stock_api

ALL = {}

#note: add date to top

def enter_name():
    return input("Enter a stock symbol: ")

def adder():
    symbol = enter_name()
    url = stock_api.create_url(symbol)
    try:
        data = stock_api.get_data(url)
        stock_api.check_valid(data)
    except InvalidSymbol:
        print("Invalid Stock Symbol")
    parsed = stock_api.get_current_close(data)
    current = parsed[0]
    time = parsed[1][-8:]
    #print(time)
    ALL[symbol] = [current, time]
    return ALL

def update(ALL:dict):
    #takes in symbols and updates their value
    pass

def display(ALL: dict):
    print("=" * 50)
    print('{:20}{:20}{:20}'.format("STOCK SYMBOL", "PRICE", "TIME"))
    print()    
    #print(current)
    for (key,value) in ALL.items():
        print('{:20}{:20}{:20}'.format(key.upper(), value[0], value[1]))
    print("=" * 50)
       
    #print(data)
    return


    



if __name__ == "__main__":
    #add updating using time modules (update every minute)
    while True:
        ALL = adder()
        display(ALL)
 
