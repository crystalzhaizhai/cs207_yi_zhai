import numpy as np
def vector_len(v, *args):
    """Returns the norm of a vector v
    
    INPUTS
    ======
    v: list of float, vector
    args:list of float, weight vector
        
    RETURNS
    ======
    norm: float
          if the dimension of w and v is not the same, an error is raised
    
    EXAMPLES
       >>L2([1,1,1,1,1],[1,2,3,4,5])
        7.416198487095663
        
    
    """

    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)