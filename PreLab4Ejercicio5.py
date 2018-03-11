"""	Lab04Ejercicio3.py
	DESCRIPCION:  Construye una clase estudiante que almacena,\
	la edad, el nombre, índice académico de un estudiante \
	y las notas de los cuatro parciales de 25 puntos de CI2611.\
	El programa lee los datos de un grupo de N estudiantes,\
	con N leido de la entrada. Estos datos son guardados en\
	un arreglo de estudiantes, llamado ​ grupo​ . Finalmente,\
	calcule el promedio de la edad del grupo, el promedio del índice,\
	la nota total de cada estudiante y el promedio para cada parcial.
	
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 02/01/2018
	VARIABLES:
	N: int // ENTRADA: Almacena el entero de entrada.
	estudiante: class // Agrupa los atributos de los estudiantes.
	grupo: array // Almacena la informacion de todos los estudiantes.
	nombre: str // ENTRADA: Atributo nombre del estudiante.
	edad: int // ENTRADA: Atributo edad del estudiante.
	indice: int // ENTRADA: Atributo indice del estudiante.

	x: int // Permite operar entre 0 y N, para anexar al grupo\
				a los estudiantes.
	i: int // Permite operar entre 0 y N, para escribir los\
				atributos de los estudiantes del grupo.
"""
# Valores iniciales:
N=int(input("Introduzca el numero de estudiantes: "))
class estudiante:
	nombre="Jose"
	edad=19
	indice=4.0
	ntp1=12.5
	ntp2=22.5
	nt3=25.0
	nt4=25.0

grupo=[estudiante() for x in range(N)]
i=0
#Cota=N-1-i
#Invariante
assert((len(grupo[i].nombre)>=1) and (grupo[i].edad>0) and (0<grupo[i].indice<6) \
	 and 0<=grupo[i].ntp1<=25 and 0<=grupo[i].ntp2<=25 and 0<=grupo[i].ntp3<=25 and 0<=grupo[i].ntp4<=25)6))

#Operaciones del lazo
for i in range(N):
	grupo[i].nombre=str(input("Introduzca el nombre del estudiante:"))
	grupo[i].edad=int(input("Introduzca la edad del estudiante:"))
	grupo[i].indice=float(input("Introduzca el indice del estudiante:"))
	grupo[i].ntp0=float(input("Introduzca la nota del primer parcial del estudiante:"))
	grupo[i].ntp1=float(input("Introduzca la nota del segundo parcial del estudiante:"))
	grupo[i].ntp2=float(input("Introduzca la nota del tercer parcial del estudiante:"))
	grupo[i].ntp3=float(input("Introduzca la nota del cuarto parcial del estudiante:"))

	#Invariante
	assert((len(grupo[i].nombre)>=1) and (grupo[i].edad>0) and (0<grupo[i].indice<6) \
		 and 0<=grupo[i].ntp1<=25 and 0<=grupo[i].ntp2<=25 and 0<=grupo[i].ntp3<=25 and 0<=grupo[i].ntp4<=25)

#Calculo Promedio Edad
p=0
for i in range(N):
	p+=grupo[i].edad
ep=(p/N)

#Calculo Promedio Indice
p=0
for i in range(N):
	p+=grupo[i].indice
ip=(p/N)

#Calculo Promedio Parcial1
p=0
for i in range(N):
	p+=grupo[i].ntp0
p0p=(p/N)

#Calculo Promedio Parcial2
p=0
for i in range(N):
	p+=grupo[i].ntp1
p1p=(p/N)

#Calculo Promedio Parcial3
p=0
for i in range(N):
	p+=grupo[i].ntp2
p2p=(p/N)

#Calculo Promedio Parcial4
p=0
for i in range(N):
	p+=grupo[i].ntp3
p3p=(p/N)

#Calculo definitiva
definitiva=0
for i in range(N):
	for j in range(4):
		definitiva+=grupo[i].ntp[j]
	if definitiva>=85:
		print("nota definitiva ",definitiva) 

# Postcondicion:
assert((ep>0) and (0<ip<6) and 0<=definitiva<6 (p1p>=0) and (p2p>=0) and (p3p>=0) and (p0p>=0))

# Salida:
print("Los promedios de edad e indice del grupo son:",ep,"y",ip)
print("Mientras que os promedios de cada parcial son:",p1p,p2p,p3p,p4p)