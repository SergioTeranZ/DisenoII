# generador pesos

import random

def mochila(lista,cap):
	capacidad=cap
	Beneficio_total=0
	Continuar=True
	Mochila=[]
	intentos_fallidos=25

	while capacidad>0 or Continuar:

			if len(lista)==0:
				break

			indice=random.randrange(len(lista))
			elemento=lista[indice]
			lista.remove(elemento)

			if (capacidad-elemento[0]>=0):
				intentos_fallidos=25
				capacidad=capacidad-elemento[0]
				Beneficio_total=Beneficio_total+elemento[1]
				Mochila=Mochila+[elemento]
			else:
				intentos_fallidos=intentos_fallidos-1


			if intentos_fallidos==0:
				if len(lista)==0:
					break
				elemento=lista[0]
				if capacidad-elemento[0]>=0:
					intentos_fallidos=25
				else:
					Continuar=False

	return Beneficio_total
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila
	
pb=[]

for i in range(0,39):
	pb=pb+[(random.randrange(99)+1,random.randrange(99)+1)]

pb=sorted(pb)

capacidad=random.randrange(500)+50

print pb
print "Capacidad Inicial: "+str(capacidad)

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]



for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]

for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]

for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]

for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]

for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]

for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]

for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]

for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]


for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]

for i in range(1,10000):
	
	
	Beneficio_total=mochila([(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]
		,capacidad)


	if Beneficio_total>Mayor_Beneficio:
		Mayor_Beneficio=Beneficio_total
		Beneficios=Beneficios+[Mayor_Beneficio]
		indices=indices+[i]

print Beneficios
print indices

Beneficio_total=0
Beneficios=[]
Mayor_Beneficio=0
indices=[]


