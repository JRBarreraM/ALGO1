"""	Prelab3ejercicio2.py
	DESCRIPCION: Programa que dado un número entero N, \
	cuenta los divisores de N.
		
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 27/01/2018
	VARIABLES:
	N: int // ENTRADA: Numero al que se le contaran los divisore.
	i: int // Valor que permite recorrer los enteros entre 1 y N.
	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine
	cuenta: int // SALIDA: Numero de divisores.
	
"""

# Valores iniciales:
N=int(input("Ingrese el valor de N: "))

# Precondicion: 
assert(N > 0)

# Inicializaciones del ciclo
cuenta, i = 0, 1
cota = N - i + 2

# Verificacion de invariante y cota al inicio
assert( (0<i<=N+1) and (cuenta == sum ( j for j in range(1,i) if (N % j ==0) ) ) )
assert(cota >= 0)

while i<=N:
	if (N % i) == 0:
		cuenta += 1
	else:
		pass
	i += 1

# Postcondicion: 
assert(cuenta == sum ( 1 for j in range(1,N+1) if (N % j ==0) ) )

# Salida:
print( "Existen",cuenta,"divisores para",N)