import turtle

screen = turtle.Screen()
screen.bgcolor("Lightblue")
screen.title("Greeting Card")

cake = turtle.Turtle()
cake.speed(2)

def draw_rectangle(turtle, width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

cake.penup()
cake.goto(-50, -70)
cake.pendown()
draw_rectangle(cake, 100, 50, "pink")

cake.penup()
cake.goto(-40, -30)
cake.pendown()
draw_rectangle(cake, 80, 40, "yellow")

cake.penup()
cake.goto(-30, -0)
cake.pendown()
draw_rectangle(cake, 60, 30, "blue")

candles = turtle.Turtle()
candles.speed(3)

def draw_candle(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    draw_rectangle(turtle, 10, 20, "white")  # menggambar lilin
    turtle.penup()
    turtle.goto(x, y + 15)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x + 5, y + 20)
    turtle.pendown()
    turtle.color("orange")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

for i in range(3):
    draw_candle(candles, -20 + i * 15, 15)

cake.hideturtle()
candles.hideturtle()

text = turtle.Turtle()
text.penup()
text.goto(0, -200)
text.color("red")
text.write("Selamat Ulang Tahun", align="center", font=("Arial", 24, "bold"))
text.goto(0, -250)
text.write("Bundaa", align="center", font=("Arial", 20, "bold"))
text.hideturtle()

turtle.done()

