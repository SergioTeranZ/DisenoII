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
		
		self.pesar(bag)
		self.diagnosticar(cap)
	
	def diagnosticar(self,cap):
		self.salud = self.peso <= cap

	def curar(self,bag,cap,tol):
		rnd = random.sample([i for i in range(0,len(bag)-1)],int(len(bag)/2))
		
		r = (self.beneficio/self.peso)
		d = int(len(bag)/2)
		m = cap/d
		'''
		print('    '+str(abs(r)))
		print(abs(cap))
		print('    '+str(abs(r/cacp)))
		print(m)
		'''
		j = 0
		while (not j == 2) and (j < len(rnd)):
			i = rnd[j]
			if self.info[i] == 1:
				
				q = self.beneficio*m
				n = self.beneficio-bag[i][0]
				e = abs(q - n)/q
				
				if e > 0.04 :
					self.info[i] = 0
					self.beneficio -= bag[i][0]
					self.peso -= bag[i][1]
			else:
				
				q = (self.peso+bag[i][1])/d
				n = bag[i][1]
				e = abs(q - n)/q
				
				if e > tol :
					self.info[i] = 1
					self.beneficio += bag[i][0]
					self.peso += bag[i][1]
			j += 1
		self.pesar(bag)

	def pesar(self,bag):
		self.beneficio = 0
		self.peso = 0
		for i in range(len(self.info)):
			self.beneficio += self.info[i]*bag[i][0]
			self.peso += self.info[i]*bag[i][1]

	def mutar(self,chance,bag,cap):
		p = random.random()
		mutante = Cromosoma(list(self.info),self.posicion,bag,cap)
		if p < chance:
			alelo = random.randrange(0,len(self.info))
			if mutante.info[alelo] == 1:
				mutante.info[alelo] = 0
			else:
				mutante.info[alelo] = 1
		mutante.pesar(bag)
		mutante.diagnosticar(cap)
		return mutante

	def print(self):
		#print("Info: ")
		#print(self.info)
		#print("Salud: "+str(self.salud)+"\nposicion: "+str(self.posicion)+"\nBeneficio: "+str(self.beneficio)+"\nPeso: "+str(self.peso)+"\n-------")
		#print("posicion: "+str(self.posicion)+"\n-------")
		print("beneficio: "+str(self.beneficio)+"\n-------")

	def printOn(self):
		on = []
		for i in range(len(self.info)):
			if self.info[i] == 1:
				on += [i]
		print(on)