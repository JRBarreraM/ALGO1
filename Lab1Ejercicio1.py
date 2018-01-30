#
# Lab1Ejercicio1.py
#
# DESCRIPCION: Programa que calcula el área de un circunferencia,
# si se le proporciona el valor del radio, a traves de la formula,
# Area = Radio*Radio*3,1416 
# Dicho resultado es almacenado en Area.
#
# Autor: 
#	Br. Jose Barrera
#
# Ultima modificacion: 16/01/2018
#

# VARIABLES:
#	R: float  // ENTRADA: Valor del Radio.
#	A: float // SALIDA: Resultado de la formula

# Valores iniciales:
R = float(input("Radio:"))

# Precondicion: 
assert(R >= 0)

# Calculos:
A = (R*R)*3.1416	

# Postcondicion: 
assert(A == (R*R)*3.1416)

# Salida:
print("El Area es",A)