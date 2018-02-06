"""	Prelab2ejercicio2.py

	DESCRIPCION: Programa que calcula las raices de polinomios de la forma \
	AX**2 + BX + C tomando como entrada 3 numeros (A,B,C) enteros.
	Para calcularlas se utiliza la formula general o formula resolvente.
	Dichas raices son  almacenadas en las variables x1 y x2.
	
	Autor: 
		Br. Jose Barrera

	Ultima modificacion: 18/01/2018

	VARIABLES:
	A: int // ENTRADA: Coeficiente del cuadratico.
	B: int // ENTRADA: Coeficiente del lineal.
	C: int // ENTRADA: Termino independiente.
	x1: float // SALIDA: raiz del polinomio para el determinante positivo.
	x2: float // SALIDA: raiz del polinomio para el determinante negativo.

"""

# Valores iniciales:
A = int(input("Coeficiente cuadratico = "))
B = int(input("Coeficiente lineal = "))
C = int(input("Termino independiente = "))

# Precondicion: 
assert((A != 0) and (4 * A * C <= B * B))

# Calculos:
x1 = float((- B + ((B ** 2) - ((4 * A) * C)) ** 0.5) / (A * 2))
x2 = float((- B - ((B ** 2) - ((4 * A) * C)) ** 0.5) / (A * 2))
if x1 == x2:
	print(x1," es raiz doble, es decir")
else:
	pass
print("Las raices del polinomio son ",x1, "es",x2)

# Postcondicion: 
assert(((((A * x1) * x1) + (B * x1) + C) == 0) and ((((A * x2) * x2) + (B * x2) + C) == 0))

# Salida:
print("Las raices del polinomio son ",x1, "es",x2)