"""	Prelab2ejercicio3.py

	DESCRIPCION: Programa que dados tres valores enteros A, B y C \
	con valores diferentes, determinar el valor máximo ëntre ellos.
			
	Autor: 
		Br. Jose Barrera

	Ultima modificacion: 23/01/2018

	VARIABLES:
	A: int // ENTRADA: 1er Numero a comparar.
	B: int // ENTRADA: 2do Numero a comparar.
	C: int // ENTRADA: 3er Numero a comparar.
	maximo: int // SALIDA: Numero maximo. 
"""

# Valores iniciales:
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

# Precondicion: 
assert(A != B != C)

# Calculos:
if A > B and A > C:
	maximo = A
elif B > A and B > C:
	maximo = B
elif C > A and C > B:
	maximo = C

# Postcondicion: 
assert( ((A > B and A > C) == (maximo == A) ) or ((B > A and B > C) == (maximo == B) ) \
	or ((C > A and C > B) == (maximo == C) ) )

# Salida:
print(maximo)