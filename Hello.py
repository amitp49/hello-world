from bson import ObjectId
from kiteconnect import KiteConnect
from pymongo import MongoClient

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#user specific

api_key = "kitefront"
access_token = "qbgmedd5qyzgho132lg4l4hbb45p5xey"
public_token = "2f402d0d2c7eb1af48fbc28483505308"
request_token = "x6595x2ikldxml85pdmz5u5sdg4txfxj"

client_id = "DA6651"

kite = KiteConnect(api_key=api_key,access_token=access_token)
kite.set_access_token(access_token)


# creating connectioons for communicating with Mongo DB
mongoclient = MongoClient('localhost:27017')
mongodatabase = mongoclient.nfo04112016

#HEAVY CALL - DO ONLY ONCE A DAY
#all_intruments = kite.instruments()
#print all_intruments

#all_instruments = {}
#LOAD directly from FILE
#with open("Output.csv") as f:
#    all_instruments = f.readlines()


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

# function to read records from mongo db
def read(expiry,strike,instrument_type):
    cursor = mongodatabase.nfo.find({ "expiry": expiry, "strike":strike,"instrument_type":instrument_type })
    for document in cursor: print(document)
    return cursor

# function to read records count from mongo db
def count():
    return mongodatabase.nfo.find({}).count()

def start():
    #records_for_target = get_historical_data(instrument_token)
    #print(records_for_target)
    #strategy(records_for_target)
    read("2016-11-10",17600.0,"CE")

start()
