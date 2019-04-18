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
    isleave = False
    NodeStack = []
    StateStack = []

    while(1):
        if(isleave):
            if(len(NodeStack) != 0):
                currNode = NodeStack.pop()
                nextState = StateStack.pop()
            else:
                break
        op = currNode.data
        isleave = False
        if(op == ','):
            if(currNode.left.data not in operators and currNode.right.data not in operators):
                transMatrix[currState][alphabet[currNode.left.data]] = nextState
                transMatrix[currState][alphabet[currNode.right.data]] = nextState
                isleave = True
            elif(currNode.right.data not in operators):
                transMatrix[currState][alphabet[currNode.right.data]] = nextState
                currNode = currNode.left
            elif(currNode.left.data not in operators):
                transMatrix[currState][alphabet[currNode.left.data]] = nextState
                currNode = currNode.right
            else:
                StateStack.append(nextState)
                NodeStack.append(currNode.left)
                currNode = currNode.right
        elif(op == '$'):
            if(currNode.left.data not in operators and currNode.right.data not in operators):
                transMatrix.append([None for i in range(len(alphabet))])
                if(len(NodeStack) == 0):
                    nextState = len(transMatrix) - 1
                    transMatrix[currState][alphabet[currNode.left.data]] = nextState
                    transMatrix[nextState][alphabet[currNode.right.data]] = final_state
                else:
                    transMatrix.append([None for i in range(len(alphabet))])
                    newState = len(transMatrix) - 2
                    nextState = len(transMatrix) - 1
                    transMatrix[currState][alphabet[currNode.left.data]] = newState
                    transMatrix[newState][alphabet[currNode.right.data]] = nextState
                currState = nextState
                isleave = True
            elif(currNode.left.data not in operators):
                transMatrix.append([None for i in range(len(alphabet))])
                newState = len(transMatrix) - 1
                transMatrix[currState][alphabet[currNode.left.data]] = newState
                currState = newState
                currNode = currNode.right
            elif(currNode.right.data not in operators):
                transMatrix.append([None for i in range(len(alphabet))])
                newState = len(transMatrix) - 1
                transMatrix[currState][alphabet[currNode.right.data]] = newState
                currState = newState
                currNode = currNode.left
            else:
                StateStack.append(nextState)
                NodeStack.append(currNode.right)
                currNode = currNode.left

        elif(op == '*'):
            pass
        elif(op == '+'):
            pass
    
    printTransTable(transMatrix)    

def dropUnused(i):
    pass

def printTransTable(Matrix):
    for i in range(len(Matrix)):
        print(str(i) + str(Matrix[i]))

regularExpressionToDFA_e('abc$,')

