"""	PreLab5ejercicio2.py
	DESCRIPCION: Programa que dado un número entero N, \
	calcula la suma de los factoriales desde 0 hasta N. \
	Con una precondicion robusta.
			
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 10/02/2018
	VARIABLES:
	N: int // ENTRADA: Numero al que se le contaran los factoriales de 0 a N.
	k: int // Valor que permite recorrer los enteros entre 0 y N.
	fact: int // Valor donde se guardará el factorial del valor que posea k.
	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine.
	suma: int // SALIDA: Valor de la sumatoria del factorial de los enteros entre 0 y N-1.
"""
import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# Definicion de productoria
def prod( iterable ):
	p = 1
	for n in iterable:
		p *= n
	return p

# Verificacion de la Precondicion (version robusta)

while True: # Se permite al usuario introducir nuevos datos correctos
	try: 
		N=int(input("Ingrese el valor de N: "))
		assert(N>=0)
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("N debe pretenecer a los naturales")
		
# Inicializaciones del ciclo
suma,fact,k = 0,1,0
cota = N+1-k
# Verificacion de invariante al inicio del ciclo
try:
	assert( 0<=k<=N+1 \
	and ( suma == sum ( prod ( j for j in range(1,i+1) ) for i in range(0,k) ) ) \
	and ( fact == prod ( j for j in range(1,k) ) ) )
except:
	print("Hubo un error en el invariante para los siguientes valores")
	print("k="+str(k)+" suma="+str(suma)+" fact="+str(fact))
	sys.exit()
# Verificacion de cota al inicio
try:
	assert( cota >= 0 )
except:
	print("Error cota no positiva: ")
	print("cota="+str(cota))
	sys.exit()

while(k<=N):
	if( k>0 ):
		fact = fact*k
	else:
		pass
	suma = suma+fact
	k = k + 1
	
	# Verificacion de invariante en cada iteracion
	try:
		assert( 0<=k<=N+1 \
		and ( suma == sum ( prod ( j for j in range(1,i+1) ) for i in range(0,k) ) ) \
		and ( fact == prod ( j for j in range(1,k) ) ) )
	except:
		print("Hubo un error en el invariante para los siguientes valores")
		print("k="+str(k)+" suma="+str(suma)+" fact="+str(fact))
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
	assert( suma == sum ( prod( j for j in range(1,i+1) ) for i in range(0,N+1) ) )

except:
	print("No se cumple la postcondicion con los valores")
	print("k="+str(k)+" suma="+str(suma)+" fact="+str(fact))
	sys.exit()
# Salida:
print( "La suma de los factoriales de 0 a",N,"es",suma )