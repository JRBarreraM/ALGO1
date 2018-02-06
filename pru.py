N=int(input("Ingrese el valor de N: "))

# Precondicion: 
assert(N >= 0)

# Inicializaciones del ciclo
suma, fact, k = 0, 1, 0
cota = N + 1 -k

# Definicion de prod
def prod( iterable ):
	p = 1
	for n in iterable:
		p *= n
	return p
print((fact == prod (j for j in range(1,k+1) ) ) )
print(sum (i for i in (0,k)))

#(prod (j for j in range(1,i+1)))