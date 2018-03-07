"""	Lab06ejercicio1.py
	DESCRIPCION: Programa que dada una secuencia S de N enteros \
	verifica si esta esta ordenada (creciente o decrecientemente) \
	o desordenada. Se devuelve como resultado un valor entero \
	(-1: decreciente; 1:creciente y 0:en desorden). Para ello utiliza 3 \
	subprogramas, para leer la secuencia, determinar el tipo de orden e imprimir.
	
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 07/03/2018
"""
import sys    # Se importa la libreria sys para poder utilizar sys.exit()
import array

# SUBPROGRAMAS


# Descripcion: Funcion que lee una secuencia de N enteros y \
#				la almacena en un arreglo S .
# Parametros:
def leer(N: int) -> (array):
# PRECONDICION: N>1
# var S: array // variable auxiliar
# var i: int // variable auxiliar
    print("A continuacion introduzca los elementos de la secuencia")
    S=[int(input("S["+str(i)+"]=")) for i in range(N)]
    return S
# POSTCONDICION: True
#Fin leer
###############################################################################

# Descripcion: Funcion que compara los elementos de un arreglo S \
#				y dice si esta ordenada (creciente o decreciente) o desordenada.
# Parametros:
def orden(S: array) -> (bool,bool,bool):
# PRECONDICION: len(S)>1

# var i: int // conteo de iteraciones el ciclo
# var creciente: bool // variable auxiliar
# var decreciente: bool // variable auxiliar
# var desordenado: bool // variable auxiliar
    i=0
    L=len(S)
    creciente=False
    decreciente=False
    desordenado=False
    while i<L-1 and desordenado==False:
        if S[i]<=S[i+1]:
            creciente=True
            if decreciente==True and creciente==True:
            	desordenado=True
        elif S[i]>S[i+1]:
            decreciente=True
            if decreciente==True and creciente==True:
            	desordenado=True
        i=i+1
        print(creciente, decreciente, desordenado)
    return (creciente,decreciente,desordenado)
# POSTCONDICION: (% forall i: int | 0 <= i /\ i < N-1 | S[i]>S[i+1] \/ creciente=True) \/
#				(% forall i: int | 0 <= i /\ i < N-1 | S[i]<=S[i+1] \/ decreciente=True) \/
#						((desordenado!=creciente) \/ (desordenado=True))
#Fin orden
###############################################################################

# Descripcion: Funcion que toma un arreglo con 3 argumentos booleanos \
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
###############################################################################

##################################
# Inicio del programa 
##################################
print("Ingrese una secuencia, se le dira si esta es creciente,decreciente o desordenada")
print("a traves de un numero entero:(-1: decreciente; 1:creciente y 0:en desorden)") 
# Valores iniciales:
N=int(input("Coloque la cantidad de elementos de la secuencia:"))

try:
    assert(N>1)
except:
    print("El tamaño de la secuencia debe ser mayor a 1")    
    print("el programa terminara")
    sys.exit()

print(mostrar(orden(leer(N))))

# Aquí no se verifica la post. Ya se verifico en el subprograma.
# Es muy sencillo el codigo del programa principal seria redundante
# FIN DEL PROGRAMA PRINCIPAL