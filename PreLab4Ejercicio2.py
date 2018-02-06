"""	Prelab4ejercicio2.py
	DESCRIPCION:Dado un arreglo A de N enteros, \
	calcule la suma de los elementos del arreglo.
	Para ello se solicita los N enteros, como input,\
	luego los coloca en un arreglo A.
	
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 01/01/2018
	VARIABLES:
	N: int // ENTRADA: Almacena el entero de entrada.
	A: array // Almacena el tamaño del arreglo.
	suma: int // SALIDA: Valor de la suma de los elementos del arreglo.
	i: int // Valor que permite operar entre 0 y N.
"""
# Valores iniciales:
N=int(input("Introduzca el tamaño del arreglo: "))

# Precondicion: 
assert(N>0)

A=[int(input("A[" + str(i) + "]= ")) for i in range(N)]
suma=0
#Cota=N-i
#Invariante
assert(N==len(A))

# operaciones del lazo
for i in range(N):
	suma+=A[i]
	# Invariante
	assert(N==len(A))
		
# Postcondicion: 
assert(suma==sum(A[i] for i in range(N)))

# Salida:
print("La adicion de los elementos del arreglo es",suma)