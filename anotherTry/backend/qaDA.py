from backend.connectionPool import ConnectionPool
from backend.qa import QA
class QaDA:
    
    def __init__(self):
        pass

    def insert(self,qa):
        try:
            ins = ConnectionPool.getInstance()
            conn = ins.getConnection()
            qcol = conn["qa"]
            d = {"_id":qa.getId(),"businessOwnerId":qa.getBusinessOwnerId(),"query":qa.getQuery(),"reply":qa.getReply(),"isUserSpecific":qa.getIsUserSpecific(),"userSpecificReply":qa.getUserSpecificReply()}
            qcol.insert_one(d)
            return True
        except Exception as e:
            print(e)
        finally:
            ins.putConnection(conn)
        return False
    
    def findQueries(self,businessOwnerId):
        try:
            ins = ConnectionPool.getInstance()
            conn = ins.getConnection()
            qcol = conn["qa"]
            l=[]
            qas = qcol.find({"businessOwnerId":businessOwnerId})
            for qa in qas:
                l.append(QA(qa["businessOwnerId"],qa["query"],qa["reply"],qa["isUserSpecific"],qa["userSpecificReply"],qa["_id"])) 
            return l
        except Exception as e:
            print(e)
        finally:
            ins.putConnection(conn)

    