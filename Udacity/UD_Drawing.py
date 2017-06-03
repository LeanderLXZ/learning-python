import turtle


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("#33ff99")

    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("#ffffff")
    brad.speed(10)

    for i in range(30):
        for j in range(4):
            brad.forward(100)
            if j % 2 == 0:
                brad.right(60)
            else:
              brad.right(120)
            j += 1
        brad.right(12)
        i += 1

    brad.right(90)
    brad.forward(300)


    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("#3399ff")
    # angie.speed(2)
    #
    # angie.circle(100)
    #
    # vix = turtle.Turtle()
    # vix.shape("turtle")
    # vix.color("#00cc66")
    # vix.speed(2)
    #
    # vix.left(60)
    # for t in range(3):
    #     vix.forward(150)
    #     vix.left(120)

    turtle.done()

draw_flower()