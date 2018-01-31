"""	Lab03ejercicio1.py
	DESCRIPCION: Programa que presenta un menú de tres opciones \
	1: Superficie de una habitación; 2: Área de una circunferencia; \
	3: Suma de cuadrados. Si el usuario selecciona la opción 1, \
	se solicita el largo y ancho de una habitación y muestra \ 
	la superficie de ésta con cuatro dígitos decimales. Si el usuario \
	selecciona la opción 2, se solicita el radio de la circunferencia, \
	y muestra el área de la misma. Usando 3.1416 como valor de π. \
	Si el usuario selecciona la opción 3, se solicita un número natural n, \
	y produce como resultado el valor de la suma​ (​ Σ ​ i ​ : 1​ ≤​ i ​ ≤​ n :​ i^2​ ​ ).
	
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 28/01/2018.
	VARIABLES:
	o: str // ENTRADA: Almacena la decision s/n.
	i: int // Valor que permite contar las veces en que se muestran las opciones.
	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine.
	p: int // ENTRADA: Almacena la decision 1/2/3.
	l: float // ENTRADA: Almacena el largo de la habitacion.
	a: float // ENTRADA: Almacena el ancho de la habitacion.
	s: float // SALIDA: Almacena el valor de la superficie.
	r: float // ENTRADA: Almacena el valor del radio.
	ar: float // SALIDA: Almacena el valor del area.
	n: int // ENTRADA: Almacena el valor del numero natural.
	su: int // SALIDA: Almacena el valor de la suma.
"""

# Valores iniciales:
print( "A continuacion se le presentan 3 opciones por favor escoja alguna de ellas" )
print( "Solo tendra 3 oportunidades" )
o=str( input ( "Esta usted de acuerdo? s/n   ") )

# Precondicion: 
assert( o=="n" or o =="s" )

if o=="n":
	pass
elif o=="s":

	# Inicializaciones del ciclo
	i=0
	cota = 2-i
	s,l,a,ar,su,r=False,False,False,False,False,False
	# Verificacion de invariante y cota al inicio
	assert( 0<=i<=2  )
	assert( cota >= 0 )
	
	while ( 0<=i<=2 ):
		print( "1: Superficie de una habitación " )
		print( "2: Área de una circunferencia " )
		print( "3: Suma de cuadrados " )
		p=int( input ( "Cual elige? 1/2/3   ") )
		
		if (p == 1):
			l=float( input ( "Ingrese el largo de la habitación   ") )
			a=float( input ( "Ingrese el ancho   ") )
			assert((l > 0) and (a > 0))
			s=l*a
			assert(s==l*a)
			s=round(s,4)
			print("La superficie es   ",s)
			i+=1
		elif (p == 2):
			r=float( input ( "Ingrese el radio   ") )
			assert(r>0)
			ar=(3.1416*(r**2))
			assert(ar==(3.1416*(r**2)))
			ar=round(ar,4)
			print("El area es   ",ar)
			i= i+1
		elif (p == 3):
			n=int( input ( "Ingrese el numero natural   ") )
			assert(n>0)
			su=sum(j**2 for j in (1,n))
			assert(su==sum(j**2 for j in (1,n)))
			print("La suma de los terminos al cuadrado desde 1 hasta",n,"es",su)
			i = i+1
		# Verificacion de invariante y cota en cada iteracion
		assert( 0<=i<=3 )
		assert( cota >= 0 )
		assert( cota > 2-i )
		cota = 2-i

# Postcondicion: 
assert( o != "s" or s==l*a or su==sum(j**2 for j in (1,n) or ar==(3.1416*(r**2))))

# Salida:
print("Hemos terminado")