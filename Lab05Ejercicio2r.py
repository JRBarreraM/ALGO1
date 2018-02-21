"""	Lab05Ejercicio2.py​ (Version Robusta)
	DESCRIPCION: Programa que recibe un número natural A y determina \
	la cantidad de pasos que se deben hacer para llegar al número 4, \
	(principio de la secuencia 4,2,1) en cada paso se debe mostrar el \
	número de pasos y el valor actual de A.
			
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 20/02/2018
	VARIABLES:
	A: int // ENTRADA: Numero con el que se inicia la secuencia.
	N: int // Valor que permite operar sobre el valor de A.
	i: int // Numero de pasos (veces que se aplica el proceso).
	
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
N,i=A,0

# Verificacion de invariante al inicio del ciclo

try:
	assert( True )
except:
	print("Hubo un error en el invariante para los siguientes valores")
	print("paso numero="+str(i)+"entero numero="+str(N))
	sys.exit()

while N>4 or N<4:
	if (N%2)==0:
		N=(N//2)
	else:
		N=(3*N)+1
	i+=1
	print("vale",N,"luego del paso",i)

	# Verificacion de invariante en cada iteracion
	try:
		assert( True )
	except:
		print("Hubo un error en el invariante para los siguientes valores")
		print("paso numero="+str(i)+"entero numero="+str(N))
		sys.exit()

# Postcondicion: 
try:
	assert( N==4 )
except:
	print("No se cumple la postcondicion con los valores ")
	print("paso numero="+str(i)+"entero numero="+str(N))
	sys.exit() # Se aborta el programa, pues no cumple la post

# Salida:
print("Partiendo desde",A,"Luego de",i+2,"pasos se tiene la secuencia 4,2,1")