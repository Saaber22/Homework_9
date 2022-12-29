import home9_1

def test_pow_1_2():
    assert home9_1.pow(1, 2) == 1

def test_pow_2_2():
    assert home9_1.pow(2, 2) == 4

def test_pow_0_0():
    assert home9_1.pow(0, 0) == 1

def test_pow_9_0_dot_5():
    assert home9_1.pow(9, 0.5) == 3.0

def test_pow_25_minus_2():
    assert home9_1.pow(25, -2) == 0.0016

def test_add_3_5():
    assert home9_1.add(3, 5) == 8

def test_add_minus_10_0_dot_5():
    assert home9_1.add(-10, 0.5) == -9.5

def test_sub_10_5():
    assert home9_1.sub(10, 5) == 5

def test_sub_0_dot_4_minus_23():
    assert home9_1.sub(0.4, -23) == 23.4

def test_mul_5_0():
    assert home9_1.mul(5, 0) == 0

def test_mul_minus_10_minus_2_dot_5():
    assert home9_1.mul(-10, -2.5) == 25.0    

def test_div_7_2():
    assert home9_1.div(7, 2) == 3.5        

def test_div_minus_8_0_dot_5():
    assert home9_1.div(-8, 0.5) == -16.0 

def test_deln_10_3():
    assert home9_1.deln(10, 3) == 3

def test_dela_10_3():
    assert home9_1.dela(10, 3) == 1    