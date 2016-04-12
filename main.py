import parameters as params
from functions import *

def runSierpinski():
    XArr, YArr = ifsAlgorithm(params.indexSierpinski, params.mSierpinski, params.order, params.probSierpinski)
    xMin = np.min(XArr)
    yMin = np.min(YArr)
    xMax = np.max(XArr)
    yMax = np.max(YArr)
    gratingx, gratingy = makeGrating(xMin, xMax, yMin, yMax, params.numDivisions)
    plotFractal(XArr, YArr, "SierpinskiTriangle.png", xMin, xMax, yMin, yMax, gratingx, gratingy)

def runFern():
    XArr, YArr = ifsAlgorithm(params.indexFern, params.mFern, params.order, params.probFern)
    xMin = np.min(XArr)
    yMin = np.min(YArr)
    xMax = np.max(XArr)
    yMax = np.max(YArr)
    gratingx, gratingy = makeGrating(xMin, xMax, yMin, yMax, params.numDivisions)
    plotFractal(XArr, YArr, "BarnsleyFern.png", xMin, xMax, yMin, yMax, gratingx, gratingy)

def runDragon():
    XArr, YArr = ifsAlgorithm(params.indexDragon, params.mDragon, params.order, params.probDragon)
    xMin = np.min(XArr)
    yMin = np.min(YArr)
    xMax = np.max(XArr)
    yMax = np.max(YArr)
    gratingx, gratingy = makeGrating(xMin, xMax, yMin, yMax, params.numDivisions)
    plotFractal(XArr, YArr, "DragonCurve.png", xMin, xMax, yMin, yMax, gratingx, gratingy)
    
def runCcurve():
    XArr, YArr = ifsAlgorithm(params.indexCcurve, params.mCcurve, params.order, params.probCcurve)
    xMin = np.min(XArr)
    yMin = np.min(YArr)
    xMax = np.max(XArr)
    yMax = np.max(YArr)
    gratingx, gratingy = makeGrating(xMin, xMax, yMin, yMax, params.numDivisions)
    plotFractal(XArr, YArr, "Ccurve.png", xMin, xMax, yMin, yMax, gratingx, gratingy)

#runSierpinski()    
#runFern()
#runDragon()
runCcurve()