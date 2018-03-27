""" Lab08Ejercicio3.py
	DESCRIPCION: Programa, que dado dada una matriz de NxN de ceros y unos,\
	calcule el número de casillas no nulas (diferentes de cero) de la matriz.

	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 26/03/2018
		VARIABLES:
	N: int // Tamaño de la matriz.
	A: list // La Matriz .
	fil: int // Fila donde se busca, decrece con cada llamada a la funcion.
	col: int // Columna donde se busca, decrece con cada llamada a la funcion.
"""

# Definicion de subprogramas

# Descripcion: Cuenta el numero de casillas no nulas de una matriz NxN.
def numNoNulas(A=list,fil=int,col=int)->int:
# { ​Pre:​ (∀i,j: 0≤i,j<N : 0≤A[i][j]≤1) }
# { ​Post:​ num = (#i,j: 0≤i,j<N: matriz[i][j]≠0) }
# { ​Cota:​ fil }
 	#VARIABLES
		# num: int // Numero de casillas no nulas por fila.
	if fil==0:
		return numNoNulasCol(A,0,col)
	else:
		num=numNoNulasCol(A,fil,col)
		return num+numNoNulasCol(A,fil-1,col)

# Descripcion: Cuenta el numero de casillas no nulas de una columna.
# Parametros:
def numNoNulasCol(A=list,fil=int,col=int)->int:
# { ​Pre:​ True }
# { ​Post:​ r = (#i: 0<=i<col: A[fil][i]!=0) }
# { ​Cota:​ col }
 	#VARIABLES
		# r: int // Numero de casillas no nulas en columna.
	if col==0:
		if A[fil][col]==0:
			r=0
		else:
			r=1
		return r
	else:
		if A[fil][col]==0:
			r=0
		else:
			r=1
		return r+numNoNulasCol(A,fil,col-1)

#INICIO DEL PROGRAMA

#Valores inciales version robusta
while True:
	try:
		N = int(input("Tamaño de la matriz cuadrada:"))
		assert(N>0)
		break
	except:
		print("Error: Tamaño No Entero Positivo")

print("Introduzca los elementos de la matriz:")

A=[[int(input("A["+str(i)+","+str(j)+"]=")) for i in range(N)] for j in range(N)]

fil,col=N-1,N-1

#Calculos y Salida
print("Hay",numNoNulas(A,fil,col),"casillas no nulas en la matriz")