class homeModel():
    def __init__(self):
        self.isaac = False
        self.sam = False
        self.toby = False
        self.oli = False

    def setIsaac(self, home):
        self.isaac = home

    def setSam(self, home):
        self.sam = home

    def setToby(self, home):
        self.toby = home

    def setOli(self, home):
        self.oli = home
        
    def getIsaac(self):
        return self.isaac

    def getSam(self):
        return self.sam

    def getToby(self):
        return self.toby

    def getOli(self):
        return self.oli