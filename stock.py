import stock_api

ALL = {}

#note: add date to top

def enter_name():
    return input("Enter a stock symbol (press enter to end program): ")

def adder(symbol = "Holder"):
    # "holder" is a placeholder
    if symbol == "Holder":
        symbol = enter_name().upper()
    if symbol == "":
        toFile()
        #return
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

def fromFile():
    response = input("Read stocks from file? (y/n) ")
    if response[0].lower() == 'y':
        fileName = input("Enter file name: ")
        try:
            file = open(fileName)
        except:
            print("File not found")
            return
        print("Loading...")
        for symbol in file:
            adder(symbol.strip())
        display(ALL)
    else:
        print("Starting program...")
        return
    return

def toFile():
    response = input("Would you like to save this session's symbols? ")
    fileName = input("Enter file name: ")
    if response[0].lower() == 'y':
        file = open(fileName, 'w')
        for (key,value) in ALL.items():
            file.write(key + '\n')
        file.close()
    print("Symbols saved as symbolsFile.txt")
    print("Ending program...")
    exit()

if __name__ == "__main__":
    #add updating using time modules (update every minute)
    fromFile()
    while True:
        adder()
        update(ALL)
        display(ALL)

#load from last session vs. load from file
    
 
