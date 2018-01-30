"""	Lab02ejercicio2.py
	DESCRIPCION: Programa que dada la edad de un ciudadano y \
	si es descendiente extranjero. Dice si puede botar o no.
		
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 23/01/2018
	VARIABLES:
	edad: int // ENTRADA: Edad del ciudadano.
	esDescendienteExtranjero: booleano // ENTRADA: Si es descendiente extranjero o no.
	puedeVotar: bool // SALIDA: Si puede votar o no.
"""

# Valores iniciales:
edad = int(input("Que edad tiene el ciudadano? "))
esDescendienteExtranjero = str(input("El ciudadano es descendiente extranjero? (si/no) "))

# Precondicion: 
assert(0 < edad < 120)

# Calculos:
puedeVotar = True
if esDescendienteExtranjero == "si":
	if (edad >= 25):
		pass
	else:
		puedeVotar = False;
elif esDescendienteExtranjero == "no":
	if (edad >= 18):
		pass
	else:
		puedeVotar = False

# Postcondicion: 
assert( ( (esDescendienteExtranjero == "no") or (edad < 25 ) or (puedeVotar == True) ) \
and ( (esDescendienteExtranjero == "si") or (edad < 18 ) or (puedeVotar == True) ) \
and ( (esDescendienteExtranjero == "no") or (edad >= 25 ) or (puedeVotar == False) ) \
and ( (esDescendienteExtranjero == "si") or (edad >= 18 ) or (puedeVotar == False) ) )

# Salida:
print(puedeVotar)