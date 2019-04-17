##Minimize
""" Authors: Jose Luis Torrentera Arroniz
             Omar Antonio Madriz Almanza
    Module 4: Minimize DFA with equivalent States
              In: DFA transition table, final states
              Out:  DFA transition table, final states """
def getCombinations(elements):
    combinations = []

    for i in range(len(elements)):
        for j in range(i+1,len(elements)):
            combinations.append((elements[i],elements[j]))
    
    return combinations
    

def getEquivalentStates(oldTransition, oldFinal):
    nonFinal = set(range(len(oldTransition)))
    nonFinal = list(nonFinal.difference(oldFinal))
    final = list(oldFinal)

    possibleEqual = getCombinations(nonFinal)
    if len(final) > 1:
        possibleEqual.extend(getCombinations(final))

    while(True):
        stop = True
        for q in possibleEqual:
            removed = False
            for alf in range(len(oldTransition[0])):
                temp_a = oldTransition[q[0]][alf]
                temp_b = oldTransition[q[1]][alf]

                if temp_a != temp_b and ((temp_a,temp_b) not in possibleEqual) and ((temp_b,temp_a) not in possibleEqual):
                    possibleEqual.remove(q)
                    removed = True
                if removed:
                    break
            if removed:
                stop = False
        if stop:
            break
    
    #Checar que pasa cuando hay dos eliminaciones en medio
    possibleEqual.sort(reverse = True)
    for eq in possibleEqual:
        if eq[1] < len(oldTransition):
            for st in range(len(oldTransition)):
                temp = [x if x != eq[1] else eq[0] for x in oldTransition[st]]
                oldTransition[st] = temp
            
            for st in range(len(oldTransition)):
                temp = [x-1 if x > eq[1] else x for x in oldTransition[st]]
                oldTransition[st] = temp
            
            oldTransition.pop(eq[1])
    
    #Checar que onda con los estados finales
    return oldTransition
    


afd = [[1, 4], [2, 5], [7, 7], [7, 3], [5, 6], [7, 7], [7, 6],[7,7]]
finals = {5,6,7}


getEquivalentStates(afd,finals)