"""	Lab05Ejercicio3.py​ (Version Robusta)
	DESCRIPCION: Programa que recibe una secuencia de enteros terminada en 0 \
	provista por el teclado, donde sólo aparecen los valores del conjunto {1,2,3,4},\
	contar para cada valor del conjunto, cuántas veces aparece dentro de la secuencia.
			
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 20/02/2018
	VARIABLES:
	N: int // ENTRADA: Nuevo numero del conjunto, se le contaran sus ocurrencias.
	A: int // Valor que almacena las ocurrencias de 1.
	B: int // Valor que almacena las ocurrencias de 2.
	C: int // Valor que almacena las ocurrencias de 3.
	D: int // Valor que almacena las ocurrencias de 4.
	i: int // Numero de veces que se aplica el proceso.
	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine.
	
"""
import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# Verificacion de la Precondicion (version robusta)

while True: # Se permite al usuario introducir nuevos datos correctos
	try: 
		N=int(input("Ingrese el numero: "))
		assert( N in range(5) )
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("el numero debe pretenecer al conjunto {1,2,3,4}")

# Inicializaciones del ciclo
A,B,C,D,i=0,0,0,0,0
cota = 100-i

# Verificacion de invariante al inicio del ciclo
try:
	assert( ( i < 101 ) )
except:
	print("Hubo un error en el invariante para los siguientes valores")
	print("proceso numero="+str(i))
	sys.exit()
# Verificacion de cota al inicio
try:
	assert( cota >= 0 )
except:
	print("Error cota no positiva: ")
	print("cota="+str(cota))
	sys.exit()

while N!=0:
	if N==1:
		A+=1
	elif N==2:
		B+=1
	elif N==3:
		C+=1
	elif N==4:
		D+=1
	i+=1
	while True: # Se permite al usuario introducir nuevos datos correctos
		try: 
			N=int(input("Ingrese el siguiente numero: "))
			assert( N in range(5) )
			break
		except:
			print("Error en los datos, debe volver a introducirlos")
			print("el numero debe pretenecer al conjunto {1,2,3,4}")
	# Verificacion de invariante en cada iteracion
	try:
		assert( ( i<101 ) )
	except:
		print("Hubo un error en el invariante para los siguientes valores")
		print("proceso numero="+str(i))
		sys.exit()
	# Verificacion de cota decreciente en cada iteración
	try:
		assert( cota > 100-i )
	except:
		print("Error cota no decreciente : ")
		print("cota anterior ="+str(cota)+" nueva cota ="+str(100-i))
		sys.exit()
	cota = 100-i
	# Verificacion de cota positiva en cada iteración
	try:
		assert( cota >= 0 )
	except:
		print("Error cota no positiva: ")
		print("cota="+str(cota))
		sys.exit()

# Postcondicion: 
try:
	assert( ( i<101 ) )
except:
	print("No se cumple la postcondicion con los valores ")
	print("proceso numero="+str(i))
	sys.exit() # Se aborta el programa, pues no cumple la post
# Salida:
print("1,2,3,4 ocurren:",A,B,C,D,"veces respectivamente")