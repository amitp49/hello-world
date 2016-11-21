import re
import requests
import json
import MySQLdb

# Open database connection
#db = MySQLdb.connect("localhost", "root", "root", "nsewebnfo")
db = MySQLdb.connect(host="52.187.79.74",port=3306,user="amitp",passwd="amitp",db="nsewebdata")

baseUrl = "http://13.67.57.203/api/v2/fno/_table"
headers = {"Accept": "application/json","X-DreamFactory-Api-Key":"6498a8ad1beb9d84d63035c5d1120c007fad6de706734db9689f8996707e0f7d",
           "X-DreamFactory-Session-Token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMsInVzZXJfaWQiOjMsImVtYWlsIjoiYW1pdHA0OUBob3RtYWlsLmNvbSIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOiJodHRwOlwvXC8xMy42Ny41Ny4yMDNcL2FwaVwvdjJcL3VzZXJcL3Nlc3Npb24iLCJpYXQiOjE0Nzk2NDYzNzksImV4cCI6MTQ3OTY0OTk3OSwibmJmIjoxNDc5NjQ2Mzc5LCJqdGkiOiJkYmZhYzU4N2FlYWNhMjI1NGRhYWVhZWNkNDFmN2I0MSJ9.X2iuhOkNe3X4o26IbYPsZGFTZHDJawV4LW8FvRDzY0I",
           "Authorization":"Basic YW1pdHA0OUBob3RtYWlsLmNvbTpBbWl0QDEyMw=="}

# prepare a cursor object using cursor() method
cursor = db.cursor()

tradingsymbol = "BANKNIFTY"
margin = 120
lotsize = 40

daystable = "days"

def range(fromday, frommonth, fromyear, today, tomonth, toyear):
    tablename = "nsewebdata." + daystable
    sql = "select fulldate from nsewebdata.days where rank between \
            (SELECT rank FROM nsewebdata.days where daynum=" + str(fromday) + " and monthnum=" + str(
        frommonth) + " and yearnum=" + str(fromyear) + ") and \
            (SELECT rank FROM nsewebdata.days where daynum=" + str(today) + " and monthnum=" + str(
        tomonth) + " and yearnum=" + str(toyear) + ") \
            order by rank";

    fromURL = baseUrl + daystable +"?fields=rank&filter=(daynum=" +  str(fromday) + ")and(monthnum="+ str(frommonth)+")and(yearnum="+ str(fromyear) +")&limit=1"
    jsonfromdata = getJsonData(fromURL)
    fromRank = jsonfromdata[0]["rank"]

    toURL = baseUrl + "?fields=rank&filter=(daynum=" +  str(today) + ")and(monthnum="+ str(tomonth)+")and(yearnum="+ str(toyear) +")&limit=1"
    jsontodata = getJsonData(toURL)
    toRank = jsontodata[0]["rank"]

    url = baseUrl + "?fields=fulldate&filter=(rank>="+str(fromRank)+") and (rank<="+str(toRank)+")"
    jsondata = getJsonData(url)
    return jsondata[0]

    #try:
        # Execute the SQL command
        #cursor.execute(sql)
        #if cursor.rowcount < 0:
        #    print "Error: No rows for date range"
        #results = cursor.fetchall()
        #return results
    #except:
        #print "Error: unable to fecth data"


def read(date):
    month = re.sub(r'[0-9]', '', date)
    tablename = "nsewebdata." + "fo" + date + "bhav"
    print tablename
    sql = "SELECT OPEN,CLOSE FROM " + tablename + " where symbol='" + tradingsymbol + "' and INSTRUMENT='FUTIDX' and EXPIRY_DT like '%" + month + "%'"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        if cursor.rowcount != 1:
            print "Error: More than 1 row for future"
        results = cursor.fetchall()
        for row in results:
            return row
    except:
        print "Error: unable to fecth data"


def excuteSQL(sql):
    try:
        # Execute the SQL command
        cursor.execute(sql)
        if cursor.rowcount < 0:
            print "Error: No rows for option."
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            return row
    except:
        print "Error: unable to fecth data"


def getJsonData(url):
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    return json_data["resource"]


def getcallprice(date, openprice):
    month = re.sub(r'[0-9]', '', date)
    endpoint = "fo" + date + "bhav"

    url= (baseUrl + "/" + endpoint +
                    "?fields=STRIKE_PR,open,close"
                    "&filter=(symbol='"+ tradingsymbol +"')and(OPTION_TYP=CE)and(EXPIRY_DT like '%" + month + "%')and(INSTRUMENT='OPTIDX')and(OPEN != 0)and(STRIKE_PR>"+ str(openprice) +")and(STRIKE_PR<"+str(openprice + margin) +")"
                    "&order=STRIKE_PR desc,EXPIRY_DT desc"
                    "&limit=1");
    jsondata = getJsonData(url)
    return jsondata


def getputprice(date, openprice):
    month = re.sub(r'[0-9]', '', date)
    endpoint = "fo" + date + "bhav"

    url= (baseUrl + "/" + endpoint +
          "?fields=STRIKE_PR,open,close"
          "&filter=(symbol='"+ tradingsymbol +"')and(OPTION_TYP=PE)and(EXPIRY_DT like '%" + month + "%')and(INSTRUMENT='OPTIDX')and(OPEN != 0)and(STRIKE_PR<"+ str(openprice) +")and(STRIKE_PR>"+str(openprice - margin) +")"
            "&order=STRIKE_PR asc,EXPIRY_DT desc"
            "&limit=1");
    jsondata = getJsonData(url)
    return jsondata


def readexpiry(date):
    pass


def start():
    totalprofit = 0
    brokragecount = 0
    dateset = range(3, 10, 2016, 28, 10, 2016)
    for daterow in dateset:
        date = daterow[0]
        #expirydate = readexpiry(date)
        print "*************************************"
        openprice = read(date)
        print "Date: " + date + ", (open,close) is: "
        print openprice
        if openprice != None:
            callprice = getcallprice(date, openprice[0])
            if callprice != None:
                print "CE (strike,open,close)"
                print callprice
            putprice = getputprice(date, openprice[0])
            if putprice != None:
                print "PE (strike,open,close)"
                print putprice
            if callprice != None and putprice != None:
                profit = (callprice[0]["OPEN"]-callprice[0]["CLOSE"]) + (putprice[0]["OPEN"]-putprice[0]["CLOSE"])
                print "Profit/loss per share:" + str(profit)
                totalprofit += profit
                brokragecount += 1
    print "*************************************"
    print "Total Profit per share: " + str(totalprofit)
    print "Total profit * lot(40) - brokrage :" + str(totalprofit * lotsize - (brokragecount * 112.5))


start()

# disconnect from server
db.close()
