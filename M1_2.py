class Node:
    def __init__(self, data, left, right, parent):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def treeConverter(string,indice,parent = None):
    N = Node(string[indice],None,None,parent)
    if(string[indice] in ('$',',')):
        newInd, N.right = treeConverter(string, indice-1,N) 
        newInd, N.left = treeConverter(string, newInd, N)
    elif(string[indice] in ('*','+')):
        newInd, N.right = treeConverter(string, indice-1,N)
    else:
        return (indice-1), N
    return newInd, N 

def postfixNotation(regExp):
    alphabet = createAcceptedChars()
    regExp = addConcatOp(regExp, alphabet)
    stack = []
    result = ""

    for i in range(len(regExp)):
        if(regExp[i] in alphabet):
            result += regExp[i]
        elif(regExp[i] == '('):
            stack.append(regExp[i])
        elif(regExp[i] in ('*', '+', ',', '$')):
            while(len(stack) != 0 and stack[-1] != '('):
                if(operatorValue(stack[-1]) < operatorValue(regExp[i])):
                    result += stack.pop()
                else:
                    break
            stack.append(regExp[i])
        elif(regExp[i] == ')'):
            while(len(stack) != 0 and stack[-1] != '('):
                result += stack.pop()
            if(len(stack) != 0):
                stack.pop()
            
    while(len(stack) != 0):
        result += stack.pop()    
    return result
            
def addConcatOp(regExp, chars):
    endOfExp = False
    i = 0
    size = len(regExp)
    while(i < size): 
        endOfExp = False
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
        i+=1
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
        '$':3,
        ',':4
    }
    return switcher.get(op,-1)

def printPostfix(root,space):
    print(space + root.data)
    if(root.left != None):
        printPostfix(root.left,space + "  ")
    if(root.right != None):
        printPostfix(root.right,space + "  ")

postF = postfixNotation('hscripts&+\n')
print(postF)
ind, root = treeConverter(postF,len(postF)-1)
printPostfix(root,"")