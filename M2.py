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
    operators = ['*', '+', ',', '$']
    ind, RETreeRoot = treeConverter(regExp,len(regExp)-1)
    dropUnused(ind)
    transMatrix = [[None for i in range(len(alphabet))],[None for i in range(len(alphabet))]]

    currNode = RETreeRoot
    currState = init_state
    nextState = final_state
    NodeStack = []
    OpStack = []

    while(1):
        if(currNode.data not in alphabet):
            op = currNode.data
        else:
            if(len(OpStack) != 0): 
                op = OpStack.pop()
        if(op == ','):
            if(currNode.left.data not in operators and currNode.right.data not in operators):
                transMatrix[currState][alphabet[currNode.left.data]] = nextState
                transMatrix[currState][alphabet[currNode.right.data]] = nextState
            elif(currNode.right.data not in operators):
                transMatrix[currState][alphabet[currNode.right.data]] = nextState
                currNode = currNode.left
            elif(currNode.left.data not in operators):
                transMatrix[currState][alphabet[currNode.left.data]] = nextState
                currNode = currNode.right
            else:
                NodeStack.append(currNode.left)
                currNode = currNode.right
        elif(op == '$'):
            if(currNode.left == None and currNode.right == None):
                if(len(NodeStack) != 0):
                    transMatrix.append([None for i in range(len(alphabet))])
                    newState = final_state
                    final_state = len(transMatrix) - 1
                    transMatrix[currState][alphabet[currNode.data]] = newState
                    currState = newState
                    currNode = NodeStack.pop()
                else:
                    transMatrix[currState][alphabet[currNode.data]] = final_state
                    currState = final_state
                    break
            else:
                NodeStack.append(currNode.right)
                OpStack.append(currNode.data)
                currNode = currNode.left

        elif(op == '*'):
            pass
        elif(op == '+'):
            pass
    
    printTransTable(transMatrix, alphabet)    

def dropUnused(i):
    pass

def printTransTable(Matrix, alphabet):
    for i in range(len(Matrix)):
        print(str(i) + str(Matrix[i]))

regularExpressionToDFA_e('ab$cd$$')

