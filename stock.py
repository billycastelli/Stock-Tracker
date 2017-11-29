import stock_api

ALL = {}

#note: add date to top

def enter_name():
    return input("Enter a stock symbol: ")

def adder(symbol = "Holder"):
    if symbol == "Holder":
        symbol = enter_name().upper()
    url = stock_api.create_url(symbol)
    #print(url)
    try:
        data = stock_api.get_data(url)
        stock_api.check_valid(data)
    except stock_api.InvalidSymbol:
        print("Invalid Stock Symbol")
        return
    parsed = stock_api.get_current_close(data)
    current = parsed[0]
    time = parsed[1][-8:]
    #print(time)
    ALL[symbol] = [current, time]
    return

def update(ALL:dict):
    for (key, value) in ALL.items():
        adder(key)
    return

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
        adder()
        update(ALL)
        display(ALL)
 
