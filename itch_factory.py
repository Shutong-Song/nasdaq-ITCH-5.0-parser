import struct

def system_event_message(msg):
    #system event message format (total 5 variables)
    #including: message type("S"), stock locate, tracking number, timestamp, event code,
    val = struct.unpack('!HH6sc',msg)
    val = list(val);
    if len(val) == 4:
        return val
    else:
        return []

def stock_directory_message(msg):
    #stock directory format (total 17 variables)
    #including: message type("R"), stock locate, tracking number, timestamp, stock, market category,
    #           FinancialStatus indicator, round lot size, round lots only, issue classification,
    #           issue subtype, authenticity, short sale threhold indicator, IPO flag, LULDReference price tier,
    #           ETP flag, ETP leverage factor, inverse indicator
    val = struct.unpack('!HH6s8sccIcc2scccccIc',msg);
    val = list(val);
    if len(val) == 16:
        return val
    else:
        return []

def stock_trading_action(msg):
    #stock trading action format (total 8 variables)
    #including: message type("H"), stock locate, tracking number, timestamp,stock, trading state, reserved, reason
    val = struct.unpack('!HH6s8scc4s',msg);
    val = list(val);
    if len(val) == 7:
        return val
    else:
        return []

def short_sale_price_test(msg):
    #Reg SHO registriction format (total 6 variables)
    #including: message type("Y"), stock locate, tracking number, timestamp,stock, Reg SHO action
    val = struct.unpack('!HH6s8sc',msg);
    val = list(val);
    if len(val) == 5:
        return val
    else:
        return []

def market_participation_position(msg):
    #market participant position format (total 9 variables)
    #including: message type("L"), stock locate, tracking number, timestamp,MPID, stock, primary market maker, market maker mode,market participant state
    val = struct.unpack('!HH6s4s8sccc',msg);
    val = list(val);
    if len(val) == 8:
        return val
    else:
        return []

def mwcb_decline_level_message(msg):
    #MWCB decline level messsage format (total 7 variables)
    #including: message type("V"), stock locate, tracking number, timestamp, level 1, level 2, level 3
    val = struct.unpack('!HH6sQQQ',msg);
    val = list(val);
    val[3:] = map(float,val[3:]);
    val[3:] = map(lambda x:x/(pow(10,8)),val[3:]);
    if len(val) == 6:
        return val
    else:
        return []

def mwcb_status_message(msg):
    #MWCB status messsage format (total 5 variables)
    #including: message type("W"), stock locate, tracking number, timestamp, breached level
    val = struct.unpack('!HH6sc',msg);
    val = list(val);
    if len(val) == 4:
        return val
    else:
        return []

def ipo_quoting_period_update(msg):
    #MIPO Quoting period update format (total 8 variables)
    #including: message type("K"), stock locate, tracking number, timestamp,stock, IPO quotation release time,IPO quotation release qualifier, IPO price
    val = list(val);
    val[6] = float(val[6]);
    val[6] = val[6]/10000;
    if len(val) == 7:
        return val
    else:
        return []

def LULD_Auction_Collar(msg):
    #LULD auction collar format (total 9 variables)
    #including: message type("J"), stock locate, tracking number, timestamp, stock, auction collar reference price, upper auction collar price, lower auction collar price, auction collar extension
    val = struct.unpack('!HH6s8sLLLI',msg);
    val = list(val);
    val[4:7] = map(float,val[4:7]);
    val[4:7] = map(lambda x:x/10000,val[4:7]);
    if len(val) == 8:
        return val
    else:
        return []

def Operational_Halt(msg):
    #operational halt format (total 7 variables)
    #including: message type("h"), stock locate, tracking number, timestamp, stock, market code, operational halt action
    val = struct.unpack('!HH6s8sLLLI',msg);
    val = struct.unpack('!HH6s8scc',msg);
    val = list(val);
    #val[8] = float(val[8]);
    #val[8] = val[8]/10000;
    if len(val) == 6:
        return val
    else:
        return []

def add_order_message(msg):
    #add order message format (total 9 variables)
    #including: message type("A"), stock locate, tracking number, timestamp, order reference number, buy/sell indicator, shares, stock, price
    val = list(val);
    val[7] = float(val[7]);
    val[7] = val[7]/10000;
    if len(val) == 8:
        return val
    else:
        return []

def add_order_with_mpid(msg):
    #add order mpid format (total 10 variables)
    #including: message type("F"), stock locate, tracking number, timestamp,order reference number, buy/sell indicator, shares, stock, price, attribution
    val = struct.unpack('!HH6sQcI8sL4s',msg);
    val = list(val);
    val[7] = float(val[7]);
    val[7] = val[7]/10000;
    if len(val) == 9:
        return val
    else:
        return []

def order_executed_message(msg):
    #order executed message format (total 7 variables)
    #including: message type("E"), stock locate, tracking number, timestamp,order reference number, executed shares, match number
    val = struct.unpack('!HH6sQIQ',msg);
    val = list(val);
    if len(val) == 6:
        return val
    else:
        return []

def order_executed_price_message(msg):
    #order executed price message format (total 9 variables)
    #including: message type("C"), stock locate, tracking number, timestamp,order reference number, executed shares, match number, printable, execution price
    val = struct.unpack('!HH6sQIQcL',msg);
    val = list(val);
    val[7] = float(val[7]);
    val[7] = val[7]/10000;
    if len(val) == 8:
        return val
    else:
        return []

def order_cancel_message(msg):
    #order cancel message format (total 6 variables)
    #including: message type("X"), stock locate, tracking number, timestamp,order reference number,cancelled shares
    val = struct.unpack('!HH6sQI',msg);
    val = list(val);
    if len(val) == 5:
        return val
    else:
        return []

def order_delete_message(msg):
    #order delete message format (total 5 variables)
    #including: message type("X"), stock locate, tracking number, timestamp,order reference number
    val = struct.unpack('!HH6sQ',msg);
    val = list(val);
    if len(val) == 4:
        return val
    else:
        return []

def order_replace_message(msg):
    #order replace message format (total 8 variables)
    #including: message type("U"), stock locate, tracking number, timestamp,original order reference number, new order reference number, shares, price
    val = struct.unpack('!HH6sQQIL',msg);
    val = list(val);
    val[6] = float(val[6]);
    val[6] = val[6]/10000;
    if len(val) == 7:
        return val
    else:
        return []

def trade_message(msg):
    #trade message format (total 10 variables)
    #including: message type("P"), stock locate, tracking number, timestamp,order reference number, buy/sell indicator,shares, stock, price, match number
    val = struct.unpack('!HH6sQcI8sLQ',msg);
    val = list(val);
    val[7] = float(val[7]);
    val[7] = val[7]/10000;
    if len(val) == 9:
        return val
    else:
        return []


def cross_trade_message(msg):
    #cross trade message format (total 9 variables)
    #including: message type("Q"), stock locate, tracking number, timestamp, shares, staock, cross price, match number, cross type
    val = struct.unpack('!HH6sQ8sLQc',msg);
    val = list(val);
    val[5] = float(val[5]);
    val[5] = val[5]/10000;
    if len(val) == 8:
        return val
    else:
        return []

def broken_trade_execution_message(msg):
    #broken trade/order execution message format (total 5 variables)
    #including: message type("B"), stock locate, tracking number, timestamp, match number
    val = struct.unpack('!HH6sQ',msg);
    val = list(val);
    if len(val) == 4:
        return val
    else:
        return []

def net_order_imbalance_message(msg):
    #net order imbalance indicator message format (total 13 variables)
    #including: message type("I"), stock locate, tracking number, timestamp, paired shares, imbalance shares, imbalance direction, stock, far price, near price, current reference price, cross type, price variation indicator
    val = struct.unpack('!HH6sQQc8sLLLcc',msg);
    val = list(val);
    val[7:10] = map(float,val[7:10]);
    val[7:10] = map(lambda x:x/10000,val[7:10]);
    if len(val) == 12:
        return val
    else:
        return []
