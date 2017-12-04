class Solution:

	def __init__(self, info,posicion,bag,cap):
		super(Solution, self).__init__()
		self.info = info
		self.beneficio = 0
		self.peso = 0
		self.aporte = False
		self.posicion = posicion
		
		self.pesar(bag,cap)
		self.diagnosticar(cap)

	def print(self):
		print('posicion: '+str(self.posicion))
		print('beneficio: '+str(self.beneficio))
		print('peso: '+str(self.peso))

	def getBestProportion(self,items):
		best = (1000,0)
		for i in range(len(self.info)):
			if self.info[i] == 1 and items[i][1]/items[i][0] < best[0]:
				best = (items[i][1]/items[i][0],i)
		return best[1]

	def pesar(self,bag,cap):
		newB = sum([self.info[i]*bag[i][0] for i in range(len(self.info)) ])
		newP = sum([self.info[i]*bag[i][1] for i in range(len(self.info)) ])

		self.peso      = newP
		self.diagnosticar(cap)
		self.beneficio = newB - (self.peso - cap) if not self.aporte else newB


	def diagnosticar(self,cap):
		self.aporte = self.peso <= cap

	def feasible(self,items,cap):
		mayor = (-10,-10)
		have1 = 1 in self.info

		for i in range(len(self.info)):
			if self.info[i] == 1 and mayor[0] < (items[i][1]/items[i][0]):
				mayor = (items[i][1]/items[i][0],i)
				have1 = True
		if have1:
			self.info[mayor[1]] += pow(-1,self.info[mayor[1]])
			self.pesar(items,cap)

	def improve(self,items,cap):
		mayor = (1000,1000)
		have0 = 0 in self.info

		while have0 and self.aporte:
			for i in range(len(self.info)):
				if self.info[i] == 0 and mayor[0] > (items[i][1]/items[i][0]) and self.peso+items[i][1] <= cap:
					mayor = (items[i][1]/items[i][0],i)
			if mayor == (1000,1000):
				have0 = False
			else:
				self.info[mayor[1]] += pow(-1,self.info[mayor[1]])
				self.pesar(items,cap)
				self.diagnosticar(cap)
				mayor = (1000,1000)

