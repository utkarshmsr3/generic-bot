class BusinessOwner:

    def __init__(self,emailid,password,name="",id=""):
        self.__id = id
        self.__name = name
        self.__emailid = emailid
        self.__password = password

    def setId(self,id):
        self.__id = id
    
    def getId(self):
        return self.__id
        
    def setName(self,name):
        self.__name = name 

    def getName(self):
        return self.__name

    def setEmailid(self,emailid):
        self.__emailid = emailid
    
    def getEmailid(self):
        return self.__emailid

    def setPassword(self,password):
        self.__password = password

    def getPassword(self):
        return self.__password

    
