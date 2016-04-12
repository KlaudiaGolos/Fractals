import numpy as np

order = 200000
numDivisions = 7 #for grating on the plot

#Sierpinski triangle
vec1Sierpinski = [0.5, 0.0, 0.0, 0.5, 0.0, 0.0]
vec2Sierpinski = [0.5, 0.0, 0.0, 0.5, 0.5, 0.0]
vec3Sierpinski = [0.5, 0.0, 0.0, 0.5, 0.25, np.sqrt(3.)/4]
indexSierpinski = [0, 1, 2]
mSierpinski = [vec1Sierpinski, vec2Sierpinski, vec3Sierpinski]
probSierpinski = [1./3, 1./3, 1./3]

#Barnsley Fern
vec1Fern = [ 0.85, 0.04, -0.04, 0.85, 0.0, 1.6]  
vec2Fern = [ 0.2, -0.26, 0.23, 0.22, 0.0, 1.6]  
vec3Fern = [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44] 
vec4Fern = [ 0.0, 0.0, 0.0, 0.16, 0.0, 0.0]  
mFern = [vec1Fern, vec2Fern, vec3Fern, vec4Fern]
indexFern = [0, 1, 2, 3]
probFern = [0.73, 0.13, 0.11, 0.03]

#Dragon curve
vec1Dragon = [0.824074, 0.281482, -0.212346,  0.864198, -1.882290, -0.110607]
vec2Dragon = [0.088272, 0.520988, -0.463889, -0.377778,  0.785360, 8.095795] 
mDragon = [vec1Dragon, vec2Dragon]
indexDragon = [0,1]
probDragon = [0.787473, 0.212527]

#C-curve
vec1Ccurve = [0.5, -0.5, 0.5, 0.5, 0.0, 0.0]
vec2Ccurve = [0.5, 0.5, -0.5, 0.5, 0.5, 0.5]
mCcurve = [vec1Ccurve, vec2Ccurve]
indexCcurve = [0, 1]
probCcurve = [0.5, 0.5]