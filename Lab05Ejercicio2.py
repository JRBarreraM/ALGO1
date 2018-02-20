"""	Lab05Ejercicio1.py​
	DESCRIPCION: Programa que dado una secuencia de números entero, \
	verifica si estan ordenados de forma creciente. Con una precondicion robusta.
			
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 20/02/2018
	VARIABLES:
	N: int // ENTRADA: Numero al que se le contaran los divisore.
	k: int // Valor que permite recorrer los enteros entre 1 y N.
	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine
	cuenta: int // SALIDA: Numero de divisores.
	
"""
import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# Verificacion de la Precondicion (version robusta)

while True: # Se permite al usuario introducir nuevos datos correctos
	try: 
		A=int(input("Ingrese el numero: "))
		assert(A>0)
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("N debe pretenecer a los enteros positivos")

# Inicializaciones del ciclo
N,i = A,0

# Verificacion de invariante al inicio del ciclo

try:
	assert( True )
except:
	print("Hubo un error en el invariante para los siguientes valores")
	print("numero="+str(i))
	sys.exit()


while N>4 or N<4:
	if N%2==0:
		M=(N//2)
	else:
		M=3*N+1
	i+=1
	N=M
	print("vale",M,"en el paso",i)

	# Verificacion de invariante en cada iteracion
	try:
		assert( True )
	except:
		print("Hubo un error en el invariante para los siguientes valores")
		print("numero="+str(i))
		sys.exit()

# Postcondicion: 
try:
	assert( M==4 )
except:
	print("No se cumple la postcondicion con los valores ")
	print("entero numero="+str(i))
	sys.exit() # Se aborta el programa, pues no cumple la post

# Salida:
print("Luego de",i,"pasos",A,"llega a",M)