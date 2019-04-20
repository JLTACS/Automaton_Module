""" Authors: Jose Luis Torrentera Arroniz
             Omar Antonio Madriz Almanza
    Module 2: Transforms a regular expression in postfix 
              notation into a Non Deterministic Finite Automaton (NFA-e)
              In: Regular expression in Postfix notation.
              Out: NFA-e transitions table  """ 

class Node:
    def __init__(self, data, left, right, parent):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

""" Constructs the tree representation of a
    regular expression in postfix notation.  """
def treeConverter(string,index,parent = None):
    N = Node(string[index],None,None,parent)
    if(string[index] in ('$',',')):
        newInd, N.right = treeConverter(string, index-1,N) 
        newInd, N.left = treeConverter(string, newInd, N)
    elif(string[index] in ('*','+')):
        newInd, N.right = treeConverter(string, index-1,N)
    else:
        return (index-1), N
    return newInd, N 

def printPostfix(root,space):
    print(space + root.data)
    if(root.left != None):
        printPostfix(root.left,space + "  ")
    if(root.right != None):
        printPostfix(root.right,space + "  ")

""" Creates an alphabet dictionary to assign a numeric representation
    to the accepted characters. """
def create_alf_dict(str_alf):
    alf = {}
    n = 0
    for letter in str_alf:
        if(letter not in ('*', '+', ',', '$')):
            alf[letter] = n
            n += 1
    alf['eps'] = n+1
    return alf

def regularExpressionToDFA_e(regExp):
    init_state = 0
    final_state = 1
    alphabet = create_alf_dict(regExp)
    ind, RETreeRoot = treeConverter(regExp,len(regExp)-1)
    dropUnused(ind)
    transMatrix = [[None for i in range(len(alphabet))],[None for i in range(len(alphabet))]]

    currNode = RETreeRoot
    currState = init_state
    nextState = final_state
    NodeStack = []
    OpStack = []
    StateQueue = []
    leftLeave = False
    finish = False
    leave = False

    while(not finish):
        if(currNode.data not in alphabet):
            op = currNode.data
            leave = False
            leftLeave = False
        else:
            if(not leave):
                leave = True
            else:
                op = OpStack.pop()
        if(currNode.left == None and currNode.right == None):
            if(op == ','):
                if(not leftLeave):
                    nextState = StateQueue.pop()
                    transMatrix[currState][alphabet[currNode.data]] = nextState
                    leftLeave = True
                else: 
                    transMatrix[currState][alphabet[currNode.data]] = nextState
                    currState = nextState
                if(len(NodeStack) != 0):
                    currNode = NodeStack.pop()
            elif(op == '$'):
                nextState = StateQueue.pop()
                if(not leftLeave):                 
                    initialState = currState
                    transMatrix[currState][alphabet[currNode.data]] = nextState
                    currState = nextState   
                    leftLeave = True
                else:
                    transMatrix[currState][alphabet[currNode.data]] = nextState
                    if(len(NodeStack) > 0 and currNode.parent.parent.data == ','):
                        currState = initialState
                    else:
                        currState = nextState
                if(len(NodeStack) != 0):
                    currNode = NodeStack.pop()
            elif(op == '*'):
                pass
            elif(op == '+'):
                pass
        else:
            if(op in ('$', '*')):
                transMatrix.append([None for i in range(len(alphabet))])
                newState = len(transMatrix) - 1
                StateQueue.append(nextState)
                nextState = newState
            elif(op == ','):
                StateQueue.append(nextState)                

            NodeStack.append(currNode.right)
            OpStack.append(currNode.data)
            currNode = currNode.left    
        if(currState == final_state or (len(NodeStack) == 0 and len(OpStack) == 0)):
            finish = True
    printTransTable(transMatrix, alphabet)    

def dropUnused(i):
    pass

def printTransTable(Matrix, alphabet):
    for i in range(len(Matrix)):
        print(str(i) + str(Matrix[i]))

regularExpressionToDFA_e('abc$,')

