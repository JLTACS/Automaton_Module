""" Authors: Jose Luis Torrentera Arroniz
             Omar Antonio Madriz Almanza
    Module 2: Transforms a regular expression in postfix 
              notation into a Non Deterministic Finite Automaton (NFA-e)
              In: Regular expression in Postfix notation.
              Out: NFA-e transitions table, alphabet, inital state, final state  """ 

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

""" Prints the tree representation of the regular expression """
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
    str_alf = set(str_alf)
    orden = sorted(str_alf)
    n = 0
    for letter in orden:
        if(letter not in ('*', '+', ',', '$')):
            alf[letter] = n
            n += 1
    alf['eps'] = n
    return alf

def regularExpressionToNFA_e(regExp):
    init_state = 0
    final_state = 1
    alphabet = create_alf_dict(regExp)
    ind, RETreeRoot = treeConverter(regExp,len(regExp)-1)
    dropUnused(ind)
    transMatrix = [[[None] for i in range(len(alphabet))],[[None] for i in range(len(alphabet))]]
    createNFA(transMatrix, RETreeRoot, init_state, final_state, alphabet)

#    printTransTable(transMatrix, alphabet)
    return alphabet, transMatrix, init_state, final_state    

def createNFA(transMatrix, currNode, currState, nextState, alphabet):
    if(currNode == 'eps'):
        if(None in transMatrix[currState][alphabet[currNode]]):
            transMatrix[currState][alphabet[currNode]].remove(None)
        transMatrix[currState][alphabet[currNode]].append(nextState)
        return
    elif(currNode.data in alphabet):
        if(None in transMatrix[currState][alphabet[currNode.data]]):
            transMatrix[currState][alphabet[currNode.data]].remove(None)
        transMatrix[currState][alphabet[currNode.data]].append(nextState)
        return
    elif(currNode.data == '$'):
        transMatrix.append([[None] for i in range(len(alphabet))])
        createNFA(transMatrix, currNode.left, currState, len(transMatrix) - 1, alphabet)
        createNFA(transMatrix, currNode.right, len(transMatrix) - 1, nextState, alphabet)
    elif(currNode.data == ','):
        createNFA(transMatrix, currNode.left, currState, nextState, alphabet)
        createNFA(transMatrix, currNode.right, currState, nextState, alphabet)
    elif(currNode.data == '*'):
        transMatrix.append([[None] for i in range(len(alphabet))])
        createNFA(transMatrix, 'eps', currState, len(transMatrix) - 1, alphabet)
        createNFA(transMatrix, 'eps', len(transMatrix) - 1, nextState, alphabet)
        createNFA(transMatrix, currNode.right, len(transMatrix) - 1, len(transMatrix) - 1, alphabet)
    elif(currNode.data == '+'):
        createNFA(transMatrix, currNode.right, currState, nextState, alphabet)
        createNFA(transMatrix, 'eps', nextState, currState, alphabet)

def dropUnused(i):
    pass

def printTransTable(Matrix, alphabet):
    keys = list(alphabet.keys())
    title = "\t"
    for k in keys:
        title += k + '\t'
    print(title)
    for i in range(len(Matrix)):
        print(str(i) + '   ' + str(Matrix[i]))

# regularExpressionToNFA_e('ab*$**')

