#tabu

#[0] beneficio
#[1] peso
#
import random
from time import time
import math

global lista_tabu

def Sol_inicial(lista,cap):
	elementos=list(lista)
	capacidad=cap
	Mochila=[0]*len(lista)
	indices=[];

	for i in range(3):
		indice=random.randrange(len(elementos))
		elemento=elementos[indice]
		
		if  not(indice in indices):
			if capacidad-elemento[1]<=0:
				break

			
			Mochila[indice]=1
			indices=indices+[indice]
			
			capacidad=capacidad-elemento[1]
		

	return Mochila

def Evaluar_Vecindad(vecindad,elementos,capacidad):
	beneficio_acual,peso_actual=0,0
	for i in range(len(vecindad)):

		if vecindad[i]==1:
			beneficio_acual=beneficio_acual+elementos[i][0]
			capacidad=capacidad-elementos[i][1]

	if capacidad<0:
		beneficio_acual=beneficio_acual + capacidad*math.sqrt(-capacidad)


	return beneficio_acual

def Busqueda_mejor_vecino(elementos,vecindad,beneficio,capacidad):
	#print capacidad
	Mejor_vecindad=list(vecindad)
		
	for i in range(len(vecindad)):
		Nueva= list(vecindad)
		Nueva[i]=int(not vecindad[i])

		if not(Nueva in lista_tabu):

			nuevo_bene=Evaluar_Vecindad(Nueva,elementos,capacidad)

			if beneficio<nuevo_bene:
				beneficio=nuevo_bene
				Mejor_vecindad=Nueva
				lista_tabu.append(Nueva)

	return beneficio,Mejor_vecindad

def ls_mejor_vecino(l,capacidad,Sol_inicial):
	nuevo_bene=0
	Mejor_vecindad,Mayor_Beneficio= Sol_inicial,0

	diferente=True

	it = 0
	while diferente:
		nuevo_bene,Mejor_vecindad=Busqueda_mejor_vecino(l,Mejor_vecindad,Mayor_Beneficio,capacidad)
		if nuevo_bene>Mayor_Beneficio:
			Mayor_Beneficio=nuevo_bene
		else:
			diferente=False
		
		it = it +1

	return Mayor_Beneficio,it,Mejor_vecindad



nombres2=["knapPI_1_100_1000_1","knapPI_1_200_1000_1","knapPI_1_500_1000_1","knapPI_1_1000_1000_1","knapPI_1_2000_1000_1","knapPI_1_5000_1000_1","knapPI_1_10000_1000_1"]

#,"knapPI_1_5000_1000_1","knapPI_1_10000_1000_1"]



for i in nombres2:

	ruta="../large_scale/"+i
	#ruta="../low-dimensional/"+i

	archivo = open(ruta, "r")

	linea=archivo.readline()
	capacidad= linea.split(" ")[1]
	capacidad=int(capacidad.split('\ ')[0])
	l=[]

	for linea in archivo.readlines():
		b,p=int(linea.split(" ")[0]),int((linea.split(" ")[1]).split('\ ')[0])
		if b==0 and (p==0 or p==1) :
			break
		l=l+[(b,p)]

	print "Problema: "+i
	print len (l)
	
	lista_tabu = []

	sol_ini=Sol_inicial(l,capacidad)
	lista_tabu.append(sol_ini)

	tiempo_inicial = time() 

	mejor_beneficio=0

	for i in range(0,19):
		Mayor_Beneficio,it,Mejor_vecindad=ls_mejor_vecino(l,capacidad,sol_ini)
		if mejor_beneficio<Mayor_Beneficio:
			mejor_beneficio=Mayor_Beneficio
		#sol_ini=cambiar_solucion(Mejor_vecindad)
		sol_ini=Mejor_vecindad


	tiempo_final = time() 
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	#print "lista:"  + str(lista_tabu)
	print mejor_beneficio
	print tiempo_ejecucion