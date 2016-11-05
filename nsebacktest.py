import re

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "root", "nsewebnfo")

# prepare a cursor object using cursor() method
cursor = db.cursor()

tradingsymbol = "BANKNIFTY"
margin = 80
lotsize = 40


def range(fromday, frommonth, fromyear, today, tomonth, toyear):
    tablename = "nsewebdata." + "days"
    sql = "select fulldate from nsewebdata.days where rank between \
            (SELECT rank FROM nsewebdata.days where daynum=" + str(fromday) + " and monthnum=" + str(
        frommonth) + " and yearnum=" + str(fromyear) + ") and \
            (SELECT rank FROM nsewebdata.days where daynum=" + str(today) + " and monthnum=" + str(
        tomonth) + " and yearnum=" + str(toyear) + ") \
            order by rank";
    try:
        # Execute the SQL command
        cursor.execute(sql)
        if cursor.rowcount < 0:
            print "Error: No rows for date range"
        results = cursor.fetchall()
        return results
    except:
        print "Error: unable to fecth data"


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


def getcallprice(date, openprice):
    month = re.sub(r'[0-9]', '', date)
    tablename = "nsewebdata." + "fo" + date + "bhav"
    sql = "SELECT STRIKE_PR,OPEN,CLOSE,OPEN-CLOSE FROM " + tablename + " where symbol='" + tradingsymbol + "' and INSTRUMENT='OPTIDX' and EXPIRY_DT like '%" + month + "%' and OPEN!=0 and \
            OPTION_TYP = 'CE' and \
            STRIKE_PR > " + str(openprice) + " and \
            STRIKE_PR < " + str(openprice + margin) + " \
            order by STRIKE_PR desc"
    price = excuteSQL(sql)
    return price


def getputprice(date, openprice):
    month = re.sub(r'[0-9]', '', date)
    tablename = "nsewebdata." + "fo" + date + "bhav"
    sql = "SELECT STRIKE_PR,OPEN,CLOSE,OPEN-CLOSE FROM " + tablename + " where symbol='" + tradingsymbol + "' and INSTRUMENT='OPTIDX' and EXPIRY_DT like '%" + month + "%' and OPEN!=0 and \
            OPTION_TYP = 'PE' and \
            STRIKE_PR < " + str(openprice) + " and \
            STRIKE_PR > " + str(openprice - margin) + "\
            order by STRIKE_PR asc"
    return excuteSQL(sql)


def start():
    totalprofit = 0
    brokragecount = 0
    dateset = range(1, 12, 2010, 28, 12, 2010)
    for daterow in dateset:
        date = daterow[0]
        print "*************************************"
        openprice = read(date)
        print "Date: " + date + ", (open,close) is: "
        print openprice
        if openprice != None:
            callprice = getcallprice(date, openprice[0])
            if callprice != None:
                print "CE (strike,open,close,open-close)"
                print callprice
            putprice = getputprice(date, openprice[0])
            if putprice != None:
                print "PE (strike,open,close,open-close)"
                print putprice
            if callprice != None and putprice != None:
                profit = callprice[3] + putprice[3]
                print "Profit/loss per share:" + str(profit)
                totalprofit += profit
                brokragecount += 1
    print "*************************************"
    print "Total Profit per share: " + str(totalprofit)
    print "Total profit * lot(40) - brokrage :" + str(totalprofit * lotsize - (brokragecount * 110))


start()

# disconnect from server
db.close()
