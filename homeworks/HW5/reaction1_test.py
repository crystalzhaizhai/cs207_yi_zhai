import reaction1_rate as rr1
import numpy as np
def test_normal1():
    x=np.array([[1.0],[2.0],[1]])
    v_i_prime=np.array([[1,0],[2,0],[0,2]])
    v_i_prime_prime=np.array([[0,1],[0,2],[1,0]])
    k=[10,10]
    assert all(rr1.reaction1_rate(x,v_i_prime,v_i_prime_prime,k)==[[-40],[10],[-80],[20],[40],[-20]])

def test_nagative_k1():
    try:
        x=np.array([[1.0],[2.0],[1]])
        v_i_prime=np.array([[1,2],[2,0],[0,2]])
        v_i_prime_prime=np.array([[0,0],[0,1],[2,1]])
        k=[-10,10]
        rr1.reaction1_rate(x,v_i_prime,v_i_prime_prime,k)
    except ValueError as err:
        assert(type(err)==ValueError)

def test_reactants1():
    try:
        x=np.array([[1.0],[2.0],[1]])
        v_i_prime=np.array([[0,2],[0,0],[0,2]])
        v_i_prime_prime=np.array([[0,0],[0,1],[2,1]])
        k=[10,10]
        rr1.reaction1_rate(x,v_i_prime,v_i_prime_prime,k)
    except ValueError as err:
        assert(True)

def test_products1():
    try:
        x=np.array([[1.0],[2.0],[1]])
        v_i_prime=np.array([[1,2],[2,0],[0,2]])
        v_i_prime_prime=np.array([[0,0],[0,0],[2,0]])
        k=[10,10]
        rr1.reaction1_rate(x,v_i_prime,v_i_prime_prime,k)
    except ValueError as err:
        assert(True)
def test_dimensions1():
    try:
        x=np.array([[1.0],[2.0]])
        v_i_prime=np.array([[1,2],[2,0],[0,2]])
        v_i_prime_prime=np.array([[1,0],[0,1],[2,0]])
        k=[10,10]
        rr1.reaction1_rate(x,v_i_prime,v_i_prime_prime,k)
    except ValueError as err:
        assert(True)