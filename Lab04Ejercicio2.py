"""	Lab04Ejercicio2.py
	DESCRIPCION: Programa calcula la suma de todos los elementos de\
	una matriz NxM dada por el usuario.

	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 09/02/2018
	VARIABLES:
	M: int // ENTRADA: Numero de filas de la matriz.
	N: int // ENTRADA: Numero de columnas de la matriz.
	P: array // Almacena los coeficientes del polinomio.
	i: int // Valor que permite recorrer los valores entre 0 y M.
"""

# Valores iniciales:
M=int(input("Numero de filas de la matriz: "))
N=int(input("Numero de columnas de la matriz: "))

# Precondicion: 
assert(M>0 and N>0)

P=[[int(input("P["+str(i)+","+str(j)+"]=")) for i in range(M)] for j in range(N)]

suma=0

# Cota=N-i
# Invariante
#assert(True)
#Operaciones del lazo
for i in range(N):
	for j in range(M):
		suma= suma + P[i][j]
		# Invariante
		#assert(True)

# Postcondicion: 
assert(suma==(sum(sum(P[i][j] for j in range(M)) for i in range(N))))

# Salida:
print("La suma de los elementos de la matriz",M,"x",N, "es =",suma)