import random
import math
from time import time
from Cromosoma import Cromosoma
from Poblacion import Poblacion
import sys
from helpMethods import *

def SGA(cap,cromosomas,maxI,cruce,mutar,optimo):
	tiempoI = time() 
	# Generar Poblacion inicial de tamaño Cromosomas
	poblacion = Generate(cap,cromosomas)
	
	i = 0
	while i < maxI:
		# Calcular salud de cada cromosoma
		poblacion.Health()

		# Verificar que porcentaje de la poblacion tiene el mismo porcentaje de salud
		# Si mas del 90% de la poblacion NO es saludable
		if not poblacion.Check():
			# Seleccionar dos cromosomas de la poblacion
			[father,mother] = poblacion.Select()

			# Cruzar ambos cromosomas
			[child1,child2] = poblacion.Cross(father,mother,cruce)

			# Mutar los cromosomas obtenidos
			mutante1 = child1.mutar(mutar,poblacion.bag,poblacion.capacidad)
			mutante2 = child2.mutar(mutar,poblacion.bag,poblacion.capacidad)

			poblacion.Insert([mutante1,mutante2,poblacion.generacion[father],poblacion.generacion[mother]])

			# Calcular salud de cada cromosoma
			poblacion.Health()
		
		# Si mas del 90% de la poblacion SI es saludable
		else:
			# Si el numero de iteracion ha superado limite o el 90% es saludable PARAR
			tiempoF = time() 
			tiempoT = tiempoF - tiempoI
			[best,error] = poblacion.ReturnBest(optimo)
			return [best,i,tiempoT,error]

		# Si el numero de iteracion NO ha superado limite o el 90% aun NO es saludable entonces repetir el ciclo
		i = i+1
	
	tiempoF = time() 
	tiempoT = tiempoF - tiempoI
	[best,error] = poblacion.ReturnBest(optimo)
	return [best,i,tiempoT,error]

def Generate(c,bag):
	p = Poblacion(c,bag)
	i = 0
	l = len(bag)

	size = int(l/2) if int(l/math.log(l,2)) > 5 else int(l*4)
	
	if int(l/2) > 499:
		size = int(l/math.log(l,2)) 
	
	for i in range(size):
		info = [random.randint(0,1) for _ in range(l)]
		crom = Cromosoma(info,i,bag,c)
		p.generacion += [crom]
	return p

def CorrerSGA(maxI,pCruce,pMutar,scale,nombre):
	[C,V,opt] = openFile(scale,nombre)
	[sga,i,t,e] = SGA(C,V,maxI,pCruce,pMutar,opt)
	return int(opt),sga.beneficio,e,i,t

def promedios(iMax,c,m,times,scale,nombres,mode,limits = ""):
	style = 't' if '-t' in sys.argv else 'e' if '-e' in sys.argv else 'n'
	
	for f in nombres:
		resultados = []
		for _ in range(times):
			resultados.append(CorrerSGA(iMax,c,m,scale,f))

		promedios = [ sum([ resultados[i][j] for i in range(len(resultados)) ])/len(resultados) for j in range(5) ]
		printResultado(f,style,mode,times,scale,limits,opt=int(promedios[0]),sga=truncate(promedios[1],2),err=truncate(promedios[2]*100,3),ite=promedios[3],tim=truncate(promedios[4],4))
		
		if '-d' in sys.argv:
			printResultado(f,'d',mode,times,scale,limits,resultados= resultados)

def runLow(iMax,c,m,times):
	mode = "screen"
	if '-f' in sys.argv:
		mode = 'file'
	nombres_low = ["f4_l-d_kp_4_11","f3_l-d_kp_4_20","f9_l-d_kp_5_80","f7_l-d_kp_7_50","f6_l-d_kp_10_60","f1_l-d_kp_10_269","f2_l-d_kp_20_878","f10_l-d_kp_20_879","f8_l-d_kp_23_10000"]
	promedios(iMax,c,m,times,"low-dimensional",nombres_low,mode)

def runLarge(iMax,c,m,times,setProblems):	
	nombres = [ ["knapPI_"+str(i+1)+"_"+ str(j) +"_1000_1" for j in setProblems] for i in range(3)]

	mode = "screen"
	limits = ""
	if '-f' in sys.argv:
		limits = str(setProblems[0])+'-'+str(setProblems[-1])
		mode = 'file'

	if mode == "screen":
		printTitle('UNCORRELATED')
	promedios(iMax,c,m,times,"large_scale",nombres[0],mode,limits)
	
	if mode == "screen":
		printTitle('WEAKLY')
	promedios(iMax,c,m,times,"large_scale",nombres[1],mode,limits)
	
	if mode == "screen":
		printTitle('STRONGLY')
	promedios(iMax,c,m,times,"large_scale",nombres[2],mode,limits)

def _main():
	[gen,rep,mut,times] = setParameters(sys)
	tl    = 0
	tL    = 0
	Set   = [[]     ,[100,200,500],[1000,2000,5000],[]]
	scale = ['LOW','100-500','1000-5000',""]

	if '--low' in sys.argv:
		if not '-f' in sys.argv:
			printTitle(scale[0] +'('+str(times)+')')
		runLow(gen,rep,mut,times)
	
	if '--500' in sys.argv:
		times = int(times/2)
		if not '-f' in sys.argv:
			printTitle( scale[1] +'('+str(times)+')')
		runLarge(gen,rep,mut,times,Set[1])
	
	if '--1000' in sys.argv:
		times = int(times/4)
		if not '-f' in sys.argv:
			printTitle( scale[2] +'('+str(times)+')')
		runLarge(gen,rep,mut,times,Set[2])
	
	if '--test' in sys.argv:
		times = int(times/4)
		if not '-f' in sys.argv:
			printTitle( scale[3] +'('+str(times)+')')
		Set[3]   = [int(sys.argv[sys.argv.index('--test')+1])]
		scale[3] = [str(Set[3][0])+'(test)']
		runLarge(gen,rep,mut,times,Set[3])

_main()