from tkinter import *
import math

SIZE = 600

def createRect(img, a, b, color):
    for y in range(min(a[1], b[1]), max(a[1], b[1])):
        for x in range(min(a[0], b[0]), max(a[0], b[0])):
            img.put(color, (x, y))

def createFrame(img, a, b, thickness, color1, color2):
    createRect(img, a, b, color1)
    #Moves coordinates toward each other in order to then create a smaller rectangle
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
    createRect(img, c, d, color2)

def createCirc(img, a, radius, color):
    for y in range(SIZE):
        for x in range(SIZE):
            if math.sqrt((a[0]-x)**2 + (a[1]-y)**2) <= radius:
                img.put(color, (x, y))

#Uses three coordinates written as lists and calculates the area of a triangle bound by the coordinates
def area(a, b, c):
    area = abs((a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1]))/2)
    return area

def createTri(img, a, b, c, color):
    totalArea = area(a, b, c)
    for y in range(SIZE):
        for x in range(SIZE):
            currentCoord = [x, y]
            sumOfTriangles = area(a, b, currentCoord) + area(a, c, currentCoord) + area(b, c, currentCoord)
            if sumOfTriangles == totalArea:
                img.put(color, (x, y))

#Build a house
def image(img):
    createRect(img, [240, 160], [60, 260], "pink")
    createFrame(img, [120, 220], [100, 260], 1, "black", "red")
    createRect(img, [180, 130], [200, 95], "grey")
    createTri(img, [40, 160], [260,160], [150, 100], "brown")
    createCirc(img, [115, 240], 3, "black")
    createFrame(img, [150, 230], [210, 195], 1, "black", "#add8e6")

def main():
    window = Tk()  # Creates a blank window
    canvas = Canvas(window, width=SIZE, height=SIZE,
                    bg="#ffffff")  # Creats a canvas of defined size with background color white
    canvas.pack()  # Places the canvas in the window
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    image(img)
    mainloop()

if __name__ == '__main__':
    main()