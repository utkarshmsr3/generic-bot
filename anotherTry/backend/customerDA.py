from backend.customer import Customer
from backend.connectionPool import ConnectionPool
class CustomerDA:

    def __init__(self):
        pass

    def authenticate(self,emailid,password):
        try:
            dbinstance = ConnectionPool.getInstance()
            dbaccess = dbinstance.getConnection()
            ccol  = dbaccess["customer"]
            cust = ccol.find({"emailid":emailid,"password":password})
            #print(type(cust))
            if cust.count() > 1:
                raise Exception("Data is inconsistent, multiple business owner with similar emaildids detected.")
            res = None
            for o in cust:
                #print(o,type(o['_id']))
                res = Customer(o['emailid'],o['password'],o['name'],o['_id'])
            dbinstance.putConnection(dbaccess)
            return res
        except Exception as e:
            print(e)
        return None