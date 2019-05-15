
def parse(matTrans, finalSt, text, alf):
    current_state = 0
    strResult = ""
    listResult = []

    for cadena in text:
        for i in range(len(cadena)):
            sub = cadena[i:]
            current_state = 0
            strResult = ""
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
    

                    


    
    