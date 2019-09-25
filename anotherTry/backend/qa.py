class QA:
    def __init__(self,businessOwnerId,query,reply,isUserSpecific=False,userSpecificReply="",id=""):
        self.__businessOwnerId = businessOwnerId
        self.__id = id
        self.__query = query
        self.__reply = reply
        self.__isUserSpecific = isUserSpecific
        self.__userSpecificReply = userSpecificReply

    def setBusinessOwnerId(self,businessOwnerId):
        self.__businessOwnerId = businessOwnerId

    def getBusinessOwnerId(self):
        return self.__businessOwnerId

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def setQuery(self,query):
        self.__query = query

    def getQuery(self):
        return self.__query

    def setReply(self,reply):
        self.__reply = reply

    def getReply(self):
        return self.__reply

    def setIsUserSpecific(self,isUserSpecific):
        self.__isUserSpecific = isUserSpecific

    def getIsUserSpecific(self):
        return self.__isUserSpecific

    def setUserSpecificReply(self,userSpecificReply):
        self.__userSpecificReply = userSpecificReply

    def getUserSpecificReply(self):
        return self.__userSpecificReply