import gzip
import struct
from itch-factory import *

path = r'E:\JupyterDatasets\02102019.NASDAQ_ITCH50.gz'

def open_file(path,read_format='rb'):
    bin_data = gzip.open(path, "rb")
    return bin_data

def read_binary_file(size):
    return bin_data.read(size)

message_type = bin_data.read(1);
while message_type:
    if message_type == b"S":
        message = read_binary_file(11);
        parsed_data = system_event_message(message);
        print(parsed_data)
    elif message_type == b"R":
        message = read_binary_file(38);
        parsed_data = stock_directory_message(message);
    elif message_type == b"H":
        message = read_binary_file(24);
        parsed_data = stock_trading_action(message);
        print(parsed_data)
    elif message_type == b"Y":
        message = read_binary_file(19);
        parsed_data = short_sale_price_test(message);
        print(parsed_data)
    elif message_type == b"L":
        message = read_binary_file(25);
        parsed_data = market_participation_position(message);
        print(parsed_data)
    elif message_type == b"V":
        message = read_binary_file(34);
        parsed_data = mwcb_decline_level_message(message);
        print(parsed_data)
    elif message_type == b"W":
        message = read_binary_file(11);
        parsed_data = mwcb_status_message(message);
        print(parsed_data)
    elif message_type == b"K":
        message = read_binary_file(27);
        parsed_data = ipo_quoting_period_update(message);
        print(parsed_data)
    elif message_type == b"J":
        message = read_binary_file(34);
        parsed_data = LULD_Auction_Collar(message);
    elif message_type == b"h":
        message = read_binary_file(20);
        parsed_data = Operational_Halt(message);
        print(parsed_data)
    elif message_type == b"A":
        message = read_binary_file(35);
        parsed_data = add_order_message(message);
        print(parsed_data)
    elif message_type == b"F":
        message = read_binary_file(39);
        parsed_data = add_order_with_mpid(message);
        print(parsed_data)
    elif message_type == b"E":
        message = read_binary_file(30);
        parsed_data = order_executed_message(message);
        print(parsed_data)
    elif message_type == b"C":
        message = read_binary_file(35);
        parsed_data = order_executed_price_message(message);
        print(parsed_data)
    elif message_type == b"X":
        message = read_binary_file(22);
        parsed_data = order_cancel_message(message);
        print(parsed_data)
    elif message_type == b"D":
        message = read_binary_file(18);
        parsed_data = order_delete_message(message);
        print(parsed_data)
    elif message_type == b"U":
        message = read_binary_file(34);
        parsed_data = order_replace_message(message);
        print(parsed_data)
    elif message_type == b"P":
        message = read_binary_file(43);
        parsed_data = trade_message(message);
        print(parsed_data)
    elif message_type == b"Q":
        message = read_binary_file(39);
        parsed_data = cross_trade_message(message);
        print(parsed_data)
    elif message_type == b"B":
        message = read_binary_file(18);
        parsed_data = broken_trade_execution_message(message);
        print(parsed_data)
    elif message_type == b"I":
        message = read_binary_file(49);
        parsed_data = net_order_imbalance_message(message);
        print(parsed_data)
    message_type = bin_data.read(1);
    i +=1
bin_data.close();
