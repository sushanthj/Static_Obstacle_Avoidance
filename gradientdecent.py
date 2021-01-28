import numpy as np
import math
import numdifftools as nd
def gradientDescent(initialPoint,maxIter,learningRate,objectiveFunction):
      y=initialPoint
      for i in range [1,maxIter]:
          y=y-learningRate*grad(objectiveFunction,y);
          gBestPositions[:,i]=y
       
