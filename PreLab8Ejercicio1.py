""" PreLab8Ejercicio1.py
	DESCRIPCION: Programa que lee un archivo de nombre “input.txt” con el formato\
  	(un número entero y un string por línea) para una cadena ADN factorizada. Y \
  	escribe en otro archivo de nombre “output.txt”, el resultado del ADN no-factorizado.
Autor: 
	Br. Jose Barrera
Ultima modificacion: 18/03/2018
"""

def ADN(l=list) -> bool:
	L=len(l)
	R=0
	for i in range(L):
		if  (l[i] == "A") or (l[i] == "T") or (l[i] == "G") or (l[i] == "C"):
			R+=1
	if R==L:
		return True
	return False

with open("input.txt") as f:
	for line in f:
		print(line, end="")
	print("\n")
	A=[line.split() for line in f]
f.closed

with open("output.txt", "r+") as f:
	for i in range(len(A)):
		if 0<int(A[i][0])<50 and ADN(A[i][1]):
			f.write(A[i][1]*int(A[i][0])+"\n")		
		else:
			f.write("Linea erronea\n")
	for line in f:
		print(line, end="")
f.closed