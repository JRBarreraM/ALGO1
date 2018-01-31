"""	Lab03ejercicio3.py
	DESCRIPCION:Dado un entero positivo n dice si es perfecto.\
	Un número perfecto es un entero que es igual a la suma \
	de los divisores propios menores que él mismo. \
	Esto incluye al 1 pero no incluye a n. Además, \
	el programa imprime los divisores de n (distintos de 1 y n)\
	a medida que consigue un divisor. Finalmente, se imprime si n es primo o no.
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 30/01/2018
	VARIABLES:
	n: int // ENTRADA: Almacena el valor de entrada.
	r: str // SALIDA: Dice si n es primo o no.
	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine.
	k: int // Valor que permite recorrer los enteros entre 2 y n-1.
	j: int // Valor que permite contar el numero de factores.
"""
# Valores iniciales:
n=int(input("Introduzca el numero: "))

# Precondicion: 
assert(n>0)

# Inicializaciones del ciclo
k,j=1,0
cota=n-k

# Verificacion de invariante y cota al inicio
assert(n>=k)
assert(cota>=0)
while (n>k):
	if ((n%k)==0):
		print(k)
		j+=k
		k+=1
	else:
		k+=1
	# Verificacion de invariante y cota en cada iteracion
	assert(n>=k)
	assert(cota>n-k)
	cota=n-k
perfecto=(n==j)
# Postcondicion: 
assert( (n==k or perfecto==False) and (n!=k or perfecto==True) )

# Salida:
if perfecto==False:
	print(n,"no es perfecto")
else:
	print(n,"es perfecto")