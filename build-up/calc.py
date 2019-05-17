from classes import *

s = "12+(345-34)"
s_len = 0

__DEBUG_PAUSE = False
__DEBUG_OUTPUT = False

def convertMathString():
    global s, s_len
    print(s)
    s_len = len(s)
    print(s_len)
    root = MathSum()
    buildSum(root, 0, "", 0)
    return root


def buildSum(obj, startLoc, pairChar, level):
    global s, s_len
    loc = startLoc
    obj.pairChar = pairChar
    while True:
        if __DEBUG_OUTPUT:
            print("level:", level, "summing", loc, s[loc])
        if __DEBUG_PAUSE:
            _ = input()

        if loc > s_len - 1:
            break
        newProduct = MathProduct()
        newProduct.origin = obj
        obj.children.append(newProduct)
        if __DEBUG_OUTPUT:
            print("level:", level, "___add child", obj.children)
        if s[loc] == "-":
            newProduct.modifier = -1
            loc += 1
        if s[loc] == "+":
            loc += 1
        if __DEBUG_OUTPUT:
            print("level:", level, "will_build_product")
        loc = buildProduct(newProduct, loc, level + 1)
        if s[loc] == ")":
            if __DEBUG_OUTPUT:
                print("level:", level, "End of Sum", "curloc:", loc)
            return loc

    return loc


def buildProduct(obj, startLoc, level):
    global s, s_len
    loc = startLoc
    while True:
        if __DEBUG_OUTPUT:
            print("level:", level, "producting", loc, s[loc])
        if __DEBUG_PAUSE:
            _ = input()
        if loc >= s_len:
            break
        elif s[loc] == "+" or s[loc] == "-":
            break
        elif s[loc].isnumeric():
            newElement = MathElement()
            newElement.origin = obj
            obj.children.append(newElement)
            loc = buildElement(newElement, loc, level + 1)
        elif s[loc] == "(":
            newSum = MathSum()
            newSum.origin = obj
            obj.children.append(newSum)
            loc = buildSum(newSum, loc + 1, pairChar = "(", level = level + 1)
        elif s[loc] == ")":
            if __DEBUG_OUTPUT:
                print("level:", level, "end of sum", "curloc:", loc)
            return loc

    return loc


def buildElement(obj, startLoc, level):
    global s, s_len
    loc = startLoc
    if s[loc].isnumeric():
        while s[loc].isnumeric():
            loc += 1
            if loc >= s_len:
                break
        obj.contentString = s[startLoc:loc]
        obj.contentNumber = int(obj.contentString)

    return loc


# mathString = input().strip()
expRoot = convertMathString()
printExp(expRoot, 0)

