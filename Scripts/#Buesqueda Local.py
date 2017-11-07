#Buesqueda Local Iterada 

import random
from time import time

def Sol_inicial(lista,cap):
	elementos=list(lista)
	capacidad=cap
	Beneficio_total=0
	Mochila=[0]*len(lista)
	intentos_fallidos=25
	indices=[];
	i=1000

	while capacidad>0 and i>0:

		indice=random.randrange(len(elementos))
		elemento=elementos[indice]
		
		if (capacidad-elemento[0]>=0 and not (indice in indices)):
			capacidad=capacidad-elemento[0]
			Beneficio_total=Beneficio_total+elemento[1]
			Mochila[indice]=1
			indices=indices+[indice]
		
		
		i=i-1

	return Mochila
	
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

def ls_mejor_vecino(pb,capacidad,Sol_inicial):
	nuevo_bene=0
	Mejor_vecindad,Mayor_Beneficio= Sol_inicial,0
	#print Mejor_vecindad
	diferente=True

	it = 0
	while diferente:
		nuevo_bene,Mejor_vecindad=Busqueda_mejor_vecino(pb,Mejor_vecindad,Mayor_Beneficio,capacidad)
		if nuevo_bene>Mayor_Beneficio:
			Mayor_Beneficio=nuevo_bene
		else:
			diferente=False
		
		it = it +1
		
	
	# print Mejor_vecindad
	# print str(Mayor_Beneficio)
	# print "---"
	return Mayor_Beneficio,it

def ls_primer_vecino(pb,capacidad,Sol_inicial):
	nuevo_bene=0
	Mejor_vecindad,Mayor_Beneficio= Sol_inicial,0
	diferente=True

	it = 0
	while diferente:
		nuevo_bene,Mejor_vecindad=Busqueda_buen_vecino(pb,Mejor_vecindad,Mayor_Beneficio,capacidad)
		if nuevo_bene>Mayor_Beneficio:
			Mayor_Beneficio=nuevo_bene
		else:
			diferente=False
		
		it = it +1
	
	# print Mejor_vecindad
	# print str(Mayor_Beneficio)
	# print "---"
	return Mayor_Beneficio,it


l=[(1, 9), (1, 19), (2, 13), (3, 8), (4, 3), (4, 14), (6, 14), (10, 13), (16, 12)]
capacidad=30


a,b,it,acum=0,0,0,0
cota_sup=1000
tiempo_inicial = time() 
for i in range(1,cota_sup):
	Sol=Sol_inicial(l,capacidad)
	b,a=ls_primer_vecino(l,capacidad,Sol)
	it,acum=it+a,b+acum
acum,it=acum/cota_sup, it/cota_sup
tiempo_final = time() 

tiempo_ejecucion = tiempo_final - tiempo_inicial

print acum
print tiempo_ejecucion
print it



