"""Creación de diccionario de Alfabeto"""
def create_alf(str_alf):
	alf = {}
	n = 0
	for letter in str_alf:
		if letter != ";" and letter != "\n":
			alf[letter] = n
			n+=1
	return alf

"""Creación de conjunto de estados finales"""
def create_fstate(str_fstate):
	fstate = set(str_fstate)
	fstate.remove(";")
	fstate.remove("\n")
	return fstate

"""Creación de matriz de transición"""
def create_mxTran(f):
	mxTran = []
	for line in f:
		tl = [int(a) for a in line if a != ";" and a != "\n"]
		mxTran.append(tl)
	return mxTran

def main():
	f = open("input.txt")
	cadena = f.readline()					#Cadena de entrada
	dic_alf = create_alf(f.readline())		#Creación de alfabeto
	init_state = int(f.readline())			#Estado inicial
	set_fst = create_fstate(f.readline())	#Estados finales
	mxTran = create_mxTran(f)				#Creación de matriz de transición
	
	lis_cad = [dic_alf[i] for i in cadena if i != "\n"]  #Ajuste de cadena de entrada
	secuence = (str(init_state) + "/")    				 #Recorrido de estados
	current_state = init_state							 #Estado actual inicial

	for letter in lis_cad:
		next_state = mxTran[current_state][letter]  #Pasar al siguiente estado
		current_state = next_state				
		
			#Actualizar estado actual
		secuence += (str(current_state) + "/")		#Actualizar recorrido
	
	if str(current_state) in set_fst:			#Evaluar último estado
		print("Aceptada")
	else:
		print("No Aceptada")
		
	print("Secuencia de estados: " + secuence)	

main()