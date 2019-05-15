""" Authors: Jose Luis Torrentera Arroniz
             Omar Antonio Madriz Almanza
    Module 1: Given a regular expression written in infix notation
              and transforms it into postfix notation.
    In: Regular Expression in infix notation
    Out: Regular Expression in postfix notation  """


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
            
""" Set '$' as a concatenation operator """
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

""" Sets the Alphabet """
def createAcceptedChars():
    chars = [chr(i) for i in range(ord('A'),  ord('Z') + 1)]
    chars += [chr(i) for i in range(ord('a'), ord('z') + 1)]
    chars += [chr(i) for i in range(ord('0'), ord('9') + 1)]
    chars += ['\n', ' ', 'á', 'é', 'í', 'ó', 'ú', '&','?']
    return chars

""" Sets Operators priority """
def operatorValue(op):
    switcher = {
        '*':1,
        '+':2,
        '$':3,
        ',':4
    }
    return switcher.get(op,-1)

# postF = postfixNotation('hscripts&+')
# print(postF)

