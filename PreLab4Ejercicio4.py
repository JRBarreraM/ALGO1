"""	Prelab4ejercicio4.py
	DESCRIPCION: Dado una que dada una matriz cuadrada
	NxN, comprueba si la matriz es diagonal. \
	Para ello lee los elementos de una matriz cuadrada 3 x 3,\
	los coloca en un arreglo multidimensional.
		
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 01/01/2018
	VARIABLES:
	diagonal: int // SALIDA: Si no varia la matriz es diagonal.
	M: // ENTRADA: Almacena cada uno de los elementos de la matriz.
	det: // Almacena el valor del determinante de la matriz.

"""
# Precondicion: 
assert(True)

M=[[int(input("M["+str(i)+","+str(j)+"]=")) for i in range(3)] for j in range(3)]
diagonal=0

#Cota=2-i
#Invariante
assert(0<=diagonal<=1)
#Operaciones del lazo
for i in range(3):
	for j in range(3):
		if ((i!=j) and (M[i][j]!=0)):
				diagonal=1
				break
				break

		# Invariante
		assert(0<=diagonal<=1)
		
# Postcondicion: 
det=(M[0][0]*(M[1][1]*M[2][2])+(M[0][1]*M[1][2]*M[2][0])+(M[1][0]*M[2][1]*M[0][2])\
	-(M[0][2]*M[1][1]*M[2][0])-(M[0][1]*M[1][0]*M[2][2])-(M[1][2]*M[2][1]*M[0][0]))
assert((diagonal==1) or (det==((M[0][0]*M[2][2]*M[1][1]))))

# Salida:
if (diagonal==0):
	print("Es una matriz diagonal")
elif (diagonal==1):
	print("No es una matriz diagonal")
