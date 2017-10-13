# generador pesos

import random

def mochila(lista,cap):
	capacidad=cap
	Beneficio_total=0
	Continuar=True
	Mochila=[0]*len(lista)
	intentos_fallidos=25
	indices=[];
	i=1000

	while capacidad>0 and i>0:

		indice=random.randrange(len(lista))
		elemento=lista[indice]
		
		if (capacidad-elemento[0]>=0 and not (indice in indices)):
			capacidad=capacidad-elemento[0]
			Beneficio_total=Beneficio_total+elemento[1]
			Mochila[indice]=1
			indices=indices+[indice]
		
		i=i-1

	return Mochila,Beneficio_total
	#print "Beneficio: "+str(Beneficio_total)+ " Capacidad: "+ str(capacidad)
	#print Mochila

def Busqueda_mejor_vecino(elementos,vecindad,beneficio_acual,capacidad):
	Mejor_vecindad=list(vecindad)
	
	for i in range(len(vecindad)):
		Nueva= list(vecindad)
		Nueva[i]=int(not vecindad[i])
		nuevo_bene,nuevo_peso=Evaular_Vecindad(Nueva,elementos)

		if beneficio_acual<nuevo_bene and (capacidad-nuevo_peso>0):
			beneficio_acual=nuevo_bene
			Mejor_vecindad=Nueva

	return beneficio_acual,Mejor_vecindad


def Busqueda_buen_vecino(elementos,vecindad,beneficio_acual,capacidad):
	Mejor_vecindad=list(vecindad)
	
	for i in range(len(vecindad)):
		Nueva= list(vecindad)
		Nueva[i]=int(not vecindad[i])
		nuevo_bene,nuevo_peso=Evaular_Vecindad(Nueva,elementos)

		if beneficio_acual<nuevo_bene and (capacidad-nuevo_peso>0):
			beneficio_acual=nuevo_bene
			Mejor_vecindad=Nueva
			break

	return beneficio_acual,Mejor_vecindad

def Evaular_Vecindad(vecindad,elementos):
	beneficio_acual=0
	peso_actual=0
	for i in range(len(vecindad)):
		beneficio_acual=beneficio_acual+elementos[i][1]*vecindad[i]
		peso_actual=peso_actual+elementos[i][0]*vecindad[i]
	return beneficio_acual,peso_actual


pb=[]
#for i in range(0,49):
#	pb=pb+[(random.randrange(99)+1,random.randrange(99)+1)]

def ls(pb,capacidad):
	#capacidad=capacidad=random.randrange(500)+50

	#print pb
	#print "Capacidad Inicial: "+str(capacidad)


	nuevo_bene=0
	Mejor_vecindad,Mayor_Beneficio= [0]*len(pb),0
	diferente=True

	#print "Mejor Vecino:"
	it = 0
	while diferente:
		nuevo_bene,Mejor_vecindad=Busqueda_mejor_vecino(pb,Mejor_vecindad,Mayor_Beneficio,capacidad)
		if nuevo_bene>Mayor_Beneficio:
			Mayor_Beneficio=nuevo_bene
		else:
			diferente=False
		print str(Mayor_Beneficio)
		it = it +1
	print "---"

	nuevo_bene=0
	Mejor_vecindad,Mayor_Beneficio= [0]*len(pb),0
	diferente=True

	#print "Cualquier Vecino:"
	it = 0
	while diferente:
		nuevo_bene,Mejor_vecindad=Busqueda_buen_vecino(pb,Mejor_vecindad,Mayor_Beneficio,capacidad)
		if nuevo_bene>Mayor_Beneficio:
			Mayor_Beneficio=nuevo_bene
		else:
			diferente=False
		#print str(Mayor_Beneficio)
		it = it +1

	#print str(it)+","+str(Mayor_Beneficio)
	print "-"

# 10
p1 = sorted([(1, 9), (1, 19), (2, 13), (3, 8), (4, 3), (4, 14), (6, 14), (10, 13), (16, 12)])
c1 = 11

p2 = sorted([(1, 10), (10, 9), (10, 13), (11, 10), (11, 12), (12, 6), (12, 11), (18, 17), (19, 18)])
c2 = 45

# 20
p3 = sorted([(3, 4), (4, 12), (4, 28), (6, 16), (7, 36), (8, 6), (8, 15), (10, 1), (10, 18), (19, 28), (22, 15), (23, 4), (23, 8), (25, 20), (27, 32), (29, 17), (31, 20), (34, 20), (38, 9)])
c3 = 121

p4 = sorted([(1, 28), (1, 37), (2, 34), (3, 37), (9, 11), (11, 16), (14, 38), (15, 15), (17, 27), (18, 19), (18, 26), (24, 37), (25, 3), (25, 31), (28, 33), (29, 13), (32, 27), (38, 38), (39, 16)])
c4 = 57

# 30
p5 = sorted([(1, 21), (3, 38), (3, 53), (8, 55), (9, 5), (9, 58), (11, 6), (11, 19), (16, 15), (20, 25), (25, 2), (25, 26), (27, 40), (29, 2), (31, 43), (34, 35), (36, 8), (39, 7), (41, 9), (42, 36), (46, 42), (46, 59), (48, 51), (49, 29), (51, 33), (51, 41), (53, 17), (57, 37), (58, 53)])
c5 = 166

p6 = sorted([(1, 46), (1, 54), (8, 40), (10, 12), (10, 22), (14, 3), (16, 8), (20, 11), (20, 28), (22, 27), (23, 8), (24, 52), (28, 4), (28, 18), (29, 24), (31, 8), (32, 34), (35, 23), (36, 7), (38, 38), (44, 45), (45, 21), (49, 48), (50, 3), (52, 49), (54, 26), (55, 28), (56, 49), (59, 34)])
c6 = 97

# 40
p7 = sorted([(5, 69), (9, 51), (11, 2), (12, 25), (13, 25), (14, 58), (14, 72), (17, 4), (17, 42), (17, 74), (18, 22), (19, 26), (19, 62), (22, 43), (22, 53), (23, 66), (29, 8), (29, 53), (31, 26), (33, 37), (35, 40), (38, 40), (39, 1), (41, 38), (44, 72), (46, 34), (47, 78), (49, 1), (54, 36), (54, 54), (55, 33), (60, 21), (61, 18), (61, 24), (64, 1), (64, 47), (64, 67), (68, 10), (72, 71)])
c7 = 66

p8 = sorted([(22, 51), (5, 49), (22, 18), (18, 35), (37, 71), (41, 57), (59, 30), (70, 14), (79, 73), (36, 4), (6, 46), (60, 30), (49, 74), (45, 23), (30, 78), (64, 51), (40, 36), (4, 22), (54, 12), (45, 40), (26, 23), (59, 54), (58, 9), (74, 55), (19, 37), (79, 59), (1, 31), (26, 43), (48, 31), (53, 69), (70, 25), (71, 61), (74, 17), (63, 64), (49, 71), (60, 35), (10, 77), (70, 46), (64, 53)])
c8 = 238

# 50
p9 = sorted([(1, 10), (2, 91), (4, 73), (4, 96), (8, 56), (8, 73), (9, 16), (13, 37), (17, 17), (18, 23), (19, 23), (23, 89), (24, 95), (25, 25), (25, 83), (31, 37), (32, 90), (33, 76), (33, 92), (34, 80), (36, 77), (42, 40), (44, 54), (48, 89), (50, 49), (50, 81), (52, 70), (56, 40), (60, 56), (61, 94), (66, 87), (69, 33), (71, 7), (72, 83), (73, 73), (74, 24), (77, 17), (77, 75), (78, 37), (82, 75), (84, 5), (89, 26), (91, 28), (91, 76), (92, 64), (95, 60), (96, 22), (97, 74), (98, 33)])
c9 = 470

p10 = sorted([(17, 77), (55, 97), (88, 10), (20, 32), (49, 71), (26, 48), (48, 82), (96, 64), (20, 86), (72, 81), (56, 7), (49, 84), (40, 55), (54, 55), (25, 18), (42, 93), (92, 73), (37, 63), (67, 76), (24, 32), (47, 66), (7, 87), (50, 34), (72, 70), (64, 47), (99, 4), (17, 4), (72, 7), (86, 67), (93, 16), (21, 38), (44, 74), (87, 7), (9, 85), (72, 19), (79, 46), (12, 28), (51, 42), (30, 12), (28, 22), (73, 84), (95, 86), (61, 13), (91, 87), (53, 40), (23, 7), (19, 95), (53, 4), (73, 9)])
c10 = 207

print("\n\np1")
ls(p1,c1)

print("\n\np2")
ls(p2,c2)

print("\n\np3")
ls(p3,c3)

print("\n\np4")
ls(p4,c4)

print("\n\np5")
ls(p5,c5)

print("\n\np6")
ls(p6,c6)

print("\n\np7")
ls(p7,c7)

print("\n\np8")
ls(p8,c8)

print("\n\np9")
ls(p9,c9)

print("\n\np10")
ls(p10,c10)