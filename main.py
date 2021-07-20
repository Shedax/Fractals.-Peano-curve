import turtle
axiom = "F"
newf = {"F":"F+F-F-F-F+F+F+F-F"}
iterations = 3
alpha = 45
angle = 90

def create_l_system(iters, axiom, newf): #функция создания l-системы
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(newf[i] if i in newf else i for i in start_string)
        start_string = end_string
    return end_string

def draw_l_system(t, instructions, angle, distance):#функция отрисовки
    for liter in instructions:
        if liter == 'F':
            t.forward(distance)
        elif liter == '+':
            t.right(angle)
        elif liter == '-':
            t.left(angle)

def create(iterations, axiom, rules, angle, length=20, size=2, width=800, height=800):#вызов функций
    inst = create_l_system(iterations, axiom, newf)
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)
    t.up()
    t.left(alpha)
    t.down()
    t.speed(10)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    wn.exitonclick()
create(iterations, axiom, newf, angle)

