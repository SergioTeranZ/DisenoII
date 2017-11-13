import random
import math
from time import time

def Generar(c,l):
	pob = []
	i = 0
	while len(pob) < abs(len(l)/(int(math.log(len(l),2)))):
		p = [random.randint(0,1) for _ in range(len(l))]
		pob = pob + [p]
	return pob

def pickRandom(p,c):
	rndI = random.randint(0,len(p)-1)
	while p[rndI] != 1:
		rndI = random.randint(0,len(p)-1)
	return rndI

def Salud(pob,cro,c):
	benT = []
	pesT = []

	# Para cada cromosoma en la poblacion hacer
	for cr in range(len(pob)):
		cromosoma = pob[cr]
		ben = 0
		pes = 0
		pesT = pesT + [0]
		benT = benT + [0]
		# Para cada item en el cromosoma
		for i in range(len(cromosoma)):
			item = cromosoma[i]
			itemCr = cro[i]
			# si esta en incluido (bit = 1)
			# agregar su peso y beneficio a los pesos y beneficios totales
			benT[cr] = benT[cr] + itemCr[0]*item
			pesT[cr] = pesT[cr] + itemCr[1]*item
		
			# Si la capacidad total es MENOR que el volumen total
			while  c < pesT[cr] :
				# escoger de manera aleatoria items del cromosoma hasta obtener uno que este en el el volumen total
				rndItem = pickRandom(cromosoma,cro)

				# Sacar ese item del volumen total (cambiar bit = 0)
				cromosoma[rndItem] = 0
				benT[cr] = benT[cr] - cro[rndItem][0]
				pesT[cr] = pesT[cr] - cro[rndItem][1]
	return benT

def porcentaje(item,l):
	t = 0
	for i in l:
		if i == item :
			t = t + 1
	return (t*1.0)/len(l)

def Chequear(salud):
	unique = sorted(list(set(salud)))
	for u in unique:
		if porcentaje(u,salud) > 0.9 :
			return True
	return False

# Roulette Whell Solution
def Seleccionar(fitness,poblacion):
	porcentajes = []
	whell = [0]*10
	rnd = 0
	p1  = 0
	p2  = 1
	total = 0

	total = sum(fitness)

	for j in range(len(fitness)):
		porcentajes = porcentajes + [(j,fitness[j]/total)]
		a = [j]*( int( (porcentajes[j][1]*100) ) )
		whell = whell + a
		
	if len(whell) != 0:
		rnd = random.randint(0,len(whell)-1)
		p1 = whell[rnd]
		if rnd != 0 :
			p2 = whell[rnd-1]

	return poblacion[p1],poblacion[p2]

def Cruzar(p1,p2,pc):
	p = random.random()
	alelo = 0
	if p < pc:
		alelo = random.randint(1,len(p1)-1)

	gen1 = p1[0:alelo]
	gen2 = p2[alelo:len(p2)]

	gen3 = p2[0:alelo]
	gen4 = p1[alelo:len(p2)]

	ch1 = gen1 + gen2
	ch2 = gen3 + gen4

	return ch1,ch2

def Mutar(child,pm):
	mutante = list(child)

	p = random.random()
	if p < pm:
		alelo = random.randint(1,len(child)-1)
		if mutante[alelo] == 1:
			mutante[alelo] = 0
		else:
			mutante[alelo] = 1

	return mutante

def devolverMayor(fitnessT,i):
	mayor = 0
	pcMayor = 0
	for j in range(len(fitnessT)):
		if porcentaje(fitnessT[j],fitnessT) > pcMayor:
			mayor = fitnessT[j]
	print('Resultado: '+str(mayor)+'\niteracion: '+str(i))
	return mayor

def devolverMayorItem(fitnessT,j):
	mejor = max(fitnessT)
	
	print('Resultado: '+str(mejor)+'\niteracion: '+str(j))
	return mejor

def Error(p,pC):
	return abs(p-pC)/p

def AGS(cap,cromosomas,maxI,cruce,mutar):
	tiempo_inicial = time() 
	# Generar Poblacion inicial de tamaño Cromosomas
	poblacion = Generar(cap,cromosomas)
	
	# Calcular salud de cada cromosoma
	fitnessT = Salud(poblacion,cromosomas,cap)

	i = 0
	while i < maxI:
		nuevaGeneracion = []

		# Verificar que porcentaje de la poblacion tiene el mismo porcentaje de salud
		# Si mas del 90% de la poblacion NO es saludable
		if not Chequear(fitnessT):
			for _ in range( int(len(poblacion)/2) ):
				# Seleccionar dos cromosomas de la poblacion
				[parent1,parent2]  = Seleccionar(fitnessT,poblacion)

				# Cruzar ambos cromosomas
				[child1,child2] = Cruzar(parent1,parent2,cruce)

				# Mutar los cromosomas obtenidos
				mutante1 = Mutar(child1,mutar)
				mutante2 = Mutar(child2,mutar)

				nuevaGeneracion = nuevaGeneracion + [mutante1,mutante2]
			
		
		# Si mas del 90% de la poblacion SI es saludable
		else:
			# Si el numero de iteracion ha superado limite o el 90% es saludable PARAR
			tiempo_final = time() 
			tiempo_ejecucion = tiempo_final - tiempo_inicial
			print('Duracion: '+str(tiempo_ejecucion))
			return devolverMayor(fitnessT,i)
		
		fitnessT = Salud(nuevaGeneracion,cromosomas,cap)

		# Calcular salud de cada cromosoma
		# Si el numero de iteracion NO ha superado limite o el 90% aun NO es saludable repetir ciclo
		i = i+1
	tiempo_final = time() 
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	print('Duracion: '+str(tiempo_ejecucion))
	return devolverMayorItem(fitnessT,i)

def CorrerAGS(maxIt,pCruce,pMutar,scale,nombres):
	for i in range(len(nombres)):

		ruta   ="../../"+scale+"/"+nombres[i]
		rutaOp ="../../"+scale+"-optimum/"+nombres[i]

		archivo   = open(ruta  , "r")
		archivoOp = open(rutaOp, "r")

		linea   = archivo.readline()
		lineaOp = archivoOp.readline()

		optimo = lineaOp

		capacidad = linea.split(" ")[1]
		capacidad = int(capacidad.split('\ ')[0])
		l=[]

		for linea in archivo.readlines():
			b,p=int(linea.split(" ")[0]),int((linea.split(" ")[1]).split('\ ')[0])
			l=l+[(b,p)]

		print("---------------------\nProblema: "+nombres_low[i])
		opAGS = AGS(capacidad,l,maxIt,pCruce,pMutar)
		e = Error(int(optimo),opAGS)
		print('Optimo Real: '+ optimo)
		print('Error: '+ str(e*100)+'%')

print('----------------------------------------------------\n LOW DIMENSION \n----------------------------------------------------')
nombres_low=['f1_l-d_kp_10_269','f2_l-d_kp_20_878']
CorrerAGS(400,0.85,0.001,"low-dimensional",nombres_low)

print('----------------------------------------------------\n LARGE SCALE \n----------------------------------------------------')
nombres_large=['knapPI_3_100_1000_1','knapPI_3_200_1000_1','knapPI_3_500_1000_1','knapPI_3_1000_1000_1','knapPI_3_2000_1000_1','knapPI_3_5000_1000_1','knapPI_1_10000_1000_1','knapPI_2_10000_1000_1','knapPI_3_10000_1000_1']
CorrerAGS(400,0.85,0.001,"large_scale",nombres_large)