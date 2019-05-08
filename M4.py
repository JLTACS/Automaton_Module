#Convertir de un AFN a un AFD
#Posible modificación, omitir oldInitial, simplemente poner 0.
#Posible modificación, checar el tipo de dato en la matriz de transición del AFN
""" Authors: Jose Luis Torrentera Arroniz
             Omar Antonio Madriz Almanza
    Module 4: Transforms a Non-Deterministic Finite Automaton (NFA)
              into a Deterministic Finite Automaton(DFA)
              In: NFA transition table, final states
              Out:  DFA transition table, final states """

def afdConverter(oldTransition,  oldFinal):
    newStates = {}
    newFinals = set()
    newTransition = []
    lastNewState = 0
    alfSize = len(oldTransition[0])

    #inicializar matriz y estados 
    newTransition.append([None]*alfSize)
    newStates[lastNewState] = set([0])

    #Checar si estado inical se encuentra en los finales
    if 0 in oldFinal:
        newFinals.add(lastNewState)
    
    st = 0
    size = len(newTransition)

    while st < size:
        #oldSt = newStates.keys()[newStates.values().index[st]]              #Revisar los estados originales que representa el estado
        oldSt = newStates[st]
        for alf in range(alfSize):
            tempSt = set()                                                  #Producir la union de la producción de los estados contenidos en el nuevo estado
            for q in oldSt:
                tempList = oldTransition[q][alf]
                # if type(tempList) is int :
                #     tempList = [tempList]
                # elif tempList == None:
                #     tempList = []
                tempSt = tempSt.union(set(tempList))

            if tempSt not in newStates.values():                                     #Revisar si el estado obtenido existe
                lastNewState += 1
                newStates[lastNewState] = tempSt
                if (not oldFinal.isdisjoint(tempSt)):
                    newFinals.add(lastNewState)
                newTransition.append([None]*alfSize)
            newTransition[st][alf] = list(newStates.keys())[list(newStates.values()).index(tempSt)] 
        st += 1
        size = len(newTransition)
    
    return newTransition, newFinals


            
                

            



    


