# nasdaq5.0-parser
parse nasdaq5.0 tick data
the nasdaq5.0 itch specification can be found here: https://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/NQTVITCHSpecification.pdf
Timestamp has been converted into binary char.
to convert it to nanosecond, use int.from_bytes(b'\x1c\x8cc\xddY\xfd',byteorder='big',signed=False) 
