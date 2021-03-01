import gzip
import struct
from itch_factory import *


def parse_ITCH_data(path):
    with gzip.open(path,"rb") as bin_data:
        message_type = bin_data.read(1)
        i = 0
        while message_type:
            if message_type == b"S":
                message = bin_data.read(11);
                parsed_data = system_event_message(message);
                #print(parsed_data)
                
            elif message_type == b"R":
                message = bin_data.read(38);
                #parsed_data = stock_directory_message(message);
                #print(parsed_data)
               
            elif message_type == b"H":
                message = bin_data.read(24);
                #parsed_data = stock_trading_action(message);
                #print(parsed_data)
              
            elif message_type == b"Y":
                message = bin_data.read(19);
                #parsed_data = short_sale_price_test(message);
                #print(parsed_data)
             
            elif message_type == b"L":
                message = bin_data.read(25);
                #parsed_data = market_participation_position(message);
                #print(parsed_data)
            
            elif message_type == b"V":
                message = bin_data.read(34);
                #parsed_data = mwcb_decline_level_message(message);
                #print(parsed_data)
           
            elif message_type == b"W":
                message = bin_data.read(11);
                #parsed_data = mwcb_status_message(message);
                #print(parsed_data)
          
            elif message_type == b"K":
                message = bin_data.read(27);
                #parsed_data = ipo_quoting_period_update(message);
                #print(parsed_data)
         
            elif message_type == b"J":
                message = bin_data.read(34);
                #parsed_data = LULD_Auction_Collar(message);
                #print(parsed_data)
        
            elif message_type == b"h":
                message = bin_data.read(20);
                #parsed_data = Operational_Halt(message);
                #print(parsed_data)
       
            elif message_type == b"A":
                message = bin_data.read(35);
                parsed_data = add_order_message(message);
                print(parsed_data)
      
            elif message_type == b"F":
                message = bin_data.read(39);
                #parsed_data = add_order_with_mpid(message);
                #print(parsed_data)
     
            elif message_type == b"E":
                message = bin_data.read(30);
                #parsed_data = order_executed_message(message);
                #print(parsed_data)
    
            elif message_type == b"C":
                message = bin_data.read(35);
                #parsed_data = order_executed_price_message(message);
                #print(parsed_data)
   
            elif message_type == b"X":
                message = bin_data.read(22);
                #parsed_data = order_cancel_message(message);
                #print(parsed_data)
  
            elif message_type == b"D":
                message = bin_data.read(18);
                #parsed_data = order_delete_message(message);
                #print(parsed_data)
 
            elif message_type == b"U":
                message = bin_data.read(34);
                #parsed_data = order_replace_message(message);
                #print(parsed_data)

            elif message_type == b"P":
                message = bin_data.read(43);
                #parsed_data = trade_message(message);
                #print(parsed_data)

            elif message_type == b"Q":
                message = bin_data.read(39);
                #parsed_data = cross_trade_message(message);
                #print(parsed_data)

            elif message_type == b"B":
                message = bin_data.read(18);
                #parsed_data = broken_trade_execution_message(message);
                #print(parsed_data)

            elif message_type == b"I":
                message = bin_data.read(49);
                #parsed_data = net_order_imbalance_message(message);
                #print(parsed_data)

            message_type = bin_data.read(1)
            i += 1
            if i == 100:
                break
          
if __name__ == "__main__":
    print("please enter ITCH-data file path: ")
    path = input()
    parse_ITCH_data(path)
