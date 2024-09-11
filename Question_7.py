#imports and shortcuts
import turtle
tk = turtle
tk.shape("turtle")
#body
tk.color("white")
tk.goto(0,0)
tk.begin_fill()
tk.circle(80)
tk.end_fill()
tk.up()

tk.goto(0,160)
tk.begin_fill()
tk.down()
tk.circle(60)
tk.end_fill()
tk.up()

tk.goto(0,-200)
tk.begin_fill()
tk.down()
tk.circle(100)
tk.end_fill()
tk.up()

#buttons
tk.color("black")
tk.goto(0,20)
tk.begin_fill()
tk.circle(10)
tk.end_fill()
tk.up()
tk.goto(0,50)
tk.down()
tk.begin_fill()
tk.circle(10)
tk.end_fill()
tk.up()
tk.goto(0,90)
tk.down()
tk.begin_fill()
tk.circle(10)
tk.end_fill()
tk.up()

#arms
tk.goto(80,75)
tk.left(45)
tk.down()
tk.forward(100)
tk.up()
tk.right(45)

tk.goto(-80,75)
tk.left(135)
tk.down()
tk.forward(100)
tk.up()
tk.right(135)

#eyes
tk.goto(-30,220)
tk.down()
tk.begin_fill()
tk.circle(10)
tk.end_fill()
tk.up()

tk.goto(30,220)
tk.down()
tk.begin_fill()
tk.circle(10)
tk.end_fill()
tk.up()

tk.bgcolor("light blue")

tk.hideturtle()
tk.exitonclick()