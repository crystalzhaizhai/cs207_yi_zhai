import L2

def test_L2_result():
    assert L2.vector_len([1,1,1,1,1],[1,2,3,4,5])==7.416198487095663

def test_L2_no_weight():
    assert L2.vector_len([1,1,1,1,1])==2.2360679774997898
def test_L2_dimensions():
    try: 
        L2.vector_len([1,1,1,1,1,1],[1,2,3])
    except ValueError as err:
        assert(type(err)==ValueError)
    