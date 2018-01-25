"""	Lab2ejercicio6.py

	DESCRIPCION: Programa que dados dos numeros enteros m y n, \
	devuelva m/n si m=10, m*n si m=5, m+n si m=3, m**n si m=2 y en cualquier otro devuelva m.
			
	Autor: 
		Br. Jose Barrera

	Ultima modificacion: 25/01/2018

	VARIABLES:
	m: int // ENTRADA: 1er Numero.
	n: int // ENTRADA: 2do Numero.
	o: var // SALIDA: Resultado de la operacion correspondiente a cada caso.

"""

# Valores iniciales:
m = int(input("ingrese el primer numero = "))
n = int(input("ingrese el segundo numero = "))

# Precondicion: 
assert(True)

# Calculos:
if m == 10:
	o = m/n
elif m == 5:
	o = m*n 
elif m == 3:
	o = m+n
elif m == 2:
	o = m**n
else:
	o = m

# Postcondicion: 
assert(((m != 10) or (o == m/n)) and ((m != 5) or (m*n == o)) \
	or ((m != 3) or (m+n == o)) and ((m == 2) != (m**n == o)) and \
	((m == 2 ==  3 == 5 == 10) or (m == o)))

# Salida:
print("El resultado es", o)