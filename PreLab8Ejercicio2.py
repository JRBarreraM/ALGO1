""" PreLab8Ejercicio2.py
	DESCRIPCION: Programa, que calcula la sumatoria desde 0 hasta \
	un N dado por el usuario, de 2 a la N. 

	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 18/03/2018
		VARIABLES:
	exp: int // ENTRADA N-esimo termino de la sumatoria.
	sumatoria: int // SALIDA Valor de  la sumatoria desde 0 hasta N de 2^N.	
"""

# Descripcion: Funcion calcula el valor de la potencia ingresada.
# Parametros:
def potencia(base=int,exp=int)-> int:
# PRECONDICION: exp>=0 /\ base >=0
	if exp==0 : 					#Caso Base exponente igual a 0
		return 1
	else:
		exp-=1
		return base*potencia(base,exp)
# POSTCONDICION: potencia(base,exp)=base^exp

# Descripcion: Funcion suma de 0 hasta un N, 2 a la N.
# Parametros:
def suma(base=int,exp=int)-> int:
# PRECONDICION: exp>=0 /\ base >=0
	if exp==0 : 					#Caso Base exponente igual a 0
		return 1
	else:
		P=potencia(base,exp)
		exp-=1
		return P+suma(base,exp)
# POSTCONDICION: (%sum i : 0<=i<=exp : base^i ) = suma(base,exp)

##################################
# Inicio del programa 
##################################

exp=int(input("Ingrese el n-esimo termino de la sumatoria:"))
sumatoria=suma(2,exp)

#Salida:
print("La sumatoria de 0 hasta",exp,"de 2 a la",exp,"es igual a",sumatoria)