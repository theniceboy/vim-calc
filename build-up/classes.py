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
        self.dividing = False

class MathProduct(object):
    def __init__(self):
        global eID
        self.id = eID
        eID += 1
        self.modifier = 1
        self.children = []
        self.origin = None
        self.power = None


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
        self.dividing = False

def printExp(root, indent):
    itemOrigin = root.origin
    itemOriginID = -1
    if root.origin != None:
        itemOriginID = root.origin.id
    if type(root) == MathSum:
        print(' '*indent + "Sum (id: " + str(root.id) + "), isDividing =", root.dividing, ", type: " + root.pairStr + " origin: " + str(itemOriginID))
    elif type(root) == MathProduct:
        print(' '*indent + "Product (id: " + str(root.id) + "), modifier: " + str(root.modifier) + " origin: " + str(itemOriginID))
    elif type(root) == MathElement:
        print(' '*indent + "Element (id: " + str(root.id) + "): [ " + root.contentString + " ], isDividing =", root.dividing, " origin: " + str(itemOriginID))
    if root.power != None:
        print(' '*indent + ", with Power {")
        printExp(root.power, indent + 3)
        print(' '*indent + "}")
    for child in root.children:
        printExp(child, indent + 3)


