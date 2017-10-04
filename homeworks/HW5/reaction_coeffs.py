from math import exp
def k_constant(k):
    return k
def k_arr(a,e,t):
    r=8.314
    if a<= 0:
        raise ValueError("a<0!")
    if t<= 0:
        raise ValueError("t<0!")

    return (a*exp(-e/(r*t)))
def k_mod_arr(a,e,t,b):
    r=8.314
    if a<= 0:
        raise ValueError("a<0!")
    if t<= 0:
        raise ValueError("t<0!")
    return (a*(t**b)*exp(-e/(r*t)))