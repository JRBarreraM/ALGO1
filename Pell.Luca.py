# Autores: 
#	Br. Jose Barrera y Br. Alfredo Cruz.	

# Pell_Luca iterativo.

def Pell_LucaI(n=int)->int:
	#VAR
		# i,p,s,var: int
	i,p,s=1,1,0
	if n==0:
		return 2
	while n>=i:
		aux=p
		p=2*p+s
		s=aux	
		i=i+1
	return 2*(p+s)

# Pell_Luca recursivo de Cola.
def Pell_Luca(n=int,i=int,p=int,s=int)->int:
	if n==0:
		return 2
	elif n==i:
		return 2*(p+s)
	elif n>i:
		return Pell_Luca(n,i+1,2*p+s,p)
print("La funcion recursiva de cola Pell_Luca")
print("Calcula la Q(n) definida como:")
print("Q(0) = 2")
print("Q(1) = 2")
print("Q(n>1) = 2*Q(n-1)+Q(n-2)")
print("Si se le introducen los valores Pell_Luca(n,1,1,0)")
while True:
	try:
		n=int(input("Ingrese n para comprobarlo "))
		opcion=int(input("iterativo=1 , recursivo de cola = 2  "))
		assert((opcion==1 and 0<=n<=99999) or (opcion==2 and 0<=n<=998))
		break
	except:
		print("n debe ser un entero mayor que 0 y menor que 999(recursivo) y menor 99999(iterativo)")
if opcion==2:
	print(Pell_Luca(n,1,1,0))
elif opcion==1:
	print(Pell_LucaI(n))
