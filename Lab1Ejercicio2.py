#
# Lab1Ejercicio2.py
#
# DESCRIPCION: Programa que dados tres valores enteros a,b,c
# que cumplen a>=b>=c, intercambie los valores de manera que cumplan a<=b<=c
# Dicho resultado es almacenado en Resultado.
#
# Autor: 
#	Br. Jose Barrera
#
# Ultima modificacion: 16/01/2018
#

# VARIABLES:
#	a: int   // ENTRADA: Valor mayor.
#	b: int // ENTRADA: Valor medio.
#   c: int // ENTRADA: Valor menor.


# Valores iniciales:
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

# Precondicion: 
assert(a >= b >= c)

# Calculos:
(a,c) = (c,a)

# Postcondicion: 
assert(c >= b >= a)

# Salida:
print("El nuevo orden es ", a, b, c)