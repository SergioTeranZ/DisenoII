# generador pesos

import random
pb=[]

for i in range(0,9):
	aux=(random.randrange(19)+1,random.randrange(19)+1)
	pb=pb+[aux]

pb=sorted(pb)
print pb
capacidad=random.randrange(50)+1
capacidad2=capacidad


#generador de pesos[0] y beneficios[1]
#

Continuar=True
Mochila=[]

Beneficio_total=0
intentos_fallidos=25
Beneficios=[]
Mayor_Beneficio=0
indices=[]

print "Capacidad Inicial: "+str(capacidad)
	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25


	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices
Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices
Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices
Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices

Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices
Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices
Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices
Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices
Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices
Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios

print indices
Beneficios=[]
Mayor_Beneficio=0
indices=[]
#print pb2
#for i in range (0,10):

	
for i in range(1,10000):
	Continuar=True
	Mochila=[]

	Beneficio_total=0
	intentos_fallidos=25

	capacidad=capacidad2



	while capacidad>0 or Continuar:
			
			indice=random.randrange(len(pb))
			elemento=pb[indice]

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos-=1

			if intentos_fallidos==0:
				elemento=pb[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]
print Beneficios
print indices