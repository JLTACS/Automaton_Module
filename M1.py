class Node:
    def __init__(self, data, left, right, parent):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def postfixNotation(regExp):
    validChar = createAcceptedChars()
    regExp = addConcatOp(regExp, validChar)
    A = []
    B = []
    finish = False
    j = 0

    while(not finish):
        #PUSH
        for j in range(j,len(regExp)):
            if(regExp[j] != ')'):
                A.append(Node(regExp[j], None, None, None))

            else: 
                A.append(Node(regExp[j], None, None, None))
                break
        j += 1
        #POP
        while(True):
            N = A.pop()

            if(N.data in validChar or N.data == ')'):
                B.append(N)
            elif(N.data in ('*','+')):
                child = B.pop()
                child.parent = N
                N.right = child
                B.append(N)
            elif(N.data in ('$',',')):
                nodeA = A.pop()
                nodeA.parent = N
                N.left = nodeA
                nodeB = B.pop()
                nodeB.parent = N
                N.right = nodeB
                B.append(N)
            elif(N.data == '('):
                nodeB = B.pop()
                temp = nodeB
                nodeB = B.pop()
                B.append(temp)

            if(len(A) == 0):
                if(j == len(regExp)):
                    return B.pop()
                else:
                    A.append(B.pop())
            if(len(B) == 0):
                break
        

def addConcatOp(regExp, chars):
    endOfExp = False
    i = 0
    size = len(regExp)
    while(i < size): 
        if(i != (len(regExp) - 1) and (regExp[i] in chars or regExp[i] in ('*', '+'))):
            if(regExp[i+1] in chars):
                regExp = insertInTheMiddle(regExp, '$', i+1)
            elif(regExp[i+1] == '('):
                regExp = insertInTheMiddle(regExp, '$', i+1)
            elif(regExp[i+1] == ')' and (i+2) < len(regExp)):
                cont = i+2
                while(regExp[cont] != '(' and regExp[cont] not in chars):
                    if(regExp[cont] in ('*', '+', ',', '$')):
                        endOfExp = True
                        break
                    cont+=1
                    if(cont == len(regExp)):
                        endOfExp = True
                        break
                if(not endOfExp):
                    regExp = insertInTheMiddle(regExp, '$', cont)
        i+=1;
        size = len(regExp)
    return regExp
            

def insertInTheMiddle(s, word, i):
    return s[:i] + word + s[i:]

def createAcceptedChars():
    chars = [chr(i) for i in range(ord('A'),  ord('Z') + 1)]
    chars += [chr(i) for i in range(ord('a'), ord('z') + 1)]
    chars += [chr(i) for i in range(ord('0'), ord('9') + 1)]
    chars += ['\n', ' ', 'á', 'é', 'í', 'ó', 'ú', '&']
    return chars

def operatorValue(op):
    switcher = {
        '*':1,
        '+':2,
        '' :3,
        ',':4
    }
    return switcher.get(op,-1)

def printPostfix(root,s):
    if(root.left != None):
        s = printPostfix(root.left,s)
    if(root.right != None):
        s = printPostfix(root.right,s)
    return s + root.data

print(printPostfix(postfixNotation('ab,cd'), ''))
