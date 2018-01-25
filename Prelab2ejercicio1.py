"""	Prelab2ejercicio1.py

	DESCRIPCION: Programa que dado un valor entero a cualquiera, calcula su valor absoluto.
	El calculo consta en la aplicacion de la definicion de valor absoluto \
	Dicho resultado es almacenado en b.
	
	Autor: 
		Br. Jose Barrera

	Ultima modificacion: 18/01/2018

	VARIABLES:
	a: int // ENTRADA: Numero al que se le desea calcular el valor absoluto.
	b: int // SALIDA: Valor absoluto de a.
"""

# Valores iniciales:
a = int(input("Calculare el valor absoluto de "))

# Precondicion: 
assert(True)

# Calculos:
if a >= 0:
	b = a
else:
	b = - a

# Postcondicion: 
assert(b == abs(a))

# Salida:
print("El valor absoluto de",a, "es",b)