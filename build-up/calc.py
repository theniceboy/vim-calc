
class MathExpression(object):
    def __init__(self):
        self.firstElement = None
        self.power = None
        self.result = 0

class MathProduct (object):
    def __init__(self):
        

class MathSum(object):
    def __init__(self):
        self.contentString = ""
        self.contentNumber = 0
        self.next = None
        self.origin = None
        self.power = None
        self.Children = None

def convertMathString(s):
    for char in s:
        print(char)
    exp = MathExpression()
    return exp

mathString = input().strip()
exp = convertMathString(mathString)
print(exp.result)

