import matplotlib.pyplot as plt
import numpy as np

def ifsAlgorithm(indeces, m, order, prob):
    mVecRandomIndeces = np.random.choice(indeces, order, p = prob)
    x = 0
    y = 0
    XArr = np.array([])
    YArr = np.array([])
    for index in mVecRandomIndeces:
        mCurrent = m[index]
        xCurrent = x
        yCurrent = y
        x = mCurrent[0] * xCurrent + mCurrent[1] * yCurrent + mCurrent[4]
        XArr = np.append(XArr,x)
        y = mCurrent[2] * xCurrent + mCurrent[3] * yCurrent + mCurrent[5]
        YArr = np.append(YArr, y)
    return XArr, YArr
    
def makeGrating(xMin, xMax, yMin, yMax, numDivisions): 
    eps = 0.001 * xMax
    linesList = np.arange(1, numDivisions + 1, 1)
    for r in linesList:
        gratingx = np.linspace(xMin - eps, xMax + eps, r + 1)
        gratingy = np.linspace(yMin - eps, yMax + eps, r + 1)  
    return gratingx, gratingy
    
def plotFractal(XArr, YArr, fileName, xMin, xMax, yMin, yMax, gratingx, gratingy):
    plt.ioff()
    plt.hlines(gratingy, xMin, xMax)
    plt.vlines(gratingx, yMin, yMax)
    plt.scatter(XArr,YArr, s=0.2, c='b', lw=0, marker='o')
    plt.savefig(fileName)
    plt.close()