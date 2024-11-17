import requests
from my_secrets import api_key, stock_list
import numpy as np

def do_stuff(stock_ticker):
    if stock_ticker == "All":
        return

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&outputsize=full&apikey={api_key}'

    r = requests.get(url)
    
    json_data = r.json()
    usable_data = json_data["Time Series (Daily)"]
    
    # Creates a list with all the dates for which there has been data collected 
    all_keys = list(usable_data.keys())
    
    data_list  = []

    for key in all_keys:    
        data = usable_data[key]
        
        data_list.append([
            float(data["1. open"]),
            float(data["2. high"]),
            float(data["3. low"]),
            float(data["4. close"]),
            int(data["5. volume"])
        ])
        
    array = np.array(data_list)

    np.save(f"{stock_ticker}_data.npy", array)
    print(array)
    print("grabbed!")

def refresh_code():
    # I'm gonna do the stocks Apple (AAPL), IBM (IBM) and Boeing (BA), I could do more, but its 12:37 AM so I do not want to do more :D (might need to look at more stocks so I can get their stock information)

    # Tells the program which stocks you want to iterate over
    to_update = input(f"what information do you want refreshed? \n {" ".join(stock_list)}, All - CASE SENSITIVE BOZO\n")

    # Executes the function do_stuff, which does the stuff (it refreshes the stuff) 
    if to_update == "All":
        for item in stock_list: 
            do_stuff(item)
    elif to_update not in stock_list: 
        print("put something in the list please")
    else: 
        do_stuff(to_update)

refresh_code()