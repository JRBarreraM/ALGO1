"""	Lab04Ejercicio1.py
	DESCRIPCION: Programa dados los coeficientes de un polinomio\
	los almacena en un arreglo (hasta que se introduzca el valor cero).\
	El programa muestra el grado del polinomio y luego el polinomio\
	en notación polinomial. El grado del polinomio no puede ser mayor que M \
	un valor inicial dado por el usuario.
		
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 09/02/2018
	VARIABLES:
	M: int // ENTRADA: Valor superior al grado del polinomio P.
	P: array // Almacena los coeficientes del polinomio.
	i: int // Valor que permite recorrer los valores entre 0 y M.
"""

# Valores iniciales:
M=int(input("El grado del polinomio es <= que: "))

# Precondicion: 
assert(M>0)

P=[int(input("P[" + str(i) + "]= ")) for i in range(M+1)]
print("P(x)= ",end=(""))

# Cota M-i
# Invariante
# assert(True)
for i in range(M+1):
	# operaciones del lazo
	if 0==P[i]:
		pass
	elif i<M and (0<P[i] or 0>P[i]):
			print(P[i],"x^",M-i,"+",end=(""))
	elif i==M:
		print(P[i])
	# Invariante
	# assert(​True)

# Postcondicion: 
assert(True)