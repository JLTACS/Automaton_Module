
def parse(matTrans, finalSt, text, alf):
    current_state = 0
    strResult = ""
    listResult = []
    errorState = geterror_state(matTrans, finalSt)

    for cadena in text:
        for i in range(len(cadena)):
            sub = cadena[i:]
            current_state = 0
            strResult = ""
            if '&' in alf:
                recursive_parse(sub,0,current_state,errorState,listResult,alf, matTrans, finalSt)
            else:
                for letter in sub:
                    strResult += letter

                    if letter not in alf:
                        break
                    next_state = matTrans[current_state][alf[letter]]
                    current_state = next_state

                    if current_state in finalSt:
                        listResult.append(strResult)
    
    f = open("resultados.txt", 'w')
    for rs in listResult:
        f.write(rs + '\n')
    f.close()
    

def geterror_state(matTrans, finalSt):
    errorState = set()
    for i in range(len(matTrans)):
        temp = set(matTrans[i])
        if len(temp) == 1 and i in temp:
            if i not in finalSt:
                errorState.add(i)
    
    return errorState

def recursive_parse(sub,i,current_state, error_state, listResult,alf, matTrans, finalSt):
    if i == len(sub):
        return
    if current_state in error_state:
        return
    if sub[i] in alf:
        state_alf = matTrans[current_state][alf[sub[i]]]
        if state_alf in finalSt:
            listResult.append(sub[:i+1])
        recursive_parse(sub,i+1,state_alf, error_state, listResult, alf, matTrans, finalSt)
    
    state_wild = matTrans[current_state][alf['&']]
    if state_wild in finalSt:
            listResult.append(sub[:i+1])
    recursive_parse(sub,i+1,state_wild, error_state, listResult, alf, matTrans, finalSt)


#recibe(sub, i, state)
#if i == len(sub) 
    #return
#if letter in alf: state con alf letter checar si es final str


    
    