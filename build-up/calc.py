import sys
import math
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("str")
# args = parser.parse_args()

# s = args.str

# s = input()
# s = "(2+4)*5^3"
# s = sys.argv[1]
# s = "pi*((1-3)^4-15+((9-8)))"
# s = "sqrt(8*sin(pi/6)+12)"
s = "(sqrt(4+6pi)+3)^4/5+ln 4-3"
s = s + '_'

# s = "12+67*1235(345-34)^2/9 "
# s = "1/2 "
# s = "sin 12 + 5"

s_len = 0
s_start = 0
s_end = 0
s_should_end = False

__DEBUG_PAUSE = False
__DEBUG_OUTPUT = False

eID = 0


class MathSum(object):
    def __init__(self):
        global eID
        self.id = eID
        eID += 1
        self.pairChar = ""
        self.children = []
        self.result = 0
        self.origin = None
        self.power = None
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
        self.powerModifier = 1
        self.children = []
        self.dividing = False

def expandExp(root, indent):
    itemOriginID = -1
    if root.origin != None:
        itemOriginID = root.origin.id
    if type(root) == MathSum:
        print(' '*indent + "Sum (id: " + str(root.id) + "), isDividing =", root.dividing, ", type: " + root.pairChar + " origin: " + str(itemOriginID))
    elif type(root) == MathProduct:
        print(' '*indent + "Product (id: " + str(root.id) + "), modifier: " + str(root.modifier) + " origin: " + str(itemOriginID))
    elif type(root) == MathElement:
        print(' '*indent + "Element (id: " + str(root.id) + "): [ " + root.contentString + " ], isDividing =", root.dividing, " origin: " + str(itemOriginID))
    if root.power != None:
        print(' '*indent + ", with Power {")
        expandExp(root.power, indent + 3)
        print(' '*indent + "}")
    for child in root.children:
        expandExp(child, indent + 3)


ansStr = ""


def printExp(root):
    global ansStr
    ansStr = ""
    _printExp(root)
    print(ansStr)

def _printExp(root):
    global ansStr
    if type(root) == MathSum:
        isFirstItem = True
        for child in root.children:
            if isFirstItem:
                if child.modifier == -1:
                    ansStr += "-"
            else:
                ansStr += "+" if child.modifier == 1 else "-"
            isFirstItem = False
            _printExp(child)
        if root.pairChar == "(":
            ansStr += ")"
    elif type(root) == MathProduct:
        isFirstItem = True
        for child in root.children:
            if isFirstItem == False:
                ansStr += "/" if child.dividing == 1 else "*"
            isFirstItem = False
            _printExp(child)
    elif type(root) == MathElement:
        if root.contentString == '(':
            ansStr += '('
            _printExp(root.children[0])
            ansStr += ')'
        else:
            ansStr += root.contentString
            if len(root.children) > 0:
                _printExp(root.children[0])
        if root.power != None:
            ansStr += "^"
            _printExp(root.power)

scientificNumbers = {'pi': math.pi, \
                     'e' : math.e}
def isScientific(loc):
    global s
    str = s[loc:loc+5].lower()
    if str == 'log10':
        return (True, str, True)
    str = str[:-1]
    if str == 'log2' or \
       str == 'sqrt':
        return (True, str, True)
    str = str[:-1]
    if str == 'sin' or \
       str == 'cos' or \
       str == 'tan':
        return (True, str, True)
    str = str[:-1]
    if str == 'ln':
        return (True, str, True)
    if str == 'pi':
        return (True, str, False)
    str = str[:-1]
    if str == 'e':
        return (True, str, False)
    return (False, '', False)

def convertMathString():
    global s, s_len, s_start, s_end
    # print(s)
    s_len = len(s)
    # print(s_len)
    root = MathSum()
    buildSum(root, 0, "", 0)
    return root


def buildSum(obj, startLoc, pairChar, level):
    print("__pairchar:", pairChar)
    global s, s_len
    loc = startLoc
    obj.pairChar = pairChar
    while True:
        if __DEBUG_OUTPUT:
            print("level:", level, "summing, loc:", loc, s[loc])
        if __DEBUG_PAUSE:
            _ = input()
            print("sum pause inputed")

        if s[loc] == '_':
            return loc
        elif s[loc] == ' ':
            loc += 1
            continue
        if loc > s_len - 1:
            break
        newProduct = MathProduct()
        newProduct.origin = obj
        obj.children.append(newProduct)

        if __DEBUG_OUTPUT:
            print("level:", level, "___add child, loc:", loc, obj.children)

        if s[loc] == '-':
            newProduct.modifier = -1
            loc += 1
        elif s[loc] == '+':
            loc += 1

        if __DEBUG_OUTPUT:
            print("level:", level, "loc:", loc, "will_build_product")

        loc = buildProduct(newProduct, loc, level+1)

        print("loc:", loc, "sloc:", s[loc], "pairchar:", pairChar)
        if s[loc] == pairChar:
            loc = loc + 1
            if __DEBUG_OUTPUT:
                print("level:", level, "End of Sum", "loc:", loc)
            return loc

        if pairChar == 'oneProductAllowed':
            break

    return loc


def buildProduct(obj, startLoc, level):
    global s, s_len, s_should_end
    loc = startLoc
    isDividing = False
    while True:
        if __DEBUG_OUTPUT:
            print("level:", level, "producting, loc:", loc, s[loc])
        if s[loc] == '_':
            return loc
        if s[loc] == ' ':
            loc += 1
            continue
        if __DEBUG_PAUSE:
            _ = input()
            print("product pause inputed")
        if loc >= s_len:
            break
        elif s[loc] == '+' or s[loc] == '-':
            break
        elif s[loc].isnumeric() or s[loc] == '.':
            newElement = MathElement()
            newElement.origin = obj
            newElement.dividing = isDividing
            obj.children.append(newElement)
            loc = buildElement(newElement, loc, level+1)
        elif s[loc].isalpha():
            scientific = isScientific(loc)
            if scientific[0]:
                newElement = MathElement()
                newElement.origin = obj
                newElement.dividing = isDividing
                obj.children.append(newElement)
                loc = buildElement(newElement, loc, level=level+1)
        elif s[loc] == '*':
            isDividing = False
            loc += 1
        elif s[loc] == '/':
            isDividing = True
            loc += 1
        elif s[loc] == '(':
            newElement = MathElement()
            newElement.origin = obj
            newElement.dividing = isDividing
            obj.children.append(newElement)
            loc = buildElement(newElement, loc, level=level+1)
        elif s[loc] == ')':
            if __DEBUG_OUTPUT:
                print("level:", level, "end of sum", "loc:", loc)
            return loc

    return loc


def buildElement(obj, startLoc, level):
    global s, s_len, s_should_end
    loc = startLoc
    isElement = False
    scientific = isScientific(loc)
    if s[loc] == '(':
        obj.contentString = '('
        newSum = MathSum()
        newSum.origin = obj
        obj.children.append(newSum)
        loc = buildSum(newSum, loc+1, ')', level=level+1)
    if s[loc].isnumeric():
        hasDot = False
        while s[loc].isnumeric() or s[loc] == '.':
            if s[loc] == '.':
                if hasDot:
                    break
                else:
                    hasDot = True
            loc += 1
            if loc >= s_len:
                break
        obj.contentString = s[startLoc:loc]
        obj.contentNumber = int(obj.contentString)
    elif scientific[0]:
        loc += len(scientific[1])
        obj.contentString = scientific[1]
        if scientific[2]:
            if s[loc] == '(':
                newElement = MathElement()
                newElement.origin = obj
                obj.children.append(newElement)
                loc = buildElement(newElement, loc, level=level+1)
            else:
                newProduct = MathProduct()
                newProduct.origin = obj
                obj.children.append(newProduct)
                loc = buildProduct(newProduct, loc, level=level+1)
        else:
            obj.contentNumber = scientificNumbers[scientific[1]]
    else:
        s_should_end = False

    if s[loc] == '_':
        return loc
    if s[loc] == '^':
        loc += 1
        powerModifier = 1
        if s[loc] == '-':
            powerModifier = -1
            loc += 1
        newElement = MathElement()
        newElement.origin = obj
        obj.power = newElement
        obj.powerModifier = powerModifier
        loc = buildElement(newElement, loc, level=level+1)

    return loc


errors = []
def calcRoot (root):
    # print(root.id, root)
    # _ = input()
    if type(root) == MathSum:
        ans = 0
        for child in root.children:
            ans = ans + child.modifier * calcRoot(child)
        return ans
    elif type(root) == MathProduct:
        ans = None
        for child in root.children:
            if ans == None:
                ans = calcRoot(child)
            else:
                if child.dividing:
                    dv = calcRoot(child)
                    if dv == 0:
                        errors.append("Dividing 0 at id=" + str(root.id))
                        return 1
                    else:
                        ans = ans / dv
                else:
                    ans = ans * calcRoot(child)
        return ans
    elif type(root) == MathElement:
        ans = root.contentNumber
        child_ans = 0
        rootstr = root.contentString
        if len(root.children) > 0:
            child_ans = calcRoot(root.children[0])
        if rootstr == '(':
            ans = child_ans
        if rootstr == 'sin':
            ans = math.sin(child_ans)
        elif rootstr == 'cos':
            ans = math.cos(child_ans)
        elif rootstr == 'tan':
            ans = math.tan(child_ans)
        elif rootstr == 'ln':
            ans = math.log(child_ans)
        elif rootstr == 'log2':
            ans = math.log2(child_ans)
        elif rootstr == 'log10':
            ans = math.log10(child_ans)
        elif rootstr == 'sqrt':
            ans = math.sqrt(child_ans)
        if root.power != None:
            return ans ** calcRoot(root.power)
        return ans


# mathString = input().strip()
expRoot = convertMathString()

ans = calcRoot(expRoot)
printExp(expRoot)
expandExp(expRoot, 0)

if len(errors) > 0:
    print(0)
    print(errors)
else:
    print(1)
    print(ans)
# print(errors)
# printExp(expRoot)

