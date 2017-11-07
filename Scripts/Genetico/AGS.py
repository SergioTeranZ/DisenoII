import random

def Leer():
	c = 269
	x = [(55, 95),(10, 4),(47, 60),(5, 32),(4, 23),(50, 72),(8, 80),(61, 62),(85, 65),(87, 46)]
	return c,x

def solVal(a,b,c):
	m = 0
	for i in range(len(a)) :
		m = m + a[i]*b[i][1]
	
	if m < c:
		return True

	return False

def Generar(c,l):
	pob = []
	i = 0
	while len(pob) != len(l):
		p = [random.randint(0,1) for _ in range(len(l))]
		#if solVal(p,l,c):
		#	pob = pob + [p]
		pob = pob + [p]
	return pob

def pickRandom(p,c):
	rndI = 0
	while p[rndI] != 1:
		rndI = random.randint(0,len(p)-1)
		if p[rndI] == 1 :
			return rndI
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
			if item == 1 :
				# agregar su peso y beneficio a los pesos y beneficios totales
				benT[cr] = benT[cr] + itemCr[0]
				pesT[cr] = pesT[cr] + itemCr[1]
		
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
	for i in range(len(l)):
		if l[i] == item :
			t = t + 1
	return (t*1.0)/len(l)

def Chequear(salud,cro):
	unique = sorted(list(set(salud)))
	for u in range(len(unique)):
		if porcentaje(unique[u],salud) > 0.9 :
			return True
	return False

# Roulette Whell Solution
def Seleccionar(fitness,poblacion):
	parents = []
	for i in range(len(fitness)):
		parents = parents + [(fitness[i],i)]
	
	roulette = list(reversed(sorted(parents)))
	porcentajes = []

	total = 0
	for i in fitness:
		total = total + i

	for j in range(len(fitness)):
		porcentajes = porcentajes + [fitness[j]/total]

	whell = []
	for k in range(len(porcentajes)):
		a = [k]*int((porcentajes[k]*100)//1)
		whell = whell + a

	p1 = whell[random.randint(0,len(whell)-1)]
	p2 = whell[random.randint(0,len(whell)-1)]

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
	print('iteracion: '+str(i))
	print('Optimo: '+str(mayor))
	return mayor

def devolverMayorItem(fitnessT,j):
	mejor = 0
	for i in fitnessT:
		if i > mejor:
			mejor = i
	print('iteracion: '+str(j))
	print('Optimo: '+str(mejor))
	return mejor

def AGS(maxI,cruce,mutar):
	# Leer archivo de entrada
	[cap,cromosomas] = Leer()

	# Generar Poblacion inicial de tamaño Cromosomas
	poblacion = Generar(cap,cromosomas)
	
	# Calcular salud de cada cromosoma
	fitnessT = Salud(poblacion,cromosomas,cap)

	i = 0
	while i < maxI:
		nuevaGeneracion = []

		# Verificar que porcentaje de la poblacion tiene el mismo porcentaje de salud
		# Si mas del 90% de la poblacion NO es saludable
		if not Chequear(fitnessT,cromosomas):

			for gen in range(len(poblacion)//2):
				# Seleccionar dos cromosomas de la poblacion
				[parent1,parent2]  = Seleccionar(fitnessT,poblacion)

				# Cruzar ambos cromosomas
				[child1,child2] = Cruzar(parent1,parent2,cruce)

				# Mutar los cromosomas obtenidos
				mutante1 = Mutar(child1,mutar)
				mutante2 = Mutar(child2,mutar)

				nuevaGeneracion = nuevaGeneracion + [mutante1,mutante2]
		
			# Calcular salud de cada cromosoma
			fitnessT = Salud(nuevaGeneracion,cromosomas,cap)
		
		# Si mas del 90% de la poblacion SI es saludable
		else:
			# Si el numero de iteracion ha superado limite o el 90% es saludable PARAR
			return devolverMayor(fitnessT,i)

		# Si el numero de iteracion NO ha superado limite o el 90% aun NO es saludable repetir ciclo
		i = i+1
	devolverMayorItem(fitnessT,i)

AGS(400,0.75,0.005)