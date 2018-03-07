"""	Lab06ejercicio2.py
	DESCRIPCION: Programa que dada un arreglo A de N naturales \
	produce otro arreglo F con el numero de Fibonacci de cada uno \
	de los valores de A. Para ello utiliza 3 subprogramas, para leer \
	los número de la entrada y almacenarlos en un arreglo A, otro \
	para producir los números de Fibonacci en un segundo arreglo F \
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
# var A: array // variable auxiliar
# var i: int // variable auxiliar
    print("A continuacion introduzca los elementos de la secuencia")
    A=[int(input("A["+str(i)+"]=")) for i in range(N)]
    return A
# POSTCONDICION: True
#Fin leer
###############################################################################

# Descripcion: Funcion que toma 3 argumentos booleanos \
#				y retorna un entero distinto en cada caso.
# Parametros:
def mostrar(B: array) -> int:
# PRECONDICION: True
	if B[2]==True:
		o=0
	elif B[1]==True:
		o=-1
	elif B[0]==True:
		o=1
	return o
# POSTCONDICION: (B[2]=True /\ o=0) \/ (B[1]=True /\ o=-1) \/ (B[0]=True /\ o=1)
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

print(mostrar(fib(leer(N))))

# Aquí no se verifica la post. Ya se verifico en el subprograma.
# Es muy sencillo el codigo del programa principal seria redundante
# FIN DEL PROGRAMA PRINCIPAL