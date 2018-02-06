"""	Lab02ejercicio1.py
	DESCRIPCION: Programa que dado el numero de un año, \
	Dice si es bisiesto o no.
		
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 25/01/2018
	VARIABLES:
	anyo: int // ENTRADA: Numero del año.
	esBisiesto: bool // SALIDA: Si es bisiesto o no.
"""

# Valores iniciales:
anyo = int(input("Que año desea saber si es bisiesto? "))

# Precondicion: 
assert(anyo > 0)

# Calculos:
esBisiesto = True
if  ((anyo % 400) == 0):
	pass
elif ((anyo % 100) != 0) and ((anyo % 4) == 0 ):
	pass
elif ((anyo % 4) != 0) or ((anyo % 100) == 0) and ((anyo % 400) != 0 ):
	esBisiesto = False

# Postcondicion: 
assert( ((anyo % 4) == 0) and ((anyo % 100) != 0) or ((anyo % 400) == 0 ) == (esBisiesto == True))

# Salida:
print(esBisiesto)