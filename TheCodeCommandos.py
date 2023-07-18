#!/usr/bin/env python
#Trial this
import numpy as np

nInst=50
currentPos = np.zeros(nInst)
def getMyPosition (prcSoFar):
    global currentPos
    (nins,nt) = prcSoFar.shape
    if (nt < 2):
        return np.zeros(nins)
    lastRet = np.log(prcSoFar[:,-1] / prcSoFar[:,-2])
    rpos = np.array([int(x) for x in 2000 * lastRet / prcSoFar[:,-1]])
    currentPos = np.array(map(int, currentPos+rpos))
    return currentPos