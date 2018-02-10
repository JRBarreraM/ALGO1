"""	PreLab5ejercicio1.py

	DESCRIPCION: Programa que calcula las raices de polinomios de la forma \
	AX**2 + BX + C tomando como entrada 3 numeros (A,B,C) enteros.
	Para calcularlas se utiliza la formula general o formula resolvente.
	Dichas raices son  almacenadas en las variables x1 y x2.
	Con una precondicion robusta.
	
	Autor: 
		Br. Jose Barrera

	Ultima modificacion: 10/02/2018

	VARIABLES:
	A: int // ENTRADA: Coeficiente del cuadratico.
	B: int // ENTRADA: Coeficiente del lineal.
	C: int // ENTRADA: Termino independiente.
	x1: float // SALIDA: raiz del polinomio para el determinante positivo.
	x2: float // SALIDA: raiz del polinomio para el determinante negativo.

"""
import sys    # Se importa la libreria sys para poder utilizar sys.exit()
"""import math Se importa la libreria math para poder utilizar math.ceil()
una solucion opcinal para el problema de las raices irracionales
Postcondicion
assert(((math.ceil(((A * x1) * x1) + (B * x1) + C) == 0) or ((math.ceil(((A * x1) * x1) + (B * x1) + C) == 1))) \
	and ((math.ceil(((A * x2) * x2) + (B * x2) + C) == 0) or ((math.ceil(((A * x2) * x2) + (B * x2) + C) == 1))"""

# Verificacion de la Precondicion (version robusta)

while True: # Se permite al usuario introducir nuevos datos correctos
	try: 
		A=int(input("Coeficiente cuadratico = "))
		B=int(input("Coeficiente lineal = "))
		C=int(input("Termino independiente = "))
		assert((A != 0) and (4 * A * C <= B * B))
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("Los valores deben ser enteros y el coeficiente cuadratico distinto de 0")
		print("Nota, este programa no soporta raices imaginarias")

# Calculos:
x1 = float((- B + ((B ** 2) - ((4 * A) * C)) ** 0.5) / (A * 2))
x2 = float((- B - ((B ** 2) - ((4 * A) * C)) ** 0.5) / (A * 2))
if x1 == x2:
	print(x1," es raiz doble, es decir")
else:
	pass

# Postcondicion: 
try:
	assert(((((A * x1) * x1) + (B * x1) + C) == 0) and ((((A * x2) * x2) + (B * x2) + C) == 0))
except:
	print("No se cumple la postcondicion con los valores ")
	print("Cabe la posibilidad de que sean raices irracionales")
	sys.exit() # Se aborta el programa, pues no cumple la postcondicion

# Salida:
print("Las raices del polinomio son ",x1,"y",x2)