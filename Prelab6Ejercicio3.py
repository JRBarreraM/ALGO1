
"""	Prelab6Ejercicio3.py
	DESCRIPCION: Programa que dado un número entero N, \
	cuenta los divisores de N. Con una precondicion robusta.
			
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 03/03/2018
	VARIABLES:
	N: int // ENTRADA: Numero al que se le contaran los divisore.
	cuenta: int // SALIDA: Numero de divisores.
	
"""
import sys    # Se importa la libreria sys para poder utilizar sys.exit()
# Definicion de productoria
# Descripcion: Funcion que el numero de divisores de N.
# Parametros: 
def cuenta(N: int) -> int:
# PRECONDICION: True
	k,cuenta=1,0
	while k<=N:
		if (N % k) == 0:
			cuenta += 1
		k += 1
	return cuenta
# var cuenta: int // variable auxiliar numero de divisores de N
# var k: int // variable para recorrer el los valores entre 0 y N
# POSTCONDICION: True(misma del programa)
# Verificacion de la Precondicion (version robusta)

while True: # Se permite al usuario introducir nuevos datos correctos
	try: 
		N=int(input("Ingrese el valor de N: "))
		assert(N>0)
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("N debe pretenecer a los naturales positivos")

cuenta=cuenta(N)

# Postcondicion: 
try:
	assert( cuenta == sum ( 1 for j in range(1,N+1) if (N % j == 0) ) )
except:
	print("No se cumple la postcondicion con los valores ")
	print("cuenta="+str(cuenta))
	sys.exit() # Se aborta el programa, pues no cumple la post

# Salida:
print( "Existen",cuenta,"divisores para",N )