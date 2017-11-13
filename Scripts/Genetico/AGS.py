import random
import math
from time import time
from Cromosoma import Cromosoma
from Poblacion import Poblacion

def Generate(c,bag):
	p = Poblacion(c,bag)
	i = 0
	l = len(bag)
	size = int(l/math.log(l,2))
	#size = int(l/2)
	
	for i in range(size):
		info = [random.randint(0,1) for _ in range(l)]
		crom = Cromosoma(info,i,bag,c)
		p.generacion += [crom]
	return p

def SGA(cap,cromosomas,maxI,cruce,mutar,cura,optimo):
	tiempoI = time() 
	# Generar Poblacion inicial de tamaño Cromosomas
	poblacion = Generate(cap,cromosomas)
	#poblacion.Identify()
	
	i = 0
	
	while i < maxI:
		# Calcular salud de cada cromosoma
		poblacion.Health(cura)

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
			poblacion.Health(cura)
		
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

def truncate(n,m):
	s = '{}'.format(n)
	if 'e' in s or 'E' in s:
		return '{0:.{1}f}'.format(n,m)
	i,p,d = s.partition('.')
	return '.'.join([i, (d+'0'*m)[:m]])

def printResultado(optimo,obtenido,error,iteracion,tiempo,file):
	print("Optimo: "+str(optimo))
	print("Resultado: "+str(obtenido))
	print("Error: "+str(error))
	#print("Error: "+str(error*100)+"%")
	print("Iteracion: "+str(iteracion))
	print("Tiempo: "+str(tiempo))
	print("----------------------")

def printResultadoTabla(optimo,obtenido,error,iteracion,tiempo,file):
	print("=================================================================================================================")
	print("Problema: "+file)
	print("=================================================================================================================")
	print("||\t Optimo \t|\t Resultado \t|\t Error \t|\t Iteracion \t|\t Tiempo \t||")
	print("-----------------------------------------------------------------------------------------------------------------")
	print("||\t"+str(optimo)+"\t\t|\t"+str(obtenido)+"\t\t|\t"+str(truncate(error*100,3))+"%\t|\t"+str(iteracion)+"\t\t|\t"+str(truncate(tiempo,5))+"\t\t||")


def comparar(a,b):
	dif = []
	for i in range(len(a.info)):
		if not a.info[i] == b.info[i]:
			dif += [i]
	return dif

def CorrerSGA(maxIt,pCruce,pMutar,tCura,scale,nombre):

	ruta   ="../../"+scale+"/"+nombre
	rutaOp ="../../"+scale+"-optimum/"+nombre

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

	l = l[0:len(l)-1]

	[opSGA,j,t,e] = SGA(capacidad,l,maxIt,pCruce,pMutar,tCura,optimo)
	return int(optimo),opSGA.beneficio,e,j,t

def promedios(iMax,c,m,t,times,scale,nombres):
	add = 0.005
	for f in nombres:
		optimos = [0]*times
		opSGAs = [0]*times
		es = [0]*times
		its = [0]*times
		ts = [0]*times
		for k in range(times):
			[optimos[k],opSGAs[k],es[k],its[k],ts[k]] = CorrerSGA(iMax,c,m,t+add,scale,f)
			add += 0.003

		optimoP = int(sum(optimos)/len(optimos))
		opSGAP = sum(opSGAs)/len(opSGAs)
		eP = sum(es)/len(es)
		itP = sum(its)/len(its)
		tP = sum(ts)/len(ts)
		#printResultado(optimoP,opSGAP,eP,itP,tP,f)
		printResultadoTabla(optimoP,opSGAP,eP,itP,tP,f)

def correr(iMax,c,m,times):
	print('=================================================================================================================\n\n\n LOW DIMENSION \n\n\n=================================================================================================================')
	nombres_low = ["f4_l-d_kp_4_11","f3_l-d_kp_4_20","f9_l-d_kp_5_80","f7_l-d_kp_7_50","f6_l-d_kp_10_60","f1_l-d_kp_10_269","f2_l-d_kp_20_878","f10_l-d_kp_20_879","f8_l-d_kp_23_10000"]
	promedios(iMax,c,m,0.955,times,"low-dimensional",nombres_low)

	print('=================================================================================================================\n\n\n LARGE SCALE \n\n\n=================================================================================================================')	

	print('=================================================================================================================\n\n UNCORRELATED \n\n=================================================================================================================')
	nombres_large_u = ["knapPI_1_100_1000_1","knapPI_1_200_1000_1","knapPI_1_500_1000_1","knapPI_1_1000_1000_1","knapPI_1_2000_1000_1","knapPI_1_5000_1000_1","knapPI_1_10000_1000_1"]
	promedios(iMax,c,m,0.955,times,"large_scale",nombres_large_u)
	
	#print('=================================================================================================================\n\n WEAKLY \n\n=================================================================================================================')
	nombres_large_w = ["knapPI_2_100_1000_1","knapPI_2_200_1000_1","knapPI_2_500_1000_1","knapPI_2_1000_1000_1","knapPI_2_2000_1000_1","knapPI_2_5000_1000_1","knapPI_2_10000_1000_1"]
	#promedios(iMax,c,m,0.955,times,"large_scale",nombres_large_w)
	
	print('=================================================================================================================\n\n STRONGLY \n\n=================================================================================================================')
	nombres_large_s = ["knapPI_3_100_1000_1","knapPI_3_200_1000_1","knapPI_3_500_1000_1","knapPI_3_1000_1000_1","knapPI_3_2000_1000_1","knapPI_3_5000_1000_1","knapPI_3_10000_1000_1"]
	promedios(iMax,c,m,0.999,times,"large_scale",nombres_large_s)


def test(iMax,c,m,times):
	s = str(100)
	#print('=================================================================================================================\n\n\n PRUEBA \n\n\n=================================================================================================================')	

	print('=================================================================================================================\n\n UNCORRELATED \n\n=================================================================================================================')
	nombres_large_u = ["knapPI_1_100_1000_1","knapPI_1_200_1000_1","knapPI_1_500_1000_1","knapPI_1_1000_1000_1","knapPI_1_2000_1000_1","knapPI_1_5000_1000_1","knapPI_1_10000_1000_1"]
	#nombres_large_u = ["knapPI_1_"+s+"_1000_1"]
	promedios(iMax,c,m,0.955,times,"large_scale",nombres_large_u)
	
	print('=================================================================================================================\n\n WEAKLY \n\n=================================================================================================================')
	nombres_large_w = ["knapPI_2_100_1000_1","knapPI_2_200_1000_1","knapPI_2_500_1000_1","knapPI_2_1000_1000_1","knapPI_2_2000_1000_1","knapPI_2_5000_1000_1","knapPI_2_10000_1000_1"]
	#nombres_large_w = ["knapPI_2_"+s+"_1000_1"]
	promedios(iMax,c,m,0.955,times,"large_scale",nombres_large_w)
	
	print('=================================================================================================================\n\n STRONGLY \n\n=================================================================================================================')
	nombres_large_s = ["knapPI_3_100_1000_1","knapPI_3_200_1000_1","knapPI_3_500_1000_1","knapPI_3_1000_1000_1","knapPI_3_2000_1000_1","knapPI_3_5000_1000_1","knapPI_3_10000_1000_1"]
	#nombres_large_s = ["knapPI_3_"+s+"_1000_1"]
	promedios(iMax,c,m,0.999,times,"large_scale",nombres_large_s)


#correr(40,0.85,0.001,10)
test(40,0.85,0.001,1)


