from classes import *

s = "12+67*1235(345-34)^2/9 "
# s = "1/2 "
# s = "sin 12 + 5"

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
            print("sum pause inputed")
        if s[loc] == ' ':
            return loc
        if loc > s_len - 1:
            break
        newProduct = MathProduct()
        newProduct.origin = obj
        obj.children.append(newProduct)
        if __DEBUG_OUTPUT:
            print("level:", level, "___add child", obj.children)
        if s[loc] == '-':
            newProduct.modifier = -1
            loc += 1
        if s[loc] == '+':
            loc += 1
        if __DEBUG_OUTPUT:
            print("level:", level, "will_build_product")
        loc = buildProduct(newProduct, loc, level + 1)
        if s[loc] == ')':
            loc = loc + 1
            if __DEBUG_OUTPUT:
                print("level:", level, "End of Sum", "curloc:", loc)
            return loc

    return loc


def buildProduct(obj, startLoc, level):
    global s, s_len
    loc = startLoc
    isDividing = False
    while True:
        if __DEBUG_OUTPUT:
            print("level:", level, "producting", loc, s[loc])
        if s[loc] == ' ':
            return loc
        if __DEBUG_PAUSE:
            _ = input()
            print("product pause inputed")
        if loc >= s_len:
            break
        elif s[loc] == '+' or s[loc] == '-':
            break
        elif s[loc].isnumeric():
            newElement = MathElement()
            newElement.origin = obj
            newElement.dividing = isDividing
            obj.children.append(newElement)
            loc = buildElement(newElement, loc, level + 1)
        elif s[loc] == '*':
            isDividing = False
            loc += 1
        elif s[loc] == '/':
            isDividing = True
            loc += 1
        elif s[loc] == '(':
            newSum = MathSum()
            newSum.origin = obj
            newSum.dividing = isDividing
            obj.children.append(newSum)
            loc = buildSum(newSum, loc + 1, '(', level=level + 1)
            if s[loc] == '^':
                loc += 1
                if s[loc].isnumeric():
                    newElement = MathElement()
                    newSum.power = newElement
                    newElement.origin = newSum
                    loc = buildElement(newElement, loc, level=level + 1)
                elif s[loc] == '(':
                    loc += 1
                    newSum = MathSum()
                    newSum.power = newSum
                    newSum.origin = newSum
                    loc = buildSum(newSum, loc, '(', level=level + 1)
        elif s[loc] == ')':
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
        if s[loc] == ' ':
            return loc
        # Check if a 'power' operation if encountered
        if s[loc] == '^':
            loc += 1
            if s[loc].isnumeric():
                newElement = MathElement()
                obj.power = newElement
                newElement.origin = obj
                loc = buildElement(newElement, loc, level=level + 1)
            elif s[loc] == '(':
                loc += 1
                newSum = MathSum()
                obj.power = newSum
                newSum.origin = obj
                loc = buildSum(newSum, loc, '(', level=level + 1)

    return loc


errors = []
def calcRoot (root):
    # print(root.id, root)
    # _ = input()
    if type(root) == MathSum:
        ans = 0
        for child in root.children:
            ans = ans + child.modifier * calcRoot(child)
        if root.power != None:
            ans = ans ** calcRoot(root.power)
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
                        print("divided by 0")
                        errors.append("Dividing 0 at id=" + str(root.id))
                        return 1
                    else:
                        ans = ans / dv
                else:
                    ans = ans * calcRoot(child)
        return ans
    elif type(root) == MathElement:
        if root.power != None:
            return root.contentNumber ** calcRoot(root.power)
        return root.contentNumber


# mathString = input().strip()
expRoot = convertMathString()
expandExp(expRoot, 0)

print(calcRoot(expRoot))
print(errors)
printExp(expRoot)

