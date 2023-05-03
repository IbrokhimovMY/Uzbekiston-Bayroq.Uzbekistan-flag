"""
To'liq kodni GitHub sahifamdan yuklab olishingiz mumkin.E'tiboringiz uchun rahmat :)
 https://GitHub.com/IbrokhimovMY

"""

import turtle
from turtle import *
turtle.bgcolor('white')
turtle.title('Uzbekistan')
my_screen = Screen()
my_screen.setup(1000,600)


uzb = Turtle()
# uzb.speed(5)
def center_mark():
    uzb.pu()
    uzb.left(180)
    uzb.forward(500)


center_mark()
uzb.right(90)
uzb.forward(100)
uzb.right(90)

uzb.pd()
uzb.fillcolor('#3399ff')
uzb.begin_fill()
uzb.forward(1000)
uzb.left(90)
uzb.forward(200)
uzb.left(90)
uzb.forward(1000)
uzb.left(90)
uzb.forward(200)
uzb.end_fill()


uzb1 = Turtle()
uzb1.pu()
uzb1.left(180)
uzb1.forward(500)
uzb1.right(90)
uzb1.forward(95)
uzb1.right(90)


uzb1.pd()
uzb1.fillcolor('#e60000')
uzb1.begin_fill()
uzb1.width(10)
uzb1.color('#e60000')
uzb1.forward(1000)
uzb1.end_fill()



uzb3 = Turtle()
def center_mark():
    uzb3.pu()
    uzb3.left(180)
    uzb3.forward(500)


center_mark()
uzb3.left(90)
uzb3.forward(100)
uzb3.left(90)

uzb3.pd()
uzb3.fillcolor('#66ff33')
uzb3.begin_fill()
uzb3.forward(1000)
uzb3.right(90)
uzb3.forward(200)
uzb3.right(90)
uzb3.forward(1000)
uzb3.right(90)
uzb3.forward(200)
uzb3.end_fill()


uzb2 = Turtle()
uzb2.pu()
uzb2.left(180)
uzb2.forward(500)
uzb2.left(90)
uzb2.forward(100)
uzb2.left(90)

uzb2.pd()
uzb2.fillcolor('#e60000')
uzb2.begin_fill()
uzb2.width(10)
uzb2.color('#e60000')
uzb2.forward(1000)
uzb2.end_fill()



uzb.write(f"\n☾",align='left',font=('White',150,'normal'))
uzb.write(f"""                              ☆ ☆ ☆\n\n\n
""", font=("White",20, "bold"))
uzb.write(f"""\n


                         ☆ ☆ ☆ ☆\n\n
""", font=("White",20, "bold"))
uzb.write(f"""\n



                     ☆ ☆ ☆ ☆ ☆\n
""", font=("white",20, "bold"))

uzb4 = Turtle()
uzb4.pu()
uzb4.begin_fill()
uzb4.write(f"O'zbek o'g'loni: @IbrokhimovMY 😎",align='center',font=("black",30, "bold"))
uzb4.end_fill()
my_screen.exitonclick()

