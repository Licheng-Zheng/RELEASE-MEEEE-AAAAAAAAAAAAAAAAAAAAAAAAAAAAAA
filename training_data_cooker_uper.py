import numpy as np 
from my_secrets import stock_list

def create(stock_ticker):
    if stock_ticker == "All":
        all_information_list = []
        
        for ticker in stock_list: 
            try: 
                file_name = f"{ticker}_data.npy"
                data = np.load(file_name)
                
                shape_of_data = data.shape
                print(shape_of_data)
                
                for actual_date in range(7, shape_of_data[0] - 30):
                    current_chunk = []
                    correct_data_compiler = []
                    
                    for future_information in range(1, 8):
                        correct_data_compiler.append(
                            data[actual_date - future_information][1]
                        )
                        correct_data_compiler.append(
                            data[actual_date - future_information][2]
                        )
                    
                    number_to_append = sum(correct_data_compiler)/len(correct_data_compiler)
                    
                    for past_information in range(1, 31):
                        current_piece = data[actual_date + past_information].tolist()
                        for piece_of_information in current_piece: 
                            current_chunk.append(piece_of_information)
                            
                    current_chunk.append(number_to_append)
                    
                    all_information_list.append(current_chunk)
                    
            except FileNotFoundError: 
                print(f"File not created yet :( go to data_grabber and grab information for {ticker}")         
    else:
        print("just use all please I don't wanna do this anymore")
        

    array_of_information = np.array(all_information_list)
    print(array_of_information[-1].shape)
    np.save(f"all_information.npy", array_of_information)
    print("List created!")
    
def create_dataset():
    # Tells the program which stocks you want to iterate over
    to_update = input(f"what information do you want refreshed? \n {" ".join(stock_list)}, All - CASE SENSITIVE BOZO\n")

    # Executes the function do_stuff, which does the stuff (it refreshes the stuff) 
    if to_update == "All": 
        create("All")
    elif to_update not in stock_list: 
        print("put something in the list please")
    else: 
        create(to_update)
    
create_dataset()
