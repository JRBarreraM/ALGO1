"""	Prelab4ejercicio2.py
	DESCRIPCION:  Construye una clase estudiante que almacena,\
	la edad, el nombre e índice académico de un estudiante.\
	El programa lee los datos de un grupo de N estudiantes,\
	con N leido de la entrada. Estos datos son guardados en\
	un arreglo de estudiantes, llamado ​ grupo​ . Finalmente,\
	calcule el promedio de la edad del grupo y el promedio del índice.
	
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
				atrubutos de los estudiantes del grupo.
"""
# Valores iniciales:
N=int(input("Introduzca el numero de estudiantes: "))
class estudiante:
	nombre="0"
	edad=1
	indice=1.0

grupo=[estudiante() for x in range(N)]
i=0
#Cota=N-1-i
#Invariante
assert((len(grupo[i].nombre)>0) and (grupo[i].edad>0) and (0<grupo[i].indice<6))

#Operaciones del lazo
for i in range(N):
	grupo[i].nombre=str(input("Introduzca el nombre del estudiante:"))
	grupo[i].edad=int(input("Introduzca la edad del estudiante:"))
	grupo[i].indice=float(input("Introduzca el indice del estudiante:"))
	#Invariante
	assert((len(grupo[i].nombre)>=1) and (grupo[i].edad>0) and (0<grupo[i].indice<6))

#Calculo Promedio Edad
a=0
for i in range(N):
	a+=grupo[i].edad
ep=(a/N)

#Calculo Promedio Indice
b=0
for i in range(N):
	b+=grupo[i].indice
ip=(b/N)

# Postcondicion:
assert((ep>0) and (0<ip<6))

# Salida:
print("Los promedios de edad e indice del grupo son:",ep,"y",ip)
