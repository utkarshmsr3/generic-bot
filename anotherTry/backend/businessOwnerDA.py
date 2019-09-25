from backend.businessOwner import BusinessOwner
from backend.connectionPool import ConnectionPool
class BusinessOwnerDA:

    def __init__(self):
        pass

    def insert(self,owner):
        try:
            dbinstance = ConnectionPool.getInstance()
            dbaccess = dbinstance.getConnection()
            bocol  = dbaccess["businessOwner"]
            d = {"emailid":owner.getEmailid(),"password":owner.getPassword(),"name":owner.getName()}
            if not owner.getId() == "":
                d["_id"] = owner.getId()
            id = bocol.insert_one(d)
            if owner.getId() == "":
                owner.setId(id.inserted_id)
            dbinstance.putConnection(dbaccess)
        except Exception as e:
            print(e)
    
    def authenticate(self,emailid,password):
        try:
            dbinstance = ConnectionPool.getInstance()
            dbaccess = dbinstance.getConnection()
            bocol  = dbaccess["businessOwner"]
            owner = bocol.find({"emailid":emailid,"password":password})
            print(type(owner))
            #if owner.count() > 1:
                #raise Exception("Data is inconsistent, multiple business owner with similar emaildids detected.")
            ans = None
            for o in owner:
                #print(o,type(o['_id']))
                ans = BusinessOwner(o['emailid'],o['password'],o['name'],o['_id'])
            dbinstance.putConnection(dbaccess)
            return ans
        except Exception as e:
            print(e)
        finally:
            dbinstance.putConnection(dbaccess)


#b = BusinessOwner("utkarshmsr3@gmail.com","utkarsh","Utkarsh Mishra")
#bda = BusinessOwnerDA()
#bda.insert(b)
#print(bda.find("utkarshmsr3@gmail.com","utkarsh"))
