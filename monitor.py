import MySQLdb
import requests
import time
import datetime
from time import sleep

class websitesMonitor:

    def connectionToDB(self, type, query):
        connectionToDB = MySQLdb.connect('localhost', 'sitemonitor', 'somepass', "sitemonitor")
        cursorDB = connectionToDB.cursor()
        if type == 'insert':
            cursorDB.execute(query)
            connectionToDB.commit()
            print('Added!')
        elif type == 'select':
            cursorDB.execute(query)
            return cursorDB


    def selectWebsites(self):
        #cursorDB, connectionToDB = self.connectionToDB()
        myWebsites = self.connectionToDB('select', "SELECT * FROM `main_websites`")
        #cursorDB.commit()
        return myWebsites

    def addNewLog(self, website_address, status, response_time, checked, datetime_check):
        #cursorDB, connectionToDB = self.connectionToDB()
        print(website_address)
        print(status)
        print(response_time)
        print(datetime_check)
        query = "INSERT INTO `main_connection_log` VALUES(NULL, '"+str(website_address)+"', '"+str(status)+"', '"+str(response_time)+"', "+checked+", '"+str(datetime_check)+"')"
        print(query)
        self.connectionToDB('insert', query)
        #cursorDB.execute("INSERT INTO `main_connection_log` VALUES(NULL, '"+str(website_address)+"', '"+str(status)+"', '"+str(response_time)+"', 1, '"+str(datetime_check)+"')")
        #connectionToDB.commit()

    def checkConnection(self, url, require_content):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        try:
            start = time.clock()
            response = requests.get(url)
            check_content = response.text.find(require_content)
            checked_new_log = '1'
            if check_content < 0:
                response = "Content Error!"
                checked_new_log = '0'
            print(check_content)
            request_time = time.clock() - start
            print(str(response))
            print(request_time)
            sql = "INSERT INTO `main_connection_log` VALUES(NULL, '" + str(url) + "', \"" + str(response) + "\", '"+str(request_time)+"', "+checked_new_log+", '" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "')"
            print(sql)
            self.connectionToDB('insert', sql)
        except Exception as error:
            print(error)
            sql = "INSERT INTO `main_connection_log` VALUES(NULL, '"+str(url)+"', \""+str(error)+"\", '0', 0, '"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"')"
            print(sql)
            self.connectionToDB('insert', sql)

#creating Monitor
#newMonitor = websitesMonitor()
#download Websites from db
#newMonitor.websites = newMonitor.selectWebsites()
#print(newMonitor.websites)
a=1
while a==1:
    # creating Monitor
    newMonitor = websitesMonitor()
    # download Websites from db
    newMonitor.websites = newMonitor.selectWebsites()
    #print(newMonitor.websites)
    sleep(5)
    for website in newMonitor.websites:
        #print(website[2])
        timenow = datetime.datetime.now() - datetime.timedelta(minutes=int(website[2]))
        #timenow = timenow.strftime("%Y-%m-%d %H:%M:%S")
        print(timenow)
        sql_query = "SELECT * FROM `main_connection_log` WHERE website_address = '"+website[1]+"' ORDER BY `id` DESC LIMIT 1 "
        #print(sql_query)
        newMonitor.site_log = newMonitor.connectionToDB('select', sql_query)
        for newMonitor.site_log in newMonitor.site_log:
            print(newMonitor.site_log[5])
            if newMonitor.site_log[5] < timenow:
                newMonitor.site_log = 1
                break
            else:
                newMonitor.site_log = 0
                break
        #newMonitor.site_log = newMonitor.site_log.fetchone()[0]
        print(newMonitor.site_log)
        if newMonitor.site_log > 0:
            newMonitor.checkConnection(website[1], website[3])
        else:
            print("NIC DO SPRAWDZENIA")