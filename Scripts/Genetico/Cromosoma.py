import random
import math

class Cromosoma:
	"""docstring for Cromosoma"""

	def __init__(self, info,posicion,bag,cap):
		super(Cromosoma, self).__init__()
		self.info = info
		self.beneficio = 0
		self.peso = 0
		self.salud = False
		self.posicion = posicion
		
		self.pesar(bag,cap)
		self.diagnosticar(cap)
	
	def diagnosticar(self,cap):
		self.salud = self.peso <= cap

	def curar(self,bag,cap,tol):
		'''
		rnd = random.sample([i for i in range(0,len(bag)-1)],int(len(bag)/2))

		r = (self.beneficio/self.peso)
		d = int(len(bag)/2)
		m = cap/d

		took1 = False
		took2 = False

		for i in rnd:
			if not took2:
				if self.info[i] == 1:
					self.info[i] = 0
					self.beneficio -= bag[i][0]
					self.peso -= bag[i][1]
					took1 = True
				else:
					if took1:
						self.info[i] = 1
						self.beneficio += bag[i][0]
						self.peso += bag[i][1]
						took2 = True
		'''
		mayor = (-10,-10)
		for i in range(len(self.info)):
			if self.info[i] == 1 and mayor[0] < (bag[i][1]/bag[i][0]):
				mayor = (bag[i][1]/bag[i][0],i)
		
		self.info[mayor[1]] = 0
		self.pesar(bag,cap)

	def pesar(self,bag,cap):
		self.beneficio = 0
		self.peso = 0
		for i in range(len(self.info)):
			self.beneficio += self.info[i]*bag[i][0]
			self.peso += self.info[i]*bag[i][1]

		self.beneficio -= (self.peso - cap)

	def mutar(self,chance,bag,cap):
		p = random.random()
		mutante = Cromosoma(list(self.info),self.posicion,bag,cap)
		if p < chance:
			alelo = random.randrange(0,len(self.info))
			if mutante.info[alelo] == 1:
				mutante.info[alelo] = 0
			else:
				mutante.info[alelo] = 1
		mutante.pesar(bag,cap)
		mutante.diagnosticar(cap)
		return mutante

	def print(self):
		print("Info: ")
		print(self.info)
		print("Salud: "+str(self.salud)+"\nposicion: "+str(self.posicion)+"\nBeneficio: "+str(self.beneficio)+"\nPeso: "+str(self.peso)+"\n-------")
		print("posicion: "+str(self.posicion)+"\n-------")
		print("beneficio: "+str(self.beneficio)+"\n-------")

	def printOn(self):
		on = []
		for i in range(len(self.info)):
			if self.info[i] == 1:
				on += [i]
		print(on)