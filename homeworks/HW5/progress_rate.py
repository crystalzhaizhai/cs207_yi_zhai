
import numpy as np
import copy
def progress_rate(x,v,vv,kk):
    """Returns progression rate of chemical reactoins
    
    INPUTS
    =======
    x: array of float
        concentration of molecule species
    v: array of integers
        Coefficient of molecule species on the left side of equation
    vv: array of integers
        Coefficient of melecule species on the right side of equation
    kk: array of float
        reaction rate coefficient
    
    RETURNS
    ========
    roots: array of floats
    
    EXAMPLES
    =========
    >>> progress_rate([[1.0],[2.0],[3.0]],[[2.0],[1.0],[0.0]],[[0],[0],[1]],10)
    20.0
    """
    if (kk<0):
        raise ValueError("k<0")
    if all([i[0]<=0 for i in v]):
        raise ValueError("no reactants")
    if all([i[0]<=0 for i in vv]):
        raise ValueError("no products")
    tmp=[x[i][0]**v[i][0] for i in range(len(x))]
    w=copy.copy(kk)
    for i in range(len(x)):
        w*=tmp[i]
#     return (np.transpose([np.array([w*(vv[i][0]-v[i][0]) for i in range(len(x))])]))
    return(w)