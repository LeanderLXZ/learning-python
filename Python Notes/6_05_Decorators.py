# Decorators


# Decorators provide a way to modify functions using other functions.

def decor(func):
    def wrap():
        print("===============")
        func()
        print("===============")
    return wrap


def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

print_text = decor(print_text)
print_text()

@decor
def print_text_1():
    print("spam")

print_text_1()


@decor
@decor
def print_text_2():
    print("eggs")

print_text_2()



