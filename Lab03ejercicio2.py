"""	Lab03ejercicio2.py
	DESCRIPCION:Dado un entero positivo n dice si el entero es primo.\
	Un número n es primo si sólo es divisible por 1 y n.\
	Además, el programa imprime los divisores de n (distintos de 1 y n)\
	a medida que consigue un divisor. Finalmente, se imprime si n es primo o no.
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 31/01/2018
	VARIABLES:
	n: int // ENTRADA: Almacena el valor del numero dado.
	r: str // SALIDA: Dice si n es primo o no.
	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine.
	k: int // Valor que permite recorrer los enteros entre 2 y n-1.
	j: int // Valor que permite contar el numero de factores.
"""
# Valores iniciales:
n=int(input("Introduzca el numero: "))

# Precondicion: 
assert(n>0)

r="es primo"
j=0
if n>2:
	# Inicializaciones del ciclo
	k=2
	cota=n-k
	
	# Verificacion de invariante y cota al inicio
	assert(n>=k)
	assert(cota>=0)
	while (n>k):
		if ((n%k)==0):
			print(k)
			j+=1
			k+=1
			r="no es primo"
		else:
			k+=1
		# Verificacion de invariante y cota en cada iteracion
		assert(n>=k)
		assert(cota>n-k)
		cota=n-k
elif n==1:
	r="no es primo"
# Postcondicion: 
assert( r=="no es primo" or j==0  )

# Salida:
if j==1:
	print(r, "pues tiene",j,"factor no trivial")
elif n==1:
	print(r)
else:
	print(r, "pues tiene",j,"factores no triviales")