# NSADAQ ITCH 5.0 data parser
It parses NASDAQ data with ITCH 5.0 protocol into readable format

# Motivation: 
a research project to build GUI for stock price trading and visualization

# How to use:
1. Run from terminal: python3 nasdaq50-parser.py
2. It will require you to input the path of nasdaq itch data file
3. Once you input the correct path, it will read the file byte by byte till the end of file
4. By default, all other messages are disabled, only the "Add Order – No MPID Attribution" message will be processed and printed out; if you want to process and print all messages, uncomment the lines in "parse_ITCH_data" function
5. The printed information are in a list with the length equals to one less than the number of variables under that message type. For example, in "Add Order – No MPID Attribution" message, there are 9 variables: "message type", "stock locate", "tracking number", "timestamp", "order reference number", "buy/sell indicator", "shares", "stock", and "price". The printed each list will have 8 elements ("message type" is dropped out). 

# NSADAQ ITCH 5.0 specification:
https://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/NQTVITCHSpecification.pdf


# Note:
the printed timestamp has been converted into binary char, to convert it to timestamp in nanosecond, use function "int.from_bytes(your_binray_char, byteorder="big", signed=False). For example, if the timestamp is "b'\r\x18\xe5\xb8.h'", int.from_bytes(b'\r\x18\xe5\xb8.h',byteorder='big',signed=False) will give 14400584429160 nanoseconds, you can convert to hour by 14400584429160/(1e9*60*60) which is about 4 AM. 
