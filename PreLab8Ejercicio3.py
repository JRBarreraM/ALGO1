""" PreLab8Ejercicio1.py
	DESCRIPCION: Programa, que por cada línea leída desde un archivo, \
	determine cuántas de sus palabras son palíndromos. 

	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 18/03/2018
		VARIABLES:
	A: list // Lista de palabras por linea.
	palindromo: int // Numero de palindromos del archivo.	
"""

# Descripcion: Funcion verifica si un str es un palindromo.
# Parametros:
def palindromo(S=str)-> bool:
# PRECONDICION: True
# var L: int // tamaño del str de entrada
	if len(S)==0 or len(S)==1:					#Casos Base de la recursion str vacio y unitario
		return True
	else:
		if S[0]==S[len(S)-1]:
			S = S[:-1]					#Se elimina el ultimo elemento
			S = S.replace(S[0],"",1)	#Se elimina el primer elemento
			return palindromo(S)		#del primer elemento con un str vacio
		else:
			return False
# POSTCONDICION: (%forall i : 0<=i<L : S[0]=S[L-1])=>True

##################################
# Inicio del programa 
##################################
# Valores iniciales:
F=str(input("Ingrese el nombre completo del archivo (ruta):"))
palindromos=0

with open(F) as f:
	for line in f:
		print(line, end="")		#se muestra el contenido del archuvo input.txt al usuario
	print("\n")
f.closed

with open(F) as f:
	for line in f:
		A=line.split()			#se separan las palabras en caso de que haya mas de una palabra por linea
		T=len(A)
		for i in range(T):
			if palindromo(A[i]):
				palindromos+=1
f.closed
#Salida
print("Hay",palindromos,"palindromos en el archivo",F)