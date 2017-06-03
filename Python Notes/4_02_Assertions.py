print(1)
assert 2 + 2 == 4
print(2)
# assert 1 + 1 == 3 ---- AssertionError
print(3)

temp = -10
print(temp)
assert (temp >= 0), "Colder than absolute zero!"


def my_func(x):
    assert x > 0, "Error!"
    print(x)