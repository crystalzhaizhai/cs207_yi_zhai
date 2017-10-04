import numpy as np
import copy
def progress1_rate(x,v,vv,k):
    """Returns progress rate of chemical reactoins
    
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
    >>> progress1_rate(np.array([[1.0],[2.0],[1]]),np.array([[1,2],[2,0],[0,2]]),np.array([[0,0],[0,1],[2,1]]),[10,10])
    [40.0, 10.0]
    """
    if (any([kk<0 for kk in k])):
        raise ValueError("k<0")
    flag=True
    for j in range(v.shape[1]):
        if all([v[i][j]<=0 for i in range(v.shape[0])]):
            flag=False
            break 
    if (flag==False):
        raise ValueError("no reactants")
    flag=True
    for j in range(vv.shape[1]):
        if all([vv[i][j]<=0 for i in range(vv.shape[0])]):
            flag=False
            break 
    if (flag==False):
        raise ValueError("no products")
    if x.shape[0]!=v.shape[0] or v.shape!=vv.shape or v.shape[1]!=len(k):
        raise ValueError("dimensions not match")
    tmp=np.array([x[i][0]**v[i][j] for i in range(v.shape[0]) for j in range(v.shape[1])]).reshape(v.shape)
    w=copy.copy(k)
    for i in range(len(x)):
        for j in range(v.shape[1]):
            a=tmp[i][j]
            w[j]*=a
            
    return (w)
