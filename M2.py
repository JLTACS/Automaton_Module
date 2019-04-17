""" Authors: Jose Luis Torrentera Arroniz
             Omar Antonio Madriz Almanza
    Module 2: Transforms a regular expression in postfix 
              notation into a Deterministic Finite Automaton (DFA-e)
              In: Regular expression in Postfix notation.
              Out: DFA-e transitions table  """ 

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
    alf[None] = n+1
    return alf

def regularExpressionToDFA_e(regExp):
    init_state = 0
    final_state = 1
    epsilon = None
    alphabet = create_alf_dict(regExp)
    operators = ['*', '+', ',', '$']
    ind, RETreeRoot = treeConverter(regExp,len(regExp)-1)
    transMatrix = [[],[]]

    currNode = RETreeRoot
    currState = init_state
    nextState = final_state
    finish = False

    while(not finish):
        op = currNode.data
        if(op == ','):
            if(currNode.left.data not in operators and currNode.right.data not in operators):
                transMatrix[currState].insert(alphabet[currNode.left.data],nextState)
                transMatrix[currState].insert(alphabet[currNode.right.data],nextState)
            elif(currNode.left.data not in operators):
                transMatrix[currState].insert(alphabet[currNode.left.data],nextState)
                currNode = currNode.right
            elif(currNode.right.data not in operators):
                transMatrix[currState].insert(alphabet[currNode.right.data],nextState)
                currNode = currNode.left
        finish = True
    print(transMatrix)    



regularExpressionToDFA_e('ab,')

