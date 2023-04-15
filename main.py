# import colorgram
# colours = colorgram.extract("image.jpg", 84)
# color_list = []
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
# print(color_list)
import turtle
import random
color_list = [(202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72), (145, 178, 148), (91, 73, 75), (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172), (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155), (175, 99, 101), (176, 192, 209), (114, 135, 138), (207, 182, 188), (69, 63, 57), (179, 197, 201)]
tom = turtle.Turtle()
turtle.colormode(255)
tom.penup()
tom.speed(0)
tom.hideturtle()
for steps in range(10):
    position = tom.goto(-300 + 50, -250 + 50* steps)
    for _ in range(10):
        tom.dot(20, random.choice(color_list))
        tom.fd(50)
screen = turtle.Screen()
screen.exitonclick()