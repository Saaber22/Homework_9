import home9_2 

def test_funсfibo_1():
    assert home9_2.func_fibo(1) == 1

def test_funсfibo_2():
    assert home9_2.func_fibo(2) == 1

"""
Делаем вывод, что при задание числа ряда 1 или 2, вывод будет всегда 1
Добавим условие в функцию
"""

def test_funсfibo_8():
    assert home9_2.func_fibo(8) == 21

def test_funсfibo_10():
    assert home9_2.func_fibo(10) == 55