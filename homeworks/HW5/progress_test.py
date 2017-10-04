import progress_rate as pr
def test_normal():
    x=[[1.0],[2.0],[3.0]]
    v_i_prime=[[2.0],[1.0],[0.0]]
    v_i_prime_prime=[[0],[0],[1]]
    k=10
    assert pr.progress_rate(x,v_i_prime,v_i_prime_prime,k)==20.0
def test_k_positive():
    try:
        x=[[1.0],[2.0],[3.0]]
        v_i_prime=[[2.0],[1.0],[0.0]]
        v_i_prime_prime=[[0],[0],[1]]
        k=-10
        pr.progress_rate(x,v_i_prime,v_i_prime_prime,k)
    except ValueError as err:
        assert(True)
def test_reactants():
    try:
        x=[[1.0],[2.0],[3.0]]
        v_i_prime=[[0],[0],[0]]
        v_i_prime_prime=[[0],[0],[1]]
        k=10
        pr.progress_rate(x,v_i_prime,v_i_prime_prime,k)
    except ValueError as err:
        assert(type(err)==ValueError)

def test_products():
    try:
        x=[[1.0],[2.0],[3.0]]
        v_i_prime=[[2],[1],[0.0]]
        v_i_prime_prime=[[0],[0],[0]]
        k=10
        pr.progress_rate(x,v_i_prime,v_i_prime_prime,k)
    except ValueError as err:
        assert(type(err)==ValueError)