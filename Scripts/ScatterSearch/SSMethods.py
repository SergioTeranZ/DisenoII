import random
from RefSet import RefSet
from Solution import Solution

# Method 1:
# 	Diversification Generation Method 
# 	to generate a collection of diverse trial solutions, using one or more arbitrary trial 
#	solutions (or seed solutions) as an input.
def DiversificationGeneration(seed,h,q):
	n = len(seed)
	sol_1 = list(seed)
	sol_2 = list(seed)
	hlist = []
	for k in range(int((n-q)/h)):
		#print('\t\tK ES '+str(k))
		x_p = 1 - seed[q+k*h]
		sol_1[q+k*h] = x_p
	
	for i in range(n):
		sol_2[i] = 0 if sol_1[i] else 1

	hlist.append(sol_1)
	hlist.append(sol_2)

	
	return hlist

# Method 2:
# 	Improvement Method
# 	to transform a trial solution into one or more enhanced trial solutions. 
#	(Neither the input nor the output solutions are required to be feasible, thought the output 
#	solutions are typically feasible. If the input trial solution is not improved as a result 
#	of the apṕlication of this method, the "enhanced" solution is considered to be the same as 
#	the input solution.)
def Improvement(xArray,items,cap):
	for x in xArray:
		# Feasiblity Phase
		while not x.aporte:
			x.feasible(items,cap)
			x.diagnosticar(cap)
		# Improvement Phase
		x.improve(items,cap)

# Method 3:
# 	Reference Set Update Method
# 	to build and maintain a reference set consisting of the b "best" solutions found 
#	(where the value of b is typically small, e.g., no more than 20), organixed to provide 
#	efficient accessing by other parts of the solution procedure. Several alternative criteria 
#	may be used to add solutions to the reference set and delete solutions from the reference set.
def ReferenceSetUpdate(refSet):
	refSet.order()

# Method 4:
# 	SubSet Generation Method
# 	to operate on the reference set, to produce a subset of its solutions as a basis for 
#	creating combined solutions, The most common subset generation method is to generate all 
#	pairs of reference solutions (i.e., all subset of size 2).
def SubSetGeneration(refSet):
	return refSet.newSubSet()

# Method 5:
# 	Solution Combination Method
# 	to tranform a given subset of solutions produced by te Subset Generation Method into one or 
#	more combined solutions.
def SolutionCombination(subset,cap,items,b):
	newSols = []
	info = []
	j = subset[0]
	k = subset[1]
	r = random.random()
	for i in range(len(j.info)):
		si = score(i,j,k)
		info.append(1 if r <= si else 0)
	x = Solution(info,0,items,cap)
	newSols.append(x)
	return newSols

def score(i,j,k):
	a = (j.beneficio*j.info[i]) + (k.beneficio*k.info[i])
	b = j.beneficio + k.beneficio
	return a/b
