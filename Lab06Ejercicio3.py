"""	Lab06Ejercicio3.py
	DESCRIPCION: Programa que dados dos numero naturales N y M, \
	produce una lista S de los factores primos de M que son <= N, \
	indicando por cada uno su exponente en la factorización de M. \
	Para ello utiliza subprogramas, el primero para leer \
	los número de la entrada y almacenarlos en un arreglo S, otro \
	para verfificar si un numero es primo, un tercero para anexar a S \
	los factores primos de M con sus exponentes, y por ultimo uno que \
	imprima la informacion de manera organizada en pantalla.
	
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 09/03/2018
"""

import sys    # Se importa la libreria sys para poder utilizar sys.exit()
import array

# SUBPROGRAMAS

# Descripcion: Funcion que lee una secuencia de A enteros y \
#				la almacena en un arreglo S .
# Parametros:
def leer(M: int, N: int) -> (array):
# PRECONDICION: True
# var S: array // variable auxiliar
# var i: int // variable auxiliar
    S=[0]*(M+2)
    S[0]=M
    S[1]=N
    return S
# POSTCONDICION: True
#Fin leer
###############################################################################

# Descripcion: Funcion que verifica si un numero es primo \
#				y retorna un booleano .
# Parametros:
def primo(i: int) -> bool:
# PRECONDICION: i>0
# var j: int // variable auxiliar
	for j in range(2,i):
		if i%j==0:
			return False
	return True
# POSTCONDICION: True
#Fin leer
###############################################################################

# Descripcion: Funcion que toma un arreglo y calcula los factores primos \
#				del primer elemento de un arreglo S.
# Parametros:
def aprimo(S: array) -> (array):
# PRECONDICION: True
# var S: array // variable auxiliar
# var i: int // base factor primo
# var E: int // exponente factor primo
# var a: int // variable auxiliar
# var b: int // variable auxiliar
	a,b=2,3
	for i in range(2,S[0]):
		if primo(i):
			E=0
			M=S[0]
			while M%i==0:
				M=M//i
				E+=1
			if E!=0:
				S[a]=i
				S[b]=E
				a+=2
				b+=2
	return S
# POSTCONDICION: True
#Fin leer
###############################################################################

# Descripcion: Funcion que toma un arreglo S e imprime la informacion que este \
#				contiene para que sea legible por el usuario.
# Parametros:
def mostrar(S: array) -> array:
# PRECONDICION: True
# var i: int // recorre el arreglo
# var N: int // tamaño del arreglo
	if S[2]==0:
		print("El numero es primo, sus factores son triviales:",1,"y",S[0])
	else: 
		for i in range(1,(M+2)//2):
			if 0<S[2*i]<S[1]:
				print(S[2*i],"a la",S[2*i+1])
	return S
# POSTCONDICION: True
#Fin mostrar

##################################
# Inicio del programa 
##################################
print("Ingrese dos numeros naturales y se calcularan los factores primos")
print("de uno que sean menores que el otro (con su descomposicion detallada)")
# Valores iniciales:
M=int(input("Ingrese el natural al cual se le calcularan sus factores primos:"))
N=int(input("Ingrese el natural mayor que los factores primos del otro:"))

try:
    assert(M>1 and N>2 and M>=N)
except:
    print("El numero a factorizar debe ser mayor a 1")
    print("La cota debe ser mayor que 2")
    print("El numero a factorizar debe ser mayor o igual que la cota")    
    print("el programa terminara")
    sys.exit()
print("Los Naturales que cumplen la condicion son:")

mostrar(aprimo(leer(M,N)))

# Aquí no se verifica la post. Ya se verifico en el subprograma.
# Es muy sencillo el codigo del programa principal seria redundante
# FIN DEL PROGRAMA PRINCIPAL