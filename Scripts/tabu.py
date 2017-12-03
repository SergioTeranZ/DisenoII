#tabu

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

