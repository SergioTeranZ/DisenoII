import sys

def printTitle(title,main = False):

	if '-e' in sys.argv or main:
		print('==================================================================================\n'+title+' \n==================================================================================')
	else:
		print('\t==================================================================================\n\t'+title+' \n\t==================================================================================')

def truncate(n,m):
	s = '{}'.format(n)
	if 'e' in s or 'E' in s:
		return '{0:.{1}f}'.format(n,m)
	i,p,d = s.partition('.')
	return '.'.join([i, (d+'0'*m)[:m]])

def printResultado(file,style,mode,times,scale,limits,opt=0,sga=1,err=2,ite=3,tim=4,resultados = []):
	name = file[:8]
	size = file.split('_')[2]
	if file[0] == "f":
		name = file.split('_')[0]
		size = file.split('-')[1].split("_")[2]

	if mode == "file":
		print('Escribiendo en archivo...')
		writeFile(times,scale,limits,name+"\t"+size+"\t"+str(opt)+"\t"+str(sga)+"\t"+str(err)+"\t"+str(ite)+"\t"+str(tim))
	else:
		if style == 't':
			print("\t==============================================================================")
			print("\tProblema: "+name+" - t = "+size)
			print("\t==============================================================================")
			print("\t||\t Optimo \t|\t Resultado \t|\t Error \t|\t Iteracion \t|\t Tiempo \t||")
			print("\t------------------------------------------------------------------------------")
			print("\t||\t"+str(opt)+"\t\t|\t"+str(sga)+"\t\t|\t"+str(err)+"%\t|\t"+str(ite)+"\t\t|\t"+str(tim)+"\t\t||")
		
		elif style == 'e':
			print(name+"\t"+size+"\t"+str(opt)+"\t"+str(sga)+"\t"+str(err)+"\t"+str(ite)+"\t"+str(tim))
		elif style == 'd':
			print('\t\t\tResultados:\t'+str([truncate(i,3) for i in [ resultados[i][1] for i in range(len(resultados)) ] ]))
			print('\t\t\tErrores:\t'   +str([truncate(i,3) for i in [ resultados[i][2] for i in range(len(resultados)) ] ]))
			print('\t\t\tIteracion:\t' +str([truncate(i,3) for i in [ resultados[i][3] for i in range(len(resultados)) ] ]))
			print('\t\t\tTiempos:\t'   +str([truncate(i,3) for i in [ resultados[i][4] for i in range(len(resultados)) ] ]))
		else:
			print("Problema: " +name)
			print("Tamaño: "   +size)
			print("Optimo: "   +str(opt))
			print("Resultado: "+str(sga))
			print("Error: "    +str(err))
			print("Iteracion: "+str(ite))
			print("Tiempo: "   +str(tim))
			print("----------------------")

def setParameters(sys):
	gen = 25
	rep = 0.85
	mut = 0.01
	times = 12

	for a in sys.argv:
		if a[0] in ['1','2','3','4','5','6','7','8','9','0'] and not sys.argv[sys.argv.index(a)-1] == '--test':
			times = int(a)
		
		if a[0] == 'm':
			mut = float(a.split('=')[1])
		if a[0] == 'g':
			gen = float(a.split('=')[1])
		if a[0] == 'r':
			rep = float(a.split('=')[1])
	return gen,rep,mut,times

def openFile(scale,nombre):
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
	return capacidad,l,optimo

def writeFile(times,scale,limits,arg):
	nombre = "AGS_"+str(scale)+"("+limits+")"+"_t"+str(times)+".txt" if limits != "" else "SS_"+str(scale)+"_t"+str(times)+".txt"
	ruta = "Resultados/"+nombre
	file = open(ruta,"a+") 
	
	file.write(arg+'\n')
	file.close()