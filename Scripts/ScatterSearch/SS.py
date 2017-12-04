import random
import math
from time import time
import sys
from SSMethods import *
from RefSet import RefSet
from Solution import Solution
from helpMethods import *

def SS(cap,items,optimo):
	tiempoI = time() 

	# Step 1:
	# Start with P = empty. 
	# Use the Diversification Generation Method to construct a solution x. 
	# If not x  in P then add x to P (P = P union x), otherwise, discard x.
	# Repeat this step until |P| = PSize. 
	# Build RefSet = {x¹,...,x^b} with b diverse solutions in P.
	b = len(items) if len(items) < 20  else 20
	PSize = 10*b if 10*b < pow(2,b) else (pow(2,b))
	P = Generate(cap,items,b,PSize)
	Improvement(P,items,cap)
	
	refSet = RefSet(cap,items,b,P)

	# Step 2:
	# Evaluate the solution in RefSet 
	# and order them according to their objective function such that
	# x¹ is the best solution and x^b the worst. 
	# Make NewSolutions = TRUE.
	ReferenceSetUpdate(refSet)
	NewSolutions = True
	# While (NewSolutions) do
	while(NewSolutions):
	# 	Step 3:
	# 	Generate NewSubSets, wich consist of all pairs of solutions in RefSet that
	# 	include at least one new solution. 
	# 	Make NewSolutions=FALSE.
		NewSubSets = SubSetGeneration(refSet)
		NewSolutions = False
	# 	While (not NewSubSets = empty ) do
		while NewSubSets:
	# 		Step 4:
	# 		Select the next subset s in NewSubSets.
			s = NewSubSets.pop(0)
	# 		Step 5:
	#		Apply the Solution Combination Method to s to obtain one or more new solutions x.
			newSols = SolutionCombination(s,cap,items,b)
			Improvement(newSols,items,cap)
			for s in newSols:
	#	 		if (x is not in RefSet and f(x) < f(x^b)) then
				if (not refSet.content(s)) and (s.beneficio < refSet.solSet[-1].beneficio):
	#				Step 6:
	#				Make x^b = x and reorder RefSet
					refSet.solSet[-1] = s
					ReferenceSetUpdate(refSet)
	# 				Step 7:
	# 				Make NewSolutions = TRUE
					NewSolutions = True
	# 			end if
	# 	end while
	# end while
	tiempoF = time() 
	tiempoT = tiempoF - tiempoI
	[best,error] = refSet.getBest(int(optimo))
	return [best,tiempoT,error]

def Generate(cap,items,b,PSize):
	PSet = []
	P = []
	seed  = [1]*len(items)
	seedC = [0]*len(items)

	hMax = int(len(seed)/5) if len(seed)/5 > 4 else len(seed)
	
	[P,PSet] = addSol(seed,P,PSet,items,cap)
	[P,PSet] = addSol(seedC,P,PSet,items,cap)

	count = 0
	maxTimes = b
	while len(P) < PSize:
		prev = PSize-len(P)
		for h in range(2,hMax):
			for q in range(0,h):
				info = DiversificationGeneration(seed,h,q)
				for i in info:
					if   count >= maxTimes and PSize > len(P):
						[P,PSet] = addSol(i,P,PSet,items,cap,True)
						count = 0
					
					elif count < maxTimes and PSize > len(P):
						[P,PSet] = addSol(i,P,PSet,items,cap)
						count += 1 if prev == PSize-len(P) else 0

		seed = P[-1]

	return PSet

def addSol(info,P,PSet,items,cap,force = False):
	x = Solution(info,0,items,cap)
	if (not x.info in P) or force:
		P.append(x.info)
		PSet.append(x)
	return P,PSet

def CorrerSS(scale,nombre):
	[C,V,opt] = openFile(scale,nombre)
	[ss,t,e] = SS(C,V,opt)
	return int(opt),ss.beneficio,e,t

def promedios(times,scale,nombres,mode,limits = ""):

	style = 't' if '-t' in sys.argv else 'e' if '-e' in sys.argv else 'n'
	for f in nombres:
		resultados = []
		for _ in range(times):
			resultados.append(CorrerSS(scale,f))

		promedios = [ sum([ resultados[i][j] for i in range(len(resultados)) ])/len(resultados) for j in range(4) ]
		printResultado(f,style,mode,times,scale,limits,opt=int(promedios[0]),ss=truncate(promedios[1],2),err=truncate(promedios[2]*100,3),tim=truncate(promedios[3],4))
		
		if '-d' in sys.argv:
			printResultado(f,'d',mode,times,scale,limits,resultados= resultados)

def runLow(times):
	mode = "screen"
	if '-f' in sys.argv:
		mode = 'file'

	nombres_low = ["f4_l-d_kp_4_11","f3_l-d_kp_4_20","f9_l-d_kp_5_80","f7_l-d_kp_7_50","f6_l-d_kp_10_60","f1_l-d_kp_10_269","f2_l-d_kp_20_878","f10_l-d_kp_20_879","f8_l-d_kp_23_10000"]
	promedios(times,"low-dimensional",nombres_low,mode)

def runLarge(times,setProblems):	
	nombres = [ ["knapPI_"+str(i+1)+"_"+ str(j) +"_1000_1" for j in setProblems] for i in range(3)]

	mode = "screen"
	limits = ""
	if '-f' in sys.argv:
		limits = str(setProblems[0])+'-'+str(setProblems[-1])
		mode = 'file'

	if mode == "screen":
		printTitle('UNCORRELATED')
	promedios(times,"large_scale",nombres[0],mode,limits)
	
	if mode == "screen":
		printTitle('WEAKLY')
	promedios(times,"large_scale",nombres[1],mode,limits)
	
	if mode == "screen":
		printTitle('STRONGLY')
	promedios(times,"large_scale",nombres[2],mode,limits)

def _main():
	times = setParameters(sys)
	tl    = 0
	tL    = 0
	Set   = []
	scale = []

	if '--low' in sys.argv:
		tl    += 1
		scale += ['LOW']
	
	if '--500' in sys.argv:
		tL    += 1
		nSet   = [100,200,500]
		Set   += [nSet]
		scale += [str(nSet[0])+' - '+ str(nSet[-1])]
	
	if '--1000' in sys.argv:
		tL    += 1
		nSet   = [1000,2000,5000,10000]
		Set   += [nSet]
		scale += [str(nSet[0])+' - '+ str(nSet[-1])]
	
	if '--test' in sys.argv:
		tL  += 1
		nSet += [int(sys.argv[sys.argv.index('--test')+1])]
		Set += [nSet]
		scale += [str(nSet[0])+'(test)']

	for i in range(tl):
		if not '-f' in sys.argv:
			printTitle(scale[i] +'('+str(times)+')')
		runLow(times)
		

	for j in range(tL):
		times = int(times/2) if Set[j][0] == 100 else int(times/4) if Set[j][0] == 1000 else times
		if not '-f' in sys.argv:
			printTitle( scale[j+tl] +'('+str(times)+')')
		runLarge(times,Set[j])

_main()