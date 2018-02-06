"""	Lab02ejercicio4.py

	DESCRIPCION: Programa que dados tres valores enteros A, B y C \
	con valores diferentes, determina el valor maximo entre ellos.
			
	Autor: 
		Br. Jose Barrera

	Ultima modificacion: 25/01/2018

	VARIABLES:
	A: int // ENTRADA: 1er Numero a comparar.
	B: int // ENTRADA: 2do Numero a comparar.
	C: int // ENTRADA: 3er Numero a comparar.
	maximo: int // SALIDA: Numero maximo. 
"""

# Valores iniciales:
A = int(input("ingrese el primer numero = "))
B = int(input("ingrese el segundo numero = "))
C = int(input("ingrese el tercer numero = "))

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
assert( ( not (A > B and A > C) or (maximo == A) ) and ( not (B > A and B > C) or (maximo == B) ) \
	and ( not(C > A and C > B) or (maximo == C) ) )

# Salida:
print("El maximo es ", maximo)