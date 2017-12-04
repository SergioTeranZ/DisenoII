import random

class RefSet:

	def __init__(self,cap,bag,b,P):
		super(RefSet, self).__init__()
		self.capacidad = cap
		self.bag = bag

		self.solSet = []
		self.beneficios = []
		self.pesos = []
		
		self.Create(b,P)

	def Create(self,b,P):
		self.beneficios = []
		self.pesos = []
		r = random.sample(P, b)
		for ri in r:
			self.solSet.append(ri)
		
		for s in self.solSet:
			s.pesar(self.bag,self.capacidad)
			self.beneficios.append(s.beneficio)
			self.pesos.append(s.peso)
			s.posicion = self.solSet.index(s)

	def order(self):
		newSortB = [ (self.beneficios[i],i) for i in range(len(self.beneficios)) ]
		newSortB = list(reversed(sorted(newSortB)))

		self.pesos      = [ self.pesos[j[1]]      for j in newSortB ]
		self.beneficios = [ self.beneficios[j[1]] for j in newSortB ]

		j =0
		newSolSet = []

		for i in newSortB:
			newSolSet.append(self.solSet[i[1]])
			newSolSet[j].posicion = j
			j += 1
		self.solSet = newSolSet

	def newSubSet(self):
		l = len(self.solSet)
		subSets = []
		subSets3 = []
		for i in range(l):
			for j in range(i+1,l):
				subSet_ij = [self.solSet[i],self.solSet[j]]
				subSets.append(subSet_ij)

		return subSets

	def content(self,sol):
		for solRef in self.solSet:
			if solRef.info == sol.info:
				return True
		return False

	def getBest(self,op):
		best = self.solSet[0]
		error = abs(op - self.solSet[0].beneficio)/op
		return best,error
	