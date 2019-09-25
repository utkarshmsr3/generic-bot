from pymongo import MongoClient as mc
from threading import Thread, Condition

class ConnectionPool:
    __totalConnections = 1
    __connectionList = []
    __instance = None
    __no_client_condition = Condition()
    def __init__(self):
        if ConnectionPool.__instance != None :
            raise Exception("Connection pool already initialized")
        else:
            for _ in range(ConnectionPool.__totalConnections):
                ConnectionPool.__connectionList.append(ConnectionPool.__getClient())
            ConnectionPool.__instance = self
            print("instance initialised as",ConnectionPool.__instance)

    @staticmethod
    def __getClient():
        conn = mc("mongodb://localhost:27017/",username="utkarsh",password="utkarsh",authSource="chatbot_database",authMechanism="SCRAM-SHA-1")
        print(conn.list_database_names())
        return conn["db"]
    
    @staticmethod
    def getInstance():
        if ConnectionPool.__instance == None :
            ConnectionPool()
        return ConnectionPool.__instance

    

    def getConnection(self):
        li = ConnectionPool.__connectionList
        conn = None
        while True:
            if (len(li)>0):
                conn = li.pop(0)
                break
            else:
                def waitfun(cv):
                    with cv:
                        li = ConnectionPool.__connectionList
                        while(len(li)==0):
                            cv.wait()
                t1 = Thread(target=waitfun,args=(ConnectionPool.__no_client_condition,))
                t1.start()
        return conn

    def putConnection(self,conn):
        li = ConnectionPool.__connectionList
        li.append(conn)
        def notifyfun(cv):
            with cv:
                cv.notifyAll()
        t1 = Thread(target=notifyfun,args=(ConnectionPool.__no_client_condition,))
        t1.start()

            
#print(mydb.list_collection_names())
#print(cList)
"""
conn = getConnection()
print(conn)
customersList = conn["customers"]
d  = {"name":"Utkarsh Mishra","business_owner_id":"123","email":"utkarshmsr3@gmail.com","username":"utkarshmsr3@gmail.com","password":"utkarsh"}
customersList.insert_one(d)
print(*customersList.find())
getConnection()
"""