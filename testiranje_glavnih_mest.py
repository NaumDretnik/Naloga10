from igra_glavnih_mest import preveri

def test_glavnih_mest_1():
    assert preveri("Slovenia", "Ljubljana", {"Slovenia": "Ljubljana"}) == True
    return "Test_1 was successful."

def test_glavnih_mest_2():
    assert preveri("Austria", "Vienna", {"Austria": "Vienna"}) == True
    return "Test_2 was successful."

print test_glavnih_mest_1()
print test_glavnih_mest_2()
