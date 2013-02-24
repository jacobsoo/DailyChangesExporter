#!/usr/bin/env python
# Settings
from datetime import date, datetime, timedelta, time
import urllib2
import sys, os, thread

# Function definitions
def datespan(startDate, endDate, delta=timedelta(days=1)):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta

# Banner
def Banner():
    print("=================================================")
    print("DailyChanges.com transfer v0.2                   ")
    print("=================================================")

# Usage
def help_menu(cmd):
    print("Usage: %s <start_Date> <endDate>\n") % (cmd)
    print("<startDate> - DD/MM/YYYY\n")
    print("<endDate> - DD/MM/YYYY\n")

# Main Program
def main(mStartDate,mEndDate):
    szNameServer = ["domaincontrol.com", "name-services.com", "blank-nameserver.com", "expiredns.com", "namebrightdns.com", "hostingpro.biz", "expirenotification.com"]
    for i in szNameServer:
        NameServerLoop(i,mStartDate,mEndDate)

# NameServer Loop
def NameServerLoop(NameServer, startDate,endDate):
    D1 = startDate.split('/')
    D2 = endDate.split('/')
    for day in datespan(date(int(D1[2]),int(D1[1]),int(D1[0])), date(int(D2[2]),int(D2[1]),int(D2[0])), delta=timedelta(days=1)):
        url = "http://www.dailychanges.com/export/%s/%s/export.csv" % (NameServer, day)
        opener = urllib2.build_opener()
        referer = "http://www.dailychanges.com/" + NameServer + "/"
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0'),('Referer', referer)]
        usock = opener.open(url)
        data = usock.read()
        szFileName = NameServer + "-" + str(day) + "-export.csv"
        localFile = open(szFileName, 'w')
        print("[*] Saving %s\n" % szFileName)
        localFile.write(data)
        localFile.close()
        usock.close()
    
if __name__ == '__main__':
    Banner()
    if len(sys.argv)<3:
        help_menu(sys.argv[0])
    else:
        startDate = sys.argv[1]
        endDate = sys.argv[2]
        main(startDate,endDate)