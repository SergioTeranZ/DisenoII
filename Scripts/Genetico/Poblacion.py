import random
from Cromosoma import Cromosoma

class Poblacion:

	def __init__(self, cap,bag):
		super(Poblacion, self).__init__()
		self.capacidad = cap
		self.bag = bag
		self.generacion = []
		self.beneficios = []
		self.pesos = []
		self.errores = []
		self.tipo = None
		self.Populate()


	def Identify(self):
		unique = []
		for t in self.bag:
			diff = abs(t[1]-t[0])
			if not diff in unique:
				unique += [diff]
		print(sorted(unique))
		lu = len(unique)
		lb = len(self.bag)
		e = abs(lb-lu)/lb
		print(e)

	def Populate(self):
		self.beneficios = []
		self.pesos = []
		for c in self.generacion:
			c.pesar(self.bag,self.capacidad)
			self.beneficios += [c.beneficio]
			self.pesos += [c.peso]

	def Health(self,tol):
		for c in self.generacion:
			k = 0
			while (not c.salud) and (k < len(self.bag)):
				c.curar(self.bag,self.capacidad,tol)
				c.diagnosticar(self.capacidad)
				k += 1
		self.Populate()

	def Error(self,op):
		self.errores = []
		for c in self.generacion:
			self.errores +=  [(abs(op-c.beneficio)/op,c.posicion)]
		self.errores = sorted(self.errores)

	def ReturnBest(self,op):
		self.Error(int(op))
		e = self.errores[0][0]
		i = self.errores[0][1]
		b = self.generacion[i]
		return b,e

	def Check(self):
		for c in self.generacion:
			if (self.beneficios.count(c.beneficio)/len(self.generacion) > 0.90) :
				return True

		return False

	def Select(self):
		total = sum(set(self.beneficios))
		p1  = 0
		p2  = 1
		wheel = []
		for b in list(set(self.beneficios)):
			if (b/total)*100 >= 0 :
				wheel += [((b/total)*100,b)]*self.beneficios.count(b)
		wheel = sorted(wheel)

		#rnd = random.sample(wheel,2)
		rnd = [wheel[0],wheel[len(wheel)-2]]

		p1 = self.beneficios.index(rnd[0][1])
		p2 = self.beneficios.index(rnd[1][1])

		return p1,p2


	def Cross(self,p1,p2,chance):
		p = random.random()
		parent1 = self.generacion[p1]
		parent2 = self.generacion[p2]
		alelo = 0
		if p < chance:
			alelo = random.randrange(0,len(self.generacion[p1].info))

		gen1 = list(parent1.info[0:alelo])
		gen2 = list(parent2.info[alelo:len(parent2.info)])

		gen3 = list(parent2.info[0:alelo])
		gen4 = list(parent1.info[alelo:len(parent2.info)])

		info1 = list(gen1 + gen2)
		info2 = list(gen3 + gen4)

		child1 = Cromosoma(info1,0,self.bag,self.capacidad)
		child2 = Cromosoma(info2,0,self.bag,self.capacidad)

		return child1,child2

	def getWorst(self,size):

		lowest = sorted(list(set(self.beneficios)))[0:size]
		iLowest = [ self.beneficios.index(l) for l in lowest]

		cromosomasLow = []
		for cro in self.generacion:
			if cro.posicion in iLowest:
				cromosomasLow += [cro]

		return cromosomasLow

	def Insert(self,newGen):	
		worst = self.getWorst(len(newGen))
		
		take = min( len(newGen), len(worst) )

		for i in range(take-1):
			newGen[i].posicion = worst[i].posicion
			self.generacion[newGen[i].posicion] = newGen[i]
		
		self.Populate()