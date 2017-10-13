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

	
	
for i in range(0,49):
	pb=pb+[(random.randrange(99)+1,random.randrange(99)+1)]
pb=sorted(pb)
		
#pb=[(5, 69), (9, 51), (11, 2), (12, 25), (13, 25), (14, 58), (14, 72), (17, 4), (17, 42), (17, 74), (18, 22), (19, 26), (19, 62), (22, 43), (22, 53), (23, 66), (29, 8), (29, 53), (31, 26), (33, 37), (35, 40), (38, 40), (39, 1), (41, 38), (44, 72), (46, 34), (47, 78), (49, 1), (54, 36), (54, 54), (55, 33), (60, 21), (61, 18), (61, 24), (64, 1), (64, 47), (64, 67), (68, 10), (72, 71)]
capacidad=capacidad=random.randrange(500)+50

print pb
print "Capacidad Inicial: "+str(capacidad)


nuevo_bene=0
Mejor_vecindad,Mayor_Beneficio= [0]*len(pb),0
diferente=True

while diferente:
	nuevo_bene,Mejor_vecindad=Busqueda_mejor_vecino(pb,Mejor_vecindad,Mayor_Beneficio,capacidad)
	if nuevo_bene>Mayor_Beneficio:
		Mayor_Beneficio=nuevo_bene
	else:
		diferente=False
print "Mejor Vecino:"
print Mayor_Beneficio

nuevo_bene=0
Mejor_vecindad,Mayor_Beneficio= [0]*len(pb),0
diferente=True

while diferente:
	nuevo_bene,Mejor_vecindad=Busqueda_buen_vecino(pb,Mejor_vecindad,Mayor_Beneficio,capacidad)
	if nuevo_bene>Mayor_Beneficio:
		Mayor_Beneficio=nuevo_bene
	else:
		diferente=False
print "Cualquier Vecino:"
print Mayor_Beneficio






