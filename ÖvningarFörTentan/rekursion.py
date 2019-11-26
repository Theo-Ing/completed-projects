import math
import random
import pygame
from pygame import gfxdraw

pygame.init()
SIZE = 700

def lnFact(n, counter = 0):
    if counter > 0:
        if n < 0:
            print("Value given is less than 0, calculating for absolute value:")
            n -= 1
        if n == 0: return 1
        if n == 1: return 1
        return n * lnFact(n-1, counter + 1)
    return math.log(lnFact(n, counter + 1), math.e)

def ex233(n):
    if n<=0: return
    print(n)
    ex233(n-2)
    ex233(n-3)
    print(n)

def ex234(n):
    if n<=0: return " "
    return ex234(n-3) + str(n) + ex234(n-2) + str(n)

def mystery(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return mystery(a+a, b//2)
    return mystery(a+a, b//2) * a

def t1(n):
    if n != 1 and n % 2 != 0:
        print("n not divisible by 2 fully, returning...")
        return
    if n == 1: return 1
    return t1(n//2) + 1
def t2(n):
    if n != 1 and n % 2 != 0:
        print("n not divisible by 2 fully, returning...")
        return
    if n == 1: return 1
    return 2 * t2(n//2) + 1
def t3(n):
    if n != 1 and n % 2 != 0:
        print("n not divisible by 2 fully, returning...")
        return
    if n == 1: return 1
    return 2 * t3(n//2) + n
def t4(n):
    if n != 1 and n % 2 != 0:
        print("n not divisible by 2 fully, returning...")
        return
    if n == 1: return 1
    return 4 * t4(n//2) + 3

def draw (n, size, x, y):
    if n == 0: return
    x0 = x - size/2.0
    x1 = x + size/2.0
    y0 = y - size/2.0
    y1 = y + size/2.0
    pygame.draw.line(win, (0, 0, 0), (x0, y), (x1, y))
    pygame.draw.line(win, (0, 0, 0), (x0, y0), (x0, y1))
    pygame.draw.line(win, (0, 0, 0), (x1, y0), (x1, y1))
    draw(n - 1, size / 2.0, x0, y0)
    draw(n - 1, size / 2.0, x0, y1)
    draw(n - 1, size / 2.0, x1, y0)
    draw(n - 1, size / 2.0, x1, y1)
def htree(n):
    draw(n, SIZE/2, SIZE/2, SIZE/2)

def sierpinski(n, c1 = [SIZE / 4, SIZE - SIZE / 4], c2 = [SIZE - SIZE / 4, SIZE - SIZE / 4], c3 = [SIZE / 2, SIZE - SIZE / 4 - SIZE * math.sqrt(3) / 4]):
    if n <= 0: return
    x1 = c1[0]
    y1 = c1[1]
    x2 = c2[0]
    y2 = c2[1]
    x3 = c3[0]
    y3 = c3[1]
    c = []
    c.append([(x3 + x1) / 2, (y1 + y3) / 2])
    c.append([(x2 + x1) / 2, (y2 + y1) / 2])
    c.append([(x2 + x3) / 2, (y2 + y3) / 2])
    pygame.draw.line(win, (0, 0, 0), c1, c2)
    pygame.draw.line(win, (0, 0, 0), c1, c3)
    pygame.draw.line(win, (0, 0, 0), c2, c3)
    sierpinski(n - 1, c1, c[1], c[0])
    sierpinski(n - 1, c[1], c2, c[2])
    sierpinski(n - 1, c[0], c[2], c3)

def sierpinskidot(n, x = 0.0, y = 0.0):
    cx = [SIZE/4, SIZE-SIZE/4, SIZE/2]
    cy = [SIZE-SIZE/4, SIZE-SIZE/4, SIZE-SIZE/4-SIZE*math.sqrt(3)/4]
    for i in range(n):
        r = random.randint(0, 2)
        x = (x + cx[r]) / 2
        y = (y + cy[r]) / 2
        gfxdraw.pixel(win, int(x), int(y), (0, 0, 0))
    pygame.display.update()

def fern(n, x = 0.0, y = 0.0):
    for i in range(n):
        r = random.randint(1, 100)
        if r == 1:
            x = 0.5*SIZE
            y = 0.16*y
        elif r <= 86:
            x = 0.85*x + 0.04*y + 0.075*SIZE
            y = -0.04*x + 0.85*y + 0.180*SIZE
        elif r <= 93:
            x = 0.2*x - 0.26*y + 0.4*SIZE
            y = 0.23*x + 0.22*y + 0.045*SIZE
        elif r <= 100:
            x = -0.15*x + 0.28*y + 0.575*SIZE
            y = 0.26*x + 0.24*y + 0.086*SIZE
        gfxdraw.pixel(win, int(x), int(y), (0, 0, 0))
    pygame.display.update()

def squarerek(n, c = [SIZE/2, SIZE/2], width = SIZE/2):
    if n <= 0: return
    c0 = [c[0] - width/2, c[1] + width/2]
    c1 = [c[0] - width/2, c[1] - width/2]
    c2 = [c[0] + width/2, c[1] - width/2]
    c3 = [c[0] + width/2, c[1] + width/2]
    pygame.draw.rect(win, (0, 0, 0), (c1[0], c1[1], width, width))
    squarerek(n - 1, c0, width / 2)
    squarerek(n - 1, c1, width / 2)
    squarerek(n - 1, c2, width / 2)
    squarerek(n - 1, c3, width / 2)

if __name__ == '__main__':
    win = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Rekursion")
    clock = pygame.time.Clock()
    pygame.draw.rect(win, (255,255,255), (0, 0, SIZE, SIZE))

    run = True
    while run:
        for event in pygame.event.get():
            # Closes window if x is pressed
            if event.type == pygame.QUIT:
                run = False
        sierpinski(7, [300, 450], [250, 300], [603, 402])
        #sierpinskidot(100)
        #fern(10000)
        #squarerek(9)
        #htree(5)
        pygame.display.update()

    #print(lnFact(100))
    #ex233(6)
    #print(ex234(6))
    #print(mystery(2, 25))
    #print(t1(8), t2(8), t3(8), t4(8))

    pygame.quit()