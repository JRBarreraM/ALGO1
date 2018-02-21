"""	Lab05Ejercicio1.py​ (Version Robusta)
	DESCRIPCION: Programa que dado una secuencia de números entero, \
	verifica si estan ordenados de forma creciente.\
	Para ello utiliza dos variables una para almacenar el valor \
	del numero de la secuencia que el usuario ingresa y otra para su \
	predecesor.
			
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 20/02/2018
	VARIABLES:
	c: int // ENTRADA: Nuevo elemento de la secuencia.
	orden: bool // Dice si la secuencia esta ordenada o no.
	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine.
	i: int // Permite contar el numero de procesos.
	b: int // Toma el valor del anterior de la secuencia.
	R: str // SALIDA: Dice si la secuencia esta ordenada o no.
"""
import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# Verificacion de la Precondicion (version robusta)

while True: # Se permite al usuario introducir nuevos datos correctos
	try: 
		c=int(input("Ingrese el siguiente numero: "))
		assert(c>=0)
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("N debe pretenecer a los enteros positivos")

# Inicializaciones del ciclo
orden,i,b,R = True,0,0,""
cota = 100-i
# Verificacion de invariante al inicio del ciclo
try:
	assert( ( i < 100 ) )
except:
	print("Hubo un error en el invariante para los siguientes valores")
	print("numero="+str(i))
	sys.exit()
# Verificacion de cota al inicio
try:
	assert( cota >= 0 )
except:
	print("Error cota no positiva: ")
	print("cota="+str(cota))
	sys.exit()

while i<100 and c>=0:
	if i==0 and c==0:
		print("No se admite la secuencia vacia, comienza de nuevo")
		while True: # Se permite al usuario introducir nuevos datos correctos
			try: 
				c=int(input("Ingrese el siguiente numero: "))
				assert(c>0)
				break
			except:
				print("Error en los datos, debe volver a introducirlos")
				print("N debe pretenecer a los enteros positivos")
	elif i==1 and c==0:
		print("No se admite la secuencia unitaria, comienza de nuevo")
		while True: # Se permite al usuario introducir nuevos datos correctos
			try: 
				c=int(input("Ingrese el siguiente numero: "))
				assert(c>0)
				break
			except:
				print("Error en los datos, debe volver a introducirlos")
				print("N debe pretenecer a los enteros positivos")

	elif c==0:
		break
	orden=(c>b)
	if orden==False:
		R="NO"
	i+=1
	b=c
	while True: # Se permite al usuario introducir nuevos datos correctos
		try: 
			c=int(input("Ingrese el siguiente numero: "))
			assert(c>=0)
			break
		except:
			print("Error en los datos, debe volver a introducirlos")
			print("N debe pretenecer a los enteros positivos")

	# Verificacion de invariante en cada iteracion
	try:
		assert( ( i<100 ) )
	except:
		print("Hubo un error en el invariante para los siguientes valores")
		print("numero="+str(i))
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
	assert( ( i<100 ) )
except:
	print("No se cumple la postcondicion con los valores ")
	print("entero numero="+str(i))
	sys.exit() # Se aborta el programa, pues no cumple la post

# Salida:
print("La lista",R,"esta ordenada estrictamente creciente")