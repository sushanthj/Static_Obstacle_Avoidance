import numpy as np
import math
import numdifftools as nd
def grad(func,x):
    delx=1e-10
    diff=np.eye(np.size(x))*delx

    return (func(x+diff)-func(x-diff))/(2*delx)
