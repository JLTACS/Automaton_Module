""" Authors: Jose Luis Torrentera Arroniz
             Omar Antonio Madriz Almanza
    Module 3: Transforms a Non-Deterministic Finite Automaton with epsilon transitions (NFA-e)
              into a Non-Deterministic Finite Automaton(NFA)
              In: alphabet, NFA-e transition table, initial state, final states
              Out: alphabet, NFA transition table, initial state, final states """

import M2

def NFAconverter(alphabet, transMatrix, initial_state, final_state):
    newMatrix = transMatrix.copy()
    newFinals = set()
    newFinals.add(final_state)
    
    e_closure = set()
    E_closure(transMatrix, initial_state, e_closure)

def E_closure(transMatrix, currState, e_closure, e_index = 0):
    if(transMatrix[currState][-1][e_index] == None):
        e_closure.add(currState)
        return
    else:
        e_closure.add(currState)
        for i in range(len(transMatrix[currState][-1])):
            nextState = transMatrix[currState][-1][i]
            E_closure(transMatrix, nextState, e_closure)    


e_closure = set()
matrix =     [[[233], [1,2]],
             [[100], [4]],
             [[10],  [None]],
             [[4], [None]],
             [[None], [None]]]

E_closure(matrix,0,e_closure)
print(e_closure)
# alphabet, transMatrix, init_state, final_state = M2.regularExpressionToNFA_e('ab*$**')
# NFAconverter(alphabet, transMatrix, init_state, final_state)