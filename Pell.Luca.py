"""
Razonamiento:
# Q(0) = 2
# Q(1) = 2
# Q(n>1) = 2*Q(n-1)+Q(n-2)
# 2,2,6,14,34,82,
# Pell.Luca(n,i,p,s)={	2 si n==0 
						2*(p+s) si i==n	
	i,p,s=1,1,0
						(n,i+1,(2*p)+s,p) si n>i
				}														
																		p(5,1,,)
																		p(5,2,5,12)
																		p(5,3,2,5)
																		p(5,4,1,2)
																		p()
				Pell.Luca(0,0,1)										Pell.Luca(n,i,p,s)
																		Pell.Luca(5,1,1,0)
Q(2)=2*Q(1)+Q(0)=2*2+2=6												Pell.Luca(5,2,2,1)
Q(3)=2*Q(2)+Q(1)=2*(2*Q(1)+Q(0))+Q(1)=5Q(1)+2Q(0)=5*2+2*2				Pell.Luca(5,3,5,2)
Q(4)=2*Q(3)+Q(2)=2*(5Q(1)+2Q(0))+2*Q(1)+Q(0)=12*Q(1)+5*Q(0)=12*2+5*2	Pell.Luca(5,4,12,5)
Q(5)=2*Q(4)+Q(13)=2*(12*Q(1)+5*Q(0))+(5Q(1)+2Q(0))=29*Q(1)+12*Q(0)		Pell.Luca(5,5,29,12)
"""
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
