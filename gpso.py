#to be changed
import numpy as np
import math
import numdifftools as nd
import grad
def gpso(initialPosition,swarmSize,maxIter,initialInertia,socialFactor,globalFactor,maxSpeedGBest,maxSpeedNeighbours,learningRate,deltaTime,maximise,objectivefunction,plotGraph,destination,obstacles):
    swarmPositions=np.random.random((swarmSize,len(initialPosition)))+initialPosition
    swarmVelocities=np.zeros((swarmSize,len(initialPosition)))
    swarmValues=objectivefunction(swarmPositions)
    #print swarmValues

    localBestPositions=swarmPositions;
    localBestValues=objectivefunction(swarmPositions)

    gBest=0
    gBestPosition=localBestPositions[gBest:gBest+1,:]
    gBestPositions=np.zeros((maxIter,len(initialPosition)))

    for iter in range(0,maxIter):
        inertia = initialInertia*(1-math.exp(-objectivefunction(gBestPosition)/(10**2)))
        swarmPositions=swarmPositions+swarmVelocities*deltaTime
        swarmValues=objectivefunction(swarmPositions)

        for j in range(1,swarmSize):
            if (swarmValues[j]<localBestValues[j] and maximise==1) or (swarmValues[j]>localBestValues[j] and maximise==0):
                localBestValues[j]=swarmValues[j]
                localBestPositions[j,:]=swarmPositions[j,:]
        
            if (swarmValues[j]<swarmValues[gBest] and maximise==1) or (swarmValues[j]>swarmValues[gBest] and maximise==0):
                gBest=j
                gBestPosition=localBestPositions[j,:]
    
        gBestPositions[iter,:]=(gBestPosition)

	for j in range(1,swarmSize):
	
		swarmVelocities[j,:]=inertia*(np.random.random((1,3))*swarmVelocities[j,:]) +(socialFactor/deltaTime)*(np.random.random((1,3))*(localBestPositions[j,:]- swarmPositions[j,:])) +(globalFactor/deltaTime)*(np.random.random((1,3))*(gBestPosition - swarmPositions[j,:]))+(globalFactor/deltaTime)*(np.random.random((1,3))*(gBestPosition - swarmPositions[j,:])) - learningRate*grad.grad(objectivefunction,swarmPositions[j:j+1,:]) 
		       
        for j in range(1,swarmSize):   
            if (np.linalg.norm(swarmVelocities[j,:])!=0):
                if j==gBest:
                    if np.linalg.norm(swarmVelocities[j,:])**2 >= maxSpeedGBest*maxSpeedGBest and maxSpeedGBest!=0:    
                        swarmVelocities[j,:]/=np.linalg.norm(swarmVelocities[j,:])
                        swarmVelocities[j,:]*=maxSpeedGBest
                else:
                    if np.linalg.norm(swarmVelocities[j,:])**2 >= maxSpeedNeighbours*maxSpeedNeighbours and np.all(maxSpeedNeighbours)!=0:    
                        swarmVelocities[j,:]/=np.linalg.norm(swarmVelocities[j,:])
                        swarmVelocities[j,:]*=maxSpeedNeighbours
    return gBestPositions 
