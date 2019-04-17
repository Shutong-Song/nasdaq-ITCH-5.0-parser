import struct

def system_event_message(msg):
    msg_type = b"S";
    val = struct.unpack('!HH6sc',msg)
    val = list(val);
    return val;

def stock_directory_message(msg):
    msg_type = b'R';
    val = struct.unpack('!HH6s8sccIcc2scccccIc',msg);
    val = list(val);
    return val;

def stock_trading_action(msg):
    msg_type = b'H';
    val = struct.unpack('!HH6s8scc4s',msg);
    val = list(val);
    return val;

def short_sale_price_test(msg):
    msg_type = b'Y';
    val = struct.unpack('!HH6s8sc',msg);
    val = list(val);
    return val;

def market_participation_position(msg):
    msg_type = b'L';
    val = struct.unpack('!HH6s4s8sccc',msg);
    val = list(val);
    return val;

def mwcb_decline_level_message(msg):
    msg_type = b'V';
    val = struct.unpack('!HH6sQQQ',msg);
    val = list(val);
    val[3:] = map(float,val[3:]);
    val[3:] = map(lambda x:x/(pow(10,8)),val[3:]);
    return val;

def mwcb_status_message(msg):
    msg_type = b'W';
    val = struct.unpack('!HH6sc',msg);
    val = list(val);
    return val;

def ipo_quoting_period_update(msg):
    msg_type = b'K';
    val = struct.unpack('!HH6s8sIcL',msg);
    val = list(val);
    val[6] = float(val[6]);
    val[6] = val[6]/10000;
    return val;

def LULD_Auction_Collar(msg):
    msg_type = b'J';
    val = struct.unpack('!HH6s8sLLLI',msg);
    val = list(val);
    val[4:7] = map(float,val[4:7]);
    val[4:7] = map(lambda x:x/10000,val[4:7]);
    return val;

def Operational_Halt(msg):
    msg_type = b'h';
    val = struct.unpack('!HH6s8scc',msg);
    val = list(val);
    return val;

def add_order_message(msg):
    msg_type = b'A';
    val = struct.unpack('!HH6sQcI8sL',msg);
    val = list(val);
    val[7] = float(val[7]);
    val[7] = val[7]/10000;
    return val;

def add_order_with_mpid(msg):
    msg_type = b'F';
    val = struct.unpack('!HH6sQcI8sL4s',msg);
    val = list(val);
    val[7] = float(val[7]);
    val[7] = val[7]/10000; 
    return val;

def order_executed_message(msg):
    msg_type = b'E';
    val = struct.unpack('!HH6sQIQ',msg);
    val = list(val);
    return val;

def order_executed_price_message(msg):
    msg_type = b'C';
    val = struct.unpack('!HH6sQIQcL',msg);
    val = list(val);
    val[7] = float(val[7]);
    val[7] = val[7]/10000;  
    return val;

def order_cancel_message(msg):
    msg_type = b'X';
    val = struct.unpack('!HH6sQI',msg);
    val = list(val);
    return val;

def order_delete_message(msg):
    msg_type = b'D';
    val = struct.unpack('!HH6sQ',msg);
    val = list(val);
    return val;

def order_replace_message(msg):
    msg_type = b'U';
    val = struct.unpack('!HH6sQQIL',msg);
    val = list(val);
    val[6] = float(val[6]);
    val[6] = val[6]/10000;
    return val;

def trade_message(msg):
    msg_type = b'P';
    val = struct.unpack('!HH6sQcI8sLQ',msg);
    val = list(val);
    val[7] = float(val[7]);
    val[7] = val[7]/10000;
    return val;

def cross_trade_message(msg):
    msg_type = b'Q';
    val = struct.unpack('!HH6sQ8sLQc',msg);
    val = list(val);
    val[5] = float(val[5]);
    val[5] = val[5]/10000;
    return val;

def broken_trade_execution_message(msg):
    msg_type = b'B';
    val = struct.unpack('!HH6sQ',msg);
    val = list(val);
    return val;

def net_order_imbalance_message(msg):
    msg_type = b'I';
    val = struct.unpack('!HH6sQQc8sLLLcc',msg);
    val = list(val);
    val[7:10] = map(float,val[7:10]);
    val[7:10] = map(lambda x:x/10000,val[7:10]);
    return val;
