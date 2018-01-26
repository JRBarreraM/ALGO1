"""	Prelab3ejercicio2.py
	DESCRIPCION: Programa que dado un número entero N, \
	cuenta los divisores de N.
		
	Autor: 
		Br. Jose Barrera
	Ultima modificacion: 25/01/2018
	VARIABLES:
	N: int // ENTRADA: Numero al que se le contaran los divisore.
	cuenta: int // SALIDA: Si es bisiesto o no.
	i: int // SALIDA: ?.
"""

# Valores iniciales:
N = int(input("ingrese el numero = "))

# Precondicion: 
{N > 0}

# Calculos:
(cuenta, i) = (0, 1)
while i<=N:
	if N % i == 0:
		cuenta = cuenta + 1
	else:
		pass
	i = i + 1

# Postcondicion: 
{cuenta == (sum j for j in range( 0 < j <= N ) if N % j == 0 )}

# Salida:
print(cuenta)
"""[
const N: int;
var cuenta: int;
var i: int;
{N > 0}
cuenta,i := 0,1;
{inv 0<i<=N+1 /\ cuenta=(%count j: 0<j<i: N mod j = 0 )}
{bound N-i+2 }
do ( i<=N ) ->
if ( N mod i = 0 ) ->
cuenta := cuenta + 1;
[] ( N mod i != 0 )
skip
fi;
i = i+1
od
{cuenta = (%count j: 0<j<= N : N mod j = 0 )}
]

(%oount j: 0<j<= N: N mod j=0)=(%sigma j: 0<j<= N /\ N mod j = 0: 1 )
"""