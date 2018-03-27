""" Lab08Ejercicio2.py
	DESCRIPCION: Programa, que dado  un arreglo de enteros calcula \
	el número de veces que un entero k aparece en el arreglo.

	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 26/03/2018
		VARIABLES:
	N: int // Tamaño del arreglo.
	A: list // Lista de enteros.
	k: int // Entero del que se buscan sus repeticiones.
	tam: int // Tamaño del sub-arreglo donde se busca a k,
				que decrece cada que se llama a la funcion.

"""

#Definicion de subprogramas

# Descripcion: Cuenta el numero de ocurrencias de un entero en un arreglo.
# Parametros:
def nroRepeticiones(A=list,tam=int,k=int)->int:
#{ ​Pre:​ N > 0 }
#{ ​Post:​ r = (#i: 0<=i<tam: A[i]=k) }
#{ ​Cota:​ tam }
	#VARIABLES
		# r: int // Numero de repeticiones de k.
	if tam==0:
		if A[tam]==k :
			r=1
		else:
			r=0
		return r
	else:
		if A[tam]==k :
			r=1
		else:
			r=0
		return r+nroRepeticiones(A,tam-1,k)

#INICIO DEL PROGRAMA

#Valores inciales version robusta
while True:
	try:
	   k = int(input("Entero que se busca:"))
	   assert(int(k))
	   break
	except:
	   print("Error: k debe ser un entero ")

while True:
	try:
		N = int(input("Tamaño del arreglo donde se busca:"))
		assert(N>=0)
		break
	except:
		print("Error: El arreglo debe contener al menos un elemento")

print("Introduzca los elementos del arreglo:")

A = [int(input("A["+str(i)+"]=")) for i in range(N)]

tam=N-1

#Calculos y Salida
print(k,"aparece",nroRepeticiones(A,tam,k),"veces en el arreglo")