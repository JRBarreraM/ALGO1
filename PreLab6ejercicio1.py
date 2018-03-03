"""	PreLab6ejercicio1.py
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

# Descripcion: Funcion que computa las raices de un polinomio cuadratico.
# Parametros: 
#           A: radio de la circunferencia 
#           B: Valor de la constante PI
#			C: 
def raices(A: int, B: int, C: int) -> (float, float):
# PRECONDICION: (A != 0) and (4 * A * C <= B * B))

# var x1: float // variable auxiliar
# var x2: float // variable auxiliar

	x1 = float((- B + ((B ** 2) - ((4 * A) * C)) ** 0.5) / (A * 2))
	x2 = float((- B - ((B ** 2) - ((4 * A) * C)) ** 0.5) / (A * 2))
	return x1,x2
# POSTCONDICION: ((((A * x1) * x1) + (B * x1) + C) == 0) and \
#					((((A * x2) * x2) + (B * x2) + C) == 0)
##################################
# Inicio del programa 
##################################
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
l=(raices(A,B,C))
x1=l[0]
x2=l[1]

# Postcondicion: 
try:
	assert(((((A * x1) * x1) + (B * x1) + C) == 0) and ((((A * x2) * x2) + (B * x2) + C) == 0))
except:
	print("No se cumple la postcondicion con los valores ")
	print("Cabe la posibilidad de que sean raices irracionales")
	sys.exit() # Se aborta el programa, pues no cumple la postcondicion

# Salida:
print("Las raices del polinomio son ",x1,"y",x2)