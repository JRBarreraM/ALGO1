"""	Lab06ejercicio2.py
	DESCRIPCION: Programa que dada un arreglo A de N naturales \
	produce otro arreglo F con el numero de Fibonacci de cada uno \
	de los valores de A. Para ello utiliza 4 subprogramas, para leer \
	los número de la entrada y almacenarlos en un arreglo A, otros dos \
	para producir los números de Fibonacci y colocarlos en un segundo arreglo F \
	y otro que tome el arreglo F y lo imprima en pantalla.
	
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 07/03/2018
"""

import sys    # Se importa la libreria sys para poder utilizar sys.exit()
import array

# SUBPROGRAMAS

# Descripcion: Funcion que lee una secuencia de A enteros y \
#				la almacena en un arreglo S .
# Parametros:
def leer(N: int) -> (array):
# PRECONDICION: N>0
# var S: array // variable auxiliar
# var i: int // variable auxiliar
    print("A continuacion introduzca los elementos de la secuencia")
    S=[int(input("S["+str(i)+"]=")) for i in range(N)]
    return S
# POSTCONDICION: True
#Fin leer
###############################################################################

# Descripcion:  Funcion que toma un arreglo S de enteros y \
#				devuelve un arreglo F, donde cada elemento \
#				de F es el Fibonacci del elemento de A correspondiente.
# Parametros:
def fib(S: int) -> int:
# PRECONDICION: S>=0
# var f: int  // variable auxiliar
# var k: int // variable auxiliar
# var a: int  // variable auxiliar
# var b: int  // variable auxiliar

	k,f,a,b=0,1,1,1
	while k<=S:
		if k==0:
			k+=1
		elif k==1:
			k+=1
		elif k!=0 and k!=1:
			f=a+b
			a=b
			b=f
			k+=1
	return f
# POSTCONDICION: fib(S)=((fib(S-2)+fib(S-1) /\ S>1) \/ (fib(S)=1 /\ (S=0 \/ S=1)))
#Fin fiba
###############################################################################

# Descripcion:  Funcion que toma un arreglo S de enteros y \
#				devuelve un arreglo F, donde cada elemento \
#				de F es el Fibonacci del elemento de A correspondiente.
# Parametros:
def fiba(S: array) -> (array):
# PRECONDICION: len(S)>0
# var S: array // variable auxiliar
# var i: int // variable auxiliar
# var N: int // variable auxiliar
	N=len(S)
	i=0
	while i<N:
		S[i]=fib(S[i])
		i+=1
	F=S
	return F
# POSTCONDICION: True
#Fin fiba
###############################################################################

# Descripcion: Funcion que muestra en pantalla un arreglo.
# Parametros:
def mostrar(F: array) -> array:
# PRECONDICION: True
	print(F)
	return F
# POSTCONDICION: True
#Fin mostrar

##################################
# Inicio del programa 
##################################
print("Ingrese un arreglo de naturales,")
print("se devuelve un arreglo con el Fibonacci de cada elemento")
# Valores iniciales:
N=int(input("Coloque la cantidad de elementos de la secuencia:"))

try:
    assert(N>0)
except:
    print("El tamaño de la secuencia debe ser mayor a 0")    
    print("el programa terminara")
    sys.exit()

mostrar(fiba(leer(N)))

# Aquí no se verifica la post. Ya se verifico en el subprograma.
# Es muy sencillo el codigo del programa principal seria redundante
# FIN DEL PROGRAMA PRINCIPAL