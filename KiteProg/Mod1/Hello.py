from kiteconnect import KiteConnect

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#user specific

api_key = "kitefront"
access_token = "t5kpt2aiglsmix5rlqcozuklnzyxntby"
public_token = "24c60ab021bb630bff53c4b95d6ccaa0"
request_token = "tn3xlh0neelkf410hhc3keqpctccjfyw"

client_id = "DA6651"

kite = KiteConnect(api_key=api_key,access_token=access_token)
kite.set_access_token(access_token)

#HEAVY CALL - DO ONLY ONCE A DAY
#all_intruments = kite.instruments()
#print all_intruments

#algo specific

instrument_token = "13419522"
lot_size = 40

from_date = "2016-10-03"
to_date = "2016-10-26"

interval = "60minute"

#margin points for call and put for target price
margin = 80

call_option_dict = {}
put_option_dict = {}

def get_historical_data(instrument_token):
    return kite.historical(instrument_token, from_date, to_date, interval)


def retrieve_and_add(call_option_dict, call_price):
    record_for_option = get_historical_data(instrument_token)


def get_call_option_price(open_price):
    call_price = ((open_price + margin) // lot_size ) + 1
    if not call_option_dict.has_key(call_price):
        retrieve_and_add(call_option_dict,call_price)


def strategy(records_for_target):
    profit = 0
    for record in records_for_target:
        open_price = record["open"]
        close_price = record["close"]
        call_option_price = get_call_option_price(open_price)
        


def start():
    records_for_target = get_historical_data(instrument_token)
    #print(records_for_target)
    #strategy(records_for_target)

start()
