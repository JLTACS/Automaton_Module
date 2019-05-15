""" Authors: Jose Luis Torrentera Arroniz
             Omar Antonio Madriz Almanza
    Module 3: Transforms a Non-Deterministic Finite Automaton with epsilon transitions (NFA-e)
              into a Non-Deterministic Finite Automaton(NFA)
              In: alphabet, NFA-e transition table, initial state, final states
              Out: alphabet, NFA transition table, initial state, final states """

import M2

def NFAconverter(alphabet, transMatrix, initial_state, final_state):
    newMatrix = [[[] for j in range(len(alphabet) - 1)] for i in range(len(transMatrix))]
    newFinals = set()
    newFinals.add(final_state)
    
    e_closure = set()

    for currState in range(len(transMatrix)):
        E_closure(transMatrix, currState, e_closure)
        if(not newFinals.isdisjoint(e_closure)):
                        newFinals.add(currState)
        keys = list(alphabet.keys())
        keys.remove('eps')
        stateSet = set()
        resultSet = set()

        for k in keys:
            for state in e_closure:
                for j in range(len(transMatrix[state][alphabet[k]])):
                    stateSet.add(transMatrix[state][alphabet[k]][j])
        
            for c in stateSet:
                if c != None:
                    E_closure(transMatrix, c, resultSet)
                    # if(not newFinals.isdisjoint(resultSet)):
                    #     newFinals.add(currState)
            resultlist = list(resultSet)
            for n in resultlist:
                newMatrix[currState][alphabet[k]].append(n)
            resultSet = set()       
            stateSet = set()
        e_closure = set()                                    
    
    alphabet.pop("eps")
    # M2.printTransTable(newMatrix, alphabet)
    return newMatrix, newFinals, alphabet


def E_closure(transMatrix, currState, e_closure, e_index = 0):
    if(transMatrix[currState][-1][e_index] == None):
        e_closure.add(currState)
        return
    else:
        e_closure.add(currState)
        for i in range(len(transMatrix[currState][-1])):
            nextState = transMatrix[currState][-1][i]
            E_closure(transMatrix, nextState, e_closure)    


# e_closure = set()
# matrix =     [[[0], [None], [1]],
#              [[None], [None], [2]],
#              [[3], [2], [None]],
#              [[None], [None], [None]]]

# alpha = {'a':0, 'b':1, 'eps':3}

# E_closure(matrix,0,e_closure)
# print(e_closure)
# alphabet, transMatrix, init_state, final_state = M2.regularExpressionToNFA_e('ab*$**')
#NFAconverter(alpha, matrix, 0, 3)