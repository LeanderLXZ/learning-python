try:
    varible = 10
    print (varible + "hello")
    print (varible / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print ("Error occurred")
finally:
    print ("This code will run no matter what")


# Raising Exceptions
# num = input(":")
# if float(num) < 0:
#     raise ValueError("Negative!")