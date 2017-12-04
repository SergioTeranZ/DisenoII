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

	def curar(self,bag,cap):
		mayor = (-10,-10)
		for i in range(len(self.info)):
			if self.info[i] == 1 and mayor[0] < (bag[i][1]/bag[i][0]):
				mayor = (bag[i][1]/bag[i][0],i)
		
		self.info[mayor[1]] = 0
		self.pesar(bag,cap)

	def pesar(self,bag,cap):
		newB = sum([self.info[i]*bag[i][0] for i in range(len(self.info)) ])
		newP = sum([self.info[i]*bag[i][1] for i in range(len(self.info)) ])

		self.peso      = newP
		self.diagnosticar(cap)
		self.beneficio = newB - (self.peso - cap) if not self.salud else newB


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