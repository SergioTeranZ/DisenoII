#Buesqueda Local Iterada 
#[0] beneficio
#[1] peso

import random
from time import time

def Sol_inicial(lista,cap):
	elementos=list(lista)
	capacidad=cap
	Beneficio_total=0
	Mochila=[0]*len(lista)
	indices=[];
	i=len(elementos)*len(elementos)

	while capacidad>0 and i>0:

		indice=random.randrange(len(elementos))
		elemento=elementos[indice]
		
		if (capacidad-elemento[1]>=0 and not (indice in indices)):
			capacidad=capacidad-elemento[1]
			Beneficio_total=Beneficio_total+elemento[0]
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
		beneficio_acual=beneficio_acual+elementos[i][0]*vecindad[i]
		peso_actual=peso_actual+elementos[i][1]*vecindad[i]
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

def Generar_Sols(lista,cap):
	Sols=[]
	a=[]
	for i in range(0,14):
		a=Sol_inicial(lista,cap)
		Sols=Sols+[a]
	return Sols

def ls_iterada(l,capacidad,Sol_inicial):
	a,b,it,mayor=0,0,0,0
	cota_sup=len(Sol_inicial)

	tiempo_inicial = time() 
	for i in Sol_inicial:
		b,a=ls_primer_vecino(l,capacidad,i)
		if b>mayor:
			it,mayor=a,b
	tiempo_final = time() 

	tiempo_ejecucion = tiempo_final - tiempo_inicial

	print "Primer Vecino"
	print str(mayor) +" " +str(it)+" " +str(tiempo_ejecucion)
	print "-----------------------------"


	a,b,it,mayor=0,0,0,0

	tiempo_inicial = time() 
	for i in Sol_inicial:
		b,a=ls_mejor_vecino(l,capacidad,i)
		if b>mayor:
			it,mayor=a,b
	tiempo_final = time() 

	tiempo_ejecucion = tiempo_final - tiempo_inicial

	print "Mejor Vecino"
	print str(mayor) +" " +str(it)+" " +str(tiempo_ejecucion)
	print "-----------------------------"

nombres=['f1_l-d_kp_10_269',"f2_l-d_kp_20_878","f3_l-d_kp_4_20","f4_l-d_kp_4_11","f6_l-d_kp_10_60","f7_l-d_kp_7_50","f8_l-d_kp_23_10000","f9_l-d_kp_5_80","f10_l-d_kp_20_879"]
nombres2=["knapPI_1_100_1000_1","knapPI_1_200_1000_1","knapPI_1_500_1000_1","knapPI_1_1000_1000_1","knapPI_1_2000_1000_1","knapPI_1_5000_1000_1","knapPI_1_10000_1000_1"]
#"knapPI_2_100_1000_1","knapPI_2_200_1000_1","knapPI_2_500_1000_1","knapPI_2_1000_1000_1","knapPI_2_2000_1000_1","knapPI_2_5000_1000_1","knapPI_2_10000_1000_1","knapPI_3_100_1000_1","knapPI_3_200_1000_1","knapPI_3_500_1000_1","knapPI_3_1000_1000_1","knapPI_3_2000_1000_1","knapPI_3_5000_1000_1","knapPI_3_10000_1000_1"]

for i in nombres2:

	ruta="../large_scale/"+i

	archivo = open(ruta, "r")

	linea=archivo.readline()
	capacidad= linea.split(" ")[1]
	capacidad=int(capacidad.split('\ ')[0])
	l=[]

	for linea in archivo.readlines():

		b,p=int(linea.split(" ")[0]),int((linea.split(" ")[1]).split('\ ')[0])
		l=l+[(b,p)]

	print "Problema: "+i
	#print l
	Sol=Generar_Sols(l,capacidad)
	ls_iterada(l,capacidad,Sol)



