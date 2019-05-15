import M1
import M2
import M3
import M4
import M5
import M6

print("----M1------")
exp = "(padre,?)wwwcom"
pos_exp = M1.postfixNotation(exp)
print(pos_exp)
print("\n")

print("----M2------")
alf, matriz_Trans, init_st, final_st = M2.regularExpressionToNFA_e(pos_exp)
M2.printTransTable(matriz_Trans,alf)
print("\n")

print("----M3------")
matriz_Trans, final_st, alf = M3.NFAconverter(alf,matriz_Trans,init_st,final_st)
M2.printTransTable(matriz_Trans, alf)
print("\n")

print("----M4------")
matriz_Trans, final_st = M4.afdConverter(matriz_Trans, final_st)
M2.printTransTable(matriz_Trans, alf)
print("\n")

print("----M5------")
matriz_Trans, final_st =  M5.Minimize(matriz_Trans, final_st)
M2.printTransTable(matriz_Trans, alf)
print("\n")

print("----M6------")
f = open("input.txt",'r')
M6.parse(matriz_Trans,final_st,f,alf)
f.close()
print("\n")