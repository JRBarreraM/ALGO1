"""	Prelab3ejercicio1.py
	DESCRIPCION: Programa que dado un N, \
	calcula la suma de los factoriales desde 0 hasta N.
	Dice si es bisiesto o no.
		
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 25/01/2018
	VARIABLES:
	anyo: int // ENTRADA: Numero del año.
	esBisiesto: bool // SALIDA: Si es bisiesto o no.
"""

# Valores iniciales:
[
const N: int;
var suma: int;
var fact: int;
var k: int;
{N >= 0}
suma,fact,k := 0,1,0;
{inv 0<=k<=N+1 /\ suma = (%sigma i: 0<=i<k: (%pi j: 1<=j<=i: j)) /\
 fact = (%pi j: 1<=j<=k: j) }
{bound N+1-k}
do ( k<=N ) ->
if ( k > 0 ) ->
fact := fact * k
[]
skip;
fi;
suma := suma + fact;
k := k + 1
od
{ suma = (%sigma i: 0<=i<=N: (%pi j: 1<=j<=i: j)) }
]

def prod( iterable ):
p= 1
for n in iterable:
p *= n
return p

prod (j for j in range(1,i)).