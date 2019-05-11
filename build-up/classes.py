class MathExpression(object):
    def __init__(self):
        self.firstElement = None
        self.result = 0

class MathElement(object):
    def __init__(self):
        self.contentString = ""
        self.contentNumber = 0
        self.next = None
        self.origin = None
        self.Children = None

