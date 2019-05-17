eID = 0

class MathSum(object):
    def __init__(self):
        global eID
        self.id = eID
        eID += 1
        self.pairStr = ""
        self.children = []
        self.power = None
        self.result = 0
        self.origin = None

class MathProduct(object):
    def __init__(self):
        global eID
        self.id = eID
        eID += 1
        self.modifier = 1
        self.children = []
        self.origin = None
        

class MathElement(object):
    def __init__(self):
        global eID
        self.id = eID
        eID += 1
        self.contentString = ""
        self.contentNumber = 0
        self.origin = None
        self.power = None
        self.children = []

def printExp(root, indent):
    itemOrigin = root.origin
    itemOriginID = -1
    if root.origin != None:
        itemOriginID = root.origin.id
    if type(root) == MathSum:
        print(' '*indent + "Sum (" + str(root.id) + "), type: " + root.pairStr + " origin: " + str(itemOriginID))
    elif type(root) == MathProduct:
        print(' '*indent + "Product (" + str(root.id) + "), modifier: " + str(root.modifier) + " origin: " + str(itemOriginID))
    elif type(root) == MathElement:
        print(' '*indent + "Element (" + str(root.id) + "): " + root.contentString + " origin: " + str(itemOriginID))
    for child in root.children:
        printExp(child, indent + 3)


