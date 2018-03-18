""" PreLab8Ejercicio1.py
	DESCRIPCION: Programa que lee un archivo de nombre “input.txt” con el formato\
  	(un número entero y un string por línea) para una cadena ADN factorizada. Y \
  	escribe en otro archivo de nombre “output.txt”, el resultado del ADN no-factorizado.
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 18/03/2018
		VARIABLES:
	A: int // Lista de tuplas donde el primer elemento es el factor del segundo.
"""

# Descripcion: Funcion verifica si todos los elementos de un str son bases del ADN.
# Parametros:
def ADN(l=str) -> bool:
# PRECONDICION: True
# var L: int // tamaño del str de entrada
# var R: int // contador de bases del ADN en los elementos del str
	L=len(l)
	R=0
	for i in range(L):
		if  (l[i] == "A") or (l[i] == "T") or (l[i] == "G") or (l[i] == "C"):
			R+=1
	if R==L:
		return True
	return False
# POSTCONDICION: (%forall i : 0<=i<L : (l[i] == "A") or (l[i] == "T") or (l[i] == "G") or (l[i] == "C"))=>True

##################################
# Inicio del programa 
##################################

# Valores iniciales:
with open("input.txt") as f:
	for line in f:
		print(line, end="")							#se muestra el contenido del archuvo input.txt al usuario
	print("\n")
f.closed

with open("input.txt") as f:
		A=[line.split() for line in f]				#se separan los factores de las Bases
f.closed

with open("output.txt", "r+") as f:
	for i in range(len(A)):
		if 0<int(A[i][0])<50 and ADN(A[i][1]):
			f.write(A[i][1]*int(A[i][0])+"\n")		#se  desfactoriza el ADN si se cumplan las condiciones		
		else:
			f.write("Linea erronea\n")				#si  no se cumplen las condiciones se escribe "Linea erronea"
f.closed

with open("output.txt", "r+") as f:
	for line in f:
		print(line, end="")							#se muestra el contenido del archuvo output.txt al usuario
f.closed