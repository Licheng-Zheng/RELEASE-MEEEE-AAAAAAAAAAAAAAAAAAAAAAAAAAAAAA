from data_grabber import refresh_code

# Refreshes the stock information 
refresh_code()

stock_list = ["AAPL", "IBM", "BA"]

#  -- Below for loop adds all the stock information into one file named "big_fat_file.txt" -- #
for stock in stock_list: 
    with open(f"{stock}.txt", "r") as file: 
        for line in file: 
            if line.strip():
                if line == "timestamp,open,high,low,close,volume": 
                    continue
                else: 
                    with open("big_fat_file.txt", "a") as appended_to: 
                        appended_to.write(line)
                        print(line)