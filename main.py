print("---------------------------------------------")
print("  Bienvenido usuario a mi programa en Python  ")
print("---------------------------------------------\n")

nombre = input("¿Cuál es tu nombre usuario?: ")
curso = input(f"¿Y de qué curso eres {nombre}?: ")
lenguaje_favorito = input(f"¿{nombre}, cuál es tu lenguaje de programación favorito?: ")

print(f"\nExcelente elección {nombre}, {lenguaje_favorito} es un lenguaje con mucha aura para aprender y crear proyectos.")
print("Con los lenguajes de programación se pueden crear varias cosas; por ejemplo, en Python puedes crear juegos y muchas cosas más.\n")
print(f"{nombre}, si quieres jugar una versión de Flappy Bird escribe [1], si quieres jugar a adivinar un número escribe [2] y si no quieres jugar nada escribe [3].")

opcion = input("Elige una opción: ")

if opcion == "1":
    print("Abriendo Flappy Bird...")
    from random import Random as Random, SystemRandom as SystemRandom, betavariate as betavariate, binomialvariate as binomialvariate, choice as choice, choices as choices, expovariate as expovariate, gammavariate as gammavariate, gauss as gauss, getrandbits as getrandbits, getstate as getstate, lognormvariate as lognormvariate, normalvariate as normalvariate, paretovariate as paretovariate, randbytes as randbytes, randint as randint, random as random, randrange as randrange, sample as sample, seed as seed, setstate as setstate, shuffle as shuffle, triangular as triangular, uniform as uniform, vonmisesvariate as vonmisesvariate, weibullvariate as weibullvariate
    from turtle import Pen as Pen, RawPen as RawPen, RawTurtle as RawTurtle, Screen as Screen, ScrolledCanvas as ScrolledCanvas, Shape as Shape, Terminator as Terminator, Turtle as Turtle, TurtleScreen as TurtleScreen, Vec2D as Vec2D, addshape as addshape, back as back, backward as backward, begin_fill as begin_fill, begin_poly as begin_poly, bgcolor as bgcolor, bgpic as bgpic, bk as bk, bye as bye, circle as circle, clear as clear, clearscreen as clearscreen, clearstamp as clearstamp, clearstamps as clearstamps, clone as clone, color as color, colormode as colormode, degrees as degrees, delay as delay, distance as distance, done as done, dot as dot, down as down, end_fill as end_fill, end_poly as end_poly, exitonclick as exitonclick, fd as fd, fill as fill, fillcolor as fillcolor, filling as filling, forward as forward, get_poly as get_poly, get_shapepoly as get_shapepoly, getcanvas as getcanvas, getpen as getpen, getscreen as getscreen, getshapes as getshapes, getturtle as getturtle, goto as goto, heading as heading, hideturtle as hideturtle, home as home, ht as ht, isdown as isdown, isvisible as isvisible, left as left, listen as listen, lt as lt, mainloop as mainloop, mode as mode, no_animation as no_animation, numinput as numinput, onclick as onclick, ondrag as ondrag, onkey as onkey, onkeypress as onkeypress, onkeyrelease as onkeyrelease, onrelease as onrelease, onscreenclick as onscreenclick, ontimer as ontimer, pd as pd, pen as pen, pencolor as pencolor, pendown as pendown, pensize as pensize, penup as penup, poly as poly, pos as pos, position as position, pu as pu, radians as radians, register_shape as register_shape, reset as reset, resetscreen as resetscreen, resizemode as resizemode, right as right, rt as rt, save as save, screensize as screensize, seth as seth, setheading as setheading, setpos as setpos, setposition as setposition, setundobuffer as setundobuffer, setup as setup, setworldcoordinates as setworldcoordinates, setx as setx, sety as sety, shape as shape, shapesize as shapesize, shapetransform as shapetransform, shearfactor as shearfactor, showturtle as showturtle, speed as speed, st as st, stamp as stamp, teleport as teleport, textinput as textinput, tilt as tilt, tiltangle as tiltangle, title as title, towards as towards, tracer as tracer, turtles as turtles, turtlesize as turtlesize, undo as undo, undobufferentries as undobufferentries, up as up, update as update, width as width, window_height as window_height, window_width as window_width, write as write, write_docstringdict as write_docstringdict, xcor as xcor, ycor as ycor
    import freegames

    bird = freegames.vector(0, 0)
    balls = []

    def tap(x, y):
        up = freegames.vector(0, 30)
        bird.move(up)

    def inside(point):
        return -200 < point.x < 200 and -200 < point.y < 200

    def draw(alive):
        clear()
        goto(bird.x, bird.y)

        if alive:
            dot(10, 'green')
        else:
            dot(10, 'red')

        for ball in balls:
            goto(ball.x, ball.y)
            dot(20, 'black')

        update()

    def move():
        bird.y -= 5

        for ball in balls:
            ball.x -= 3

        if randrange(10) == 0:
            y = randrange(-199, 199)
            ball = freegames.vector(199, y)
            balls.append(ball)

        while len(balls) > 0 and not inside(balls[0]):
            balls.pop(0)

        if not inside(bird):
            draw(False)
            return

        for ball in balls:
            if abs(ball - bird) < 15:
                draw(False)
                return

        draw(True)
        ontimer(move, 50)

    setup(420, 420, 370, 0)
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    move()
    done()

elif opcion == "2":
    print("Abriendo el juego de adivinar el número...")
    from random import randint

    inicio = 1
    fin = 100
    valor = randint(inicio, fin)

    print(f"Estoy pensando en un número entre {inicio} y {fin}.")

    intento = None

    while intento != valor:
        texto = input("Adivina el número: ")
        intento = int(texto)

        if intento < valor:
            print("Más alto.")
        elif intento > valor:
            print("Más bajo.")

    print(f"¡Felicidades {nombre}! Adivinaste el número correcto: {valor}")

elif opcion == "3":
    print("Gracias por probar mi código. ¡Adiós!")

else:
    print("Opción no válida. Escribe 1, 2 o 3.")