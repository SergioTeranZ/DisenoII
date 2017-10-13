import random


pb2=[(1, 9), (1, 19), (2, 13), (3, 8), (4, 3), (4, 14), (6, 14), (10, 13), (16, 12)]
pb=[]	
for i in pb2:
	costo=i[0]
	beneficio=i[1]
	pb=pb+[(beneficio/costo,costo,beneficio)]
pb=sorted(pb)

#print pb

capacidad=11
beneficio=0
for i in pb:
	if capacidad-i[1]>0:
		capacidad=capacidad-i[1]
		beneficio=beneficio+i[2]

print pb
print "Capacidad Inicial: "+str(capacidad)
print beneficio