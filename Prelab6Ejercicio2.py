
"""	PreLab6ejercicio2.py
	DESCRIPCION: Programa que dado un número entero N, \
	calcula la suma de los factoriales desde 0 hasta N. \
	Con una precondicion robusta.
			
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 03/03/2018
	VARIABLES:
	N: int // ENTRADA: Numero al que se le contaran los factoriales de 0 a N.
	suma: int // SALIDA: Valor de la sumatoria del factorial de los enteros entre 0 y N.
"""
import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# Definicion de productoria
# Descripcion: Funcion que computa la productoria.
# Parametros: 
def fact( n: int ) -> int:
# PRECONDICION: True
	p = 1
	if n == 0:
		pass
	for i in range(1,n+1):
		p *= i
	return p
# var p: int // variable auxiliar valor de la productoria de la iteracion
# var i: int // variable para recorrer los valores entre 0 y n-1
# POSTCONDICION: True

# Definicion de suma
# Descripcion: Funcion que computa la suma de los factoriales entre 0 y N.
# Parametros: 
def suma(A: int) -> int:
# PRECONDICION: True
	k=0
	suma=0
	while(k<=A):
		suma += fact(k)
		k += 1
	return suma
# var suma: int // variable auxiliar valor de la suma de los factoriales de N
# var k: int // variable para recorrer el iterable
# POSTCONDICION: True

##################################
# Inicio del programa 
##################################

# Verificacion de la Precondicion (version robusta)

while True: # Se permite al usuario introducir nuevos datos correctos
	try: 
		N=int(input("Ingrese el valor de N: "))
		assert(N>=0)
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("N debe pretenecer a los naturales")

#Calculos:
suma = suma(N)
# Postcondicion: 
try:
	assert( suma == sum ( fact(i) for i in range(N+1) ) )
except:
	print("No se cumple la postcondicion con los valores")
	print(" suma="+str(suma))
	sys.exit()
# Salida:
print( "La suma de los factoriales de 0 a",N,"es",suma )