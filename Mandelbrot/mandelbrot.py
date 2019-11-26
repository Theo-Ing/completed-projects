from tkinter import *

def mandel(z0, limit):
    z = z0
    for i in range(limit):
        if abs(z) > 2.0: return i
        z = z**2 + z0
    return limit

def color(n):
    r = 1
    g = 7
    b = 1
    if 255 - n*r < 0: red = "00"
    else: red = hex(255 - n*r)[2:]
    if len(red) == 1: red = "0" + red

    if 255 - n*g < 0 : green = "00"
    else: green = hex(255 - n*g)[2:]
    if len(green) == 1: green = "0" + green

    if 255 - n*b < 0 : blue = "00"
    else: blue = hex(255 - n*b)[2:]
    if len(blue) == 1: blue = "0" + blue

    return ("#" + red + green + blue)

n = 512
xc = -0.5
yc = 0
size = 2

window = Tk()  # Creates a blank window
canvas = Canvas(window, width=n, height=n, bg="white")  # Creats a canvas of defined size with background color white
canvas.pack()  # Places the canvas in the window
img = PhotoImage(width=n, height=n)
canvas.create_image((n / 2, n / 2), image=img, state="normal")

for col in range(n):
    for row in range(n):
        x0 = xc - size/2 + size*col/n
        y0 = yc - size/2 + size*row/n
        z0 = complex(x0, y0)
        gray = mandel(z0, 255)
        paint = color(gray)
        img.put(paint, (col, n-1-row))


mainloop()
