#Buesqueda Local Iterada 2
#[0] beneficio
#[1] peso
#
import random
from time import time
import math


def Sol_inicial(lista,cap):
	elementos=list(lista)
	capacidad=cap
	Mochila=[0]*len(lista)
	indices=[];

	while True:
		indice=random.randrange(len(elementos))
		elemento=elementos[indice]
		
		if  not(indice in indices):
			

			
			Mochila[indice]=1
			indices=indices+[indice]
			if capacidad-elemento[1]<=0:
				break
			capacidad=capacidad-elemento[1]
		
		
	return Mochila

def Evaluar_Vecindad(vecindad,elementos,capacidad):
	cap=capacidad
	beneficio_acual,peso_actual=0,0
	for i in range(len(vecindad)):

		if vecindad[i]==1:
			beneficio_acual=beneficio_acual+elementos[i][0]*vecindad[i]
			capacidad=capacidad-elementos[i][1]*vecindad[i]

	if capacidad<0:
		beneficio_acual=beneficio_acual + capacidad*int(math.sqrt(-1*capacidad))/16


	return beneficio_acual

def Busqueda_mejor_vecino(elementos,vecindad,beneficio,capacidad):

	Mejor_vecindad=list(vecindad)
		
	for i in range(len(vecindad)):
		Nueva= list(vecindad)
		Nueva[i]=int(not vecindad[i])

		nuevo_bene=Evaluar_Vecindad(Nueva,elementos,capacidad)

		if beneficio<nuevo_bene:
			beneficio=nuevo_bene
			Mejor_vecindad=Nueva

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

def cambiar_solucion(Sol):
	nueva_solucion=list(Sol)
	indices=[]

	for i in range(int(math.sqrt(len(Sol)))*10):
		indice=random.randrange(len(Sol))
		if not(indice in indices):
			Sol[indice]= int(not(Sol[indice]))
			indices=indices+[i]


	# for i in range(len(nueva_solucion)):
	# 	if nueva_solucion[i]:
	# 		if random.randrange(2)%2==1:
	# 			nueva_solucion[i]=0

	return nueva_solucion



nombres2=["knapPI_3_5000_1000_1","knapPI_3_10000_1000_1"]

#,"knapPI_1_5000_1000_1","knapPI_1_10000_1000_1"]

for i in nombres2:

	ruta="../large_scale/"+i

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
	sol_ini=Sol_inicial(l,capacidad)
	tiempo_inicial = time() 

	mejor_beneficio=0
	for i in range(0,29):
		Mayor_Beneficio,it,Mejor_vecindad=ls_mejor_vecino(l,capacidad,sol_ini)
		if mejor_beneficio<Mayor_Beneficio:
			mejor_beneficio=Mayor_Beneficio
		sol_ini=cambiar_solucion(Mejor_vecindad)
	tiempo_final = time() 
	tiempo_ejecucion = tiempo_final - tiempo_inicial

	print mejor_beneficio
	print tiempo_ejecucion