import numpy as np
import math
import numdifftools as nd
import gpso
import grad
import gradientdecent
from rdp import rdp
swarmSize=64                       # number of the swarm particles
maxIter=100                        # maximum number of iterations
deltaTime=0.01
inertia=1.61803398875
initialInertia=1.61803398865
socialFactor=1.61803398875*(deltaTime/0.01)
globalFactor=1.61803398875*(deltaTime/0.01)
learningRate=1.61803398875
maximise=1
path=[]
def sda(init,des,obstacles):
	destination=np.array(des)
	initialPosition = np.array(init)
	obstacles=np.array(obstacles)

	def objectivefunction(x):
		try:
			y = np.linalg.norm(x-destination, axis=1)
			for obstacle in obstacles:
				y+=40000/(1+((np.linalg.norm(x-obstacle[0:3],axis =1)**2)/(obstacle[2]**2))**10)
			return y

		except:
			y = np.linalg.norm(x-destination)
			for obstacle in obstacles:
				y+=40000/(1+((np.linalg.norm(x-obstacle[0:3])**2)/(obstacle[2]**2))**10)
			return y
	adi=gpso.gpso(initialPosition,swarmSize,maxIter,inertia,socialFactor,globalFactor,1.5*1800*(0.01/deltaTime),1.5*3600*(0.01/deltaTime),learningRate,deltaTime,1,objectivefunction,1,destination,obstacles)

	return np.asarray(adi)
	
	#print np.asarray(objectivefunction(adi))
#adi1=np.array(adi).tolist()
#adi2=rdp(adi1,epsilon=200)
#print adi2
#adi1=np.array(sda([6014700.0, -211277.0],[6014550.0, -211763.0],[[50,111.111111111111111111,30],[90,200,50],[120,340,40]])).tolist()
#adi2=rdp(adi1,epsilon=5)
#print adi2
waypoints=[]
obstacles=[]
for line in open("output1.txt"):
	line = line.strip()
	parts = line.split(" ")
	waypoints.append([float(parts[0]),float(parts[1]),float(parts[2])])
for line in open("obstacle_localcartesian.txt"):
	line = line.strip()
	parts = line.split(" ")
	obstacles.append([float(parts[0]),float(parts[1]),float(parts[2])])
for i in range(0,len(waypoints)-1):
	a=rdp(np.array(sda(waypoints[i],waypoints[i+1],obstacles)).tolist(),epsilon=50)
	for i in range(0,len(a)):
		path.append(a[i])
#print path
f = open("output2.txt","w") #opens file with name of "test.txt"
for i in range(0,len(path)):
	f.write(str(path[i][0]))
	f.write(" ")
	f.write(str(path[i][1]))
	f.write(" ")
	f.write(str(path[i][2]))
	f.write("\n")
f.close()	 
