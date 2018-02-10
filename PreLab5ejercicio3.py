"""	Prelab5ejercicio3.py
	DESCRIPCION: Programa que dado un número entero N, \
	cuenta los divisores de N. Con una precondicion robusta.
			
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 10/02/2018
	VARIABLES:
	N: int // ENTRADA: Numero al que se le contaran los divisore.
	k: int // Valor que permite recorrer los enteros entre 1 y N.
	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine
	cuenta: int // SALIDA: Numero de divisores.
	
"""

# Verificacion de la Precondicion (version robusta)

while True: # Se permite al usuario introducir nuevos datos correctos
	try: 
		N=int(input("Ingrese el valor de N: "))
		assert(N>0)
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("N debe pretenecer a los naturales positivos")

# Inicializaciones del ciclo
cuenta, k = 0,1
cota = N-k+1

# Verificacion de invariante al inicio del ciclo
try:
	assert( ( 0<k<=N+1 ) and ( cuenta == sum ( 1 for j in range(1,k) if (N % j == 0) ) ) )
except:
	print("Hubo un error en el invariante para los siguientes valores")
	print("cuenta="+str(cuenta)+" k="+str(k))
	sys.exit()
# Verificacion de cota al inicio
try:
	assert( cota >= 0 )
except:
	print("Error cota no positiva: ")
	print("cota="+str(cota))
	sys.exit()

while k<=N:
	if (N % k) == 0:
		cuenta += 1
	k += 1
	
	# Verificacion de invariante en cada iteracion
	try:
		assert( ( 0<k<=N+1 ) and ( cuenta == sum ( 1 for j in range(1,k) if (N % j == 0) ) ) )
	except:
		print("Hubo un error en el invariante para los siguientes valores")
		print("cuenta="+str(cuenta)+" k="+str(k))
		sys.exit()
	# Verificacion de cota decreciente en cada iteración
	try:
		assert( cota > N+1-k )
	except:
		print("Error cota no decreciente : ")
		print("cota anterior ="+str(cota)+" nueva cota ="+str(N-k+1))
		sys.exit()
	cota = N+1-k
	# Verificacion de cota positiva en cada iteración
	try:
		assert( cota >= 0 )
	except:
		print("Error cota no positiva: ")
		print("cota="+str(cota))
		sys.exit()
# Postcondicion: 
try:
	assert( cuenta == sum ( 1 for j in range(1,N+1) if (N % j == 0) ) )
except:
	print("No se cumple la postcondicion con los valores ")
	print("cuenta="+str(cuenta)+" k="+str(N))
	sys.exit() # Se aborta el programa, pues no cumple la post

# Salida:
print( "Existen",cuenta,"divisores para",N )