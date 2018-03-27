""" PreLab8Ejercicio1.py
	DESCRIPCION: Programa que permite dos opciones, leer un archivo y guardar en un archivo.

	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 26/03/2018
		VARIABLES:
	N: int    //ENTRADA: 1 si desea cargar y 2 para guardar
	e: str    //Estructura del juego a ser guardada
	estructura: str   //Estructura del juego a ser cargada	
"""
#Clase que nos almacenar los valores de juego

class valoresdejuego:
	nombre="Jose"					#nombre del jugador
	turno=100						#turno de la partida en curso
	nivel=2							#deficultad de la IA
	A=[[0]*7 for i in range(6)]		#tablero de juego
	i=5								#fila de la ultima jugada de la IA
	j=3								#columna de la ultima jugada de la IA
anterior=valoresdejuego()			#estructura donde guardamos los datos de la partida

#Definicion de subprogramas

# Descripcion: Funcion que cada turno actualiza los valores de las variables de juego. 
# Parametros:
def actualizacion(estructura=valoresdejuego,nombre=str,turno=int,nivel=int,A=list,i=int,j=int)->valoresdejuego:
		anterior.nombre=nombre
		anterior.turno=turno
		anterior.nivel=nivel
		anterior.A=A
		anterior.i=i
		anterior.j=j

# Descripcion: Funcion que lee el archivo de guardado y almacena su informacion
#			en una lista para posteriormente sobreescribir las variables de juego. 
# Parametros:
def CargarJuego(archivo=str)->list:
	with open(archivo,'r+') as f:
		oldcontenido = f.readlines()
		contenido = [oldcontenido[i].rstrip() for i in range(6)]
	f.closed
	return contenido
# Descripcion: Funcion que escibe en el archivo de guardado los valores actuales
#			de las variables de juego(nombre,turno,nivel,A,i,j). 
# Parametros:
def GuardarJuego(archivo=str, estructura=valoresdejuego):#no tiene salida
	with open(archivo,'w') as f:
		f.write(anterior.nombre+"\n")
		f.write(str(anterior.turno)+"\n")
		f.write(str(anterior.nivel)+"\n")
		f.write(str(anterior.A)+"\n")
		f.write(str(anterior.i)+"\n")
		f.write(str(anterior.j))
	f.closed

# Valores iniciales:

nombre,turno,nivel,A,i,j="Jose",23,2,[[0]*7 for i in range(6)],3,5 #variables de prueba

#print(nombre,turno,nivel,A,i,j) #mostrar variables de juego para ejemplificar

#Precondicion
while True: # Se permite al usuario introducir nuevos datos correctos
	try: 
		N = int(input("1 = Cargar Juego      2 = Guardar Juego"))
		assert(N == 1 or N == 2)
		break
	except:
		print("Opciones Validas 1 o 2")

#calculos

if N == 1:	#sobreescribimos las varibles de juego con las de la partida guardada
	contenido=CargarJuego("guardado.txt")
	nombre = contenido[0]		#nombre del jugador
	turno = int(contenido[1])	#turno de la partida en curso
	nivel = int(contenido[2])	#deficultad de la IA
	A = (contenido[3])			#tablero de juego
	i = int(contenido[4])		#fila de la ultima jugada de la IA
	j = int(contenido[5])		#columna de la ultima jugada de la IA

elif N == 2:	#escribimos en alrchivo de guardado las variales de juego actuales
	GuardarJuego("guardado.txt",anterior)
"""
print(nombre,turno,nivel,A,i,j) #mostrar el cambio tras cargar las variables

with open("guardado.txt") as f:
	for line in f:
		print(line, end="")		#se muestra el contenido del archivo de guardado
	print("\n")
f.closed
"""