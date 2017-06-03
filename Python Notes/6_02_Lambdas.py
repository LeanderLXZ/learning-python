# Lambda is used when passing a simple function as an argument to another function.
def my_fuc(f, arg):
    return f(arg)

print(my_fuc(lambda x: 2*x*x, 5))

# Lambdas can only do things that require a single expression.
# They usually equivalent to a single line of code.


# Function
def polynomial(x):
    return x**2 + 5*x +4
print(polynomial(-4))

# Lambda
print((lambda x: x**2 + 5*x + 4)(-4))
# (lambda x: x**2 + 5*x + 4) ---- f
# (lambda x: x**2 + 5*x + 4)(-4) ---- f(-4)

double = lambda x: x * 2  # ---- better to define a function with def instead.
print(double(7))
