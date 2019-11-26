from tkinter import *
import math

SIZE = int(input("Canvas size: "))

#Doesn't require user input, this is used in createFrame()
def createRectForFrame(img, a, b, color):
    for y in range(min(a[1], b[1]), max(a[1], b[1])):
        for x in range(min(a[0], b[0]), max(a[0], b[0])):
            img.put(color, (x, y))

def createRect(img):
    a = [int(input("x1 = ")), int(input("y1 = "))]
    b = [int(input("x2 = ")), int(input("y2 = "))]
    color = input("What color should the rectangle be? ")
    for y in range(min(a[1], b[1]), max(a[1], b[1])):
        for x in range(min(a[0], b[0]), max(a[0], b[0])):
            img.put(color, (x, y))

def createFrame(img):
    a = [int(input("x1 = ")), int(input("y1 = "))]
    b = [int(input("x2 = ")), int(input("y2 = "))]
    thickness = int(input("How thick should the frame be? "))
    color1 = input("What color should the frame be? ")
    color2 = input("What color should the inside be? ")

    createRectForFrame(img, a, b, color1)
    if a[0] < b[0] and a[1] < b[1]:
        c = [a[0] + thickness , a[1] + thickness]
        d = [b[0] - thickness , b[1] - thickness]
    elif a[0] > b[0] and a[1] < b[1]:
        c = [a[0] - thickness , a[1] + thickness]
        d = [b[0] + thickness , b[1] - thickness]
    elif a[0] < b[0] and a[1] > b[1]:
        c = [a[0] + thickness , a[1] - thickness]
        d = [b[0] - thickness , b[1] + thickness]
    else:
        c = [a[0] - thickness, a[1] - thickness]
        d = [b[0] + thickness, b[1] + thickness]
    createRectForFrame(img, c, d, color2)

def createCirc(img):
    a = [int(input("Center x = ")), int(input("Center y = "))]
    radius = int(input("Radius = "))
    color = input("What color should the circle be? ")
    for y in range(SIZE):
        for x in range(SIZE):
            if math.sqrt((a[0]-x)**2 + (a[1]-y)**2) <= radius:
                img.put(color, (x, y))

def area(a, b, c):
    area = abs((a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1]))/2)
    return area

def createTri(img):
    a = [int(input("x1 = ")) , int(input("y1 = "))]
    b = [int(input("x2 = ")) , int(input("y2 = "))]
    c = [int(input("x3 = ")) , int(input("y3 = "))]
    color = input("What color should the triangle be? ")
    totalArea = area(a, b, c)
    for y in range(SIZE):
        for x in range(SIZE):
            currentCoord = [x, y]
            sumOfTriangles = area(a, b, currentCoord) + area(a, c, currentCoord) + area(b, c, currentCoord)
            if sumOfTriangles == totalArea:
                img.put(color, (x, y))

def draw():
    mainloop()
    root.mainloop()

def main():
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")

    # Menu
    menu = {}
    menu["Rectangle"] = lambda: createRect(img)
    menu["Frame"] = lambda: createFrame(img)
    menu["Circle"] = lambda: createCirc(img)
    menu["Triangle"] = lambda: createTri(img)
    while True:
        for x in menu.keys(): print(x)
        choice = input("> ")
        menu[choice]()
        window.update_idletasks()
        window.update()

if __name__ == '__main__':
    main()