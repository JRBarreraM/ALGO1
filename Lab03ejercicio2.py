"""	Lab03ejercicio2.py

	DESCRIPCION:Dado un entero positivo n escriba un programa que diga si\
	el entero es primo. Un número n es primo si sólo es divisible por 1 y n.\
	Además, el programa imprime los divisores de n (distintos de 1 y n)\
	a medida que consigue un divisor. Finalmente, se imprime si n es primo o no.

	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 30/01/2018
	VARIABLES:
	o: str // ENTRADA: Almacena la decision s/n.
"""
# Valores iniciales:
n=int(input("Introduzca el numero: "))

# Precondicion: 
assert(n >= 2)

# Inicializaciones del ciclo
k=1
cota=n-k

# Verificacion de invariante y cota al inicio

#assert( True )
assert( cota >= 0)

while ( n >= k ):
	if (n % k == 0):
		print(k) 
		k=k+1
	else:
		k=k+1
   
	# Verificacion de invariante y cota en cada iteracion
	#assert( True )
	assert( cota > n-k )
	cota = n-k
   
# Postcondicion: 
#assert(  )
 
# Salida:
#if 