import pygame
import math
import random
pygame.init()

pygame.mixer.music.load('song2.mp3')
pygame.mixer.music.play(-1)

SIZE = 400

win = pygame.display.set_mode((SIZE,SIZE))
pygame.display.set_caption("Simulator")

bg = (255,255,255)

clock = pygame.time.Clock()

x = 50
y = 415
radius = 3
angle = 0
vel = 5
vision = 20
n = 1000

cells = []
for i in range (0,n):
    cells.append([50, 415, 0, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))])
#[50, 415, 0, (0,255,0)],[50, 415, 0, (0,0,255)]

def redrawGameWindow():
    #pygame.draw.rect(win, bg, (0,0, SIZE, SIZE))
    for cell in cells:
        pygame.draw.circle(win, cell[3], (cell[0],cell[1]), radius)
    pygame.display.update()

pygame.draw.rect(win, bg, (0,0, SIZE, SIZE))

def main():
    run = True
    while run:
        for i in range (0, 15):
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
            for cell in cells:
                if cell[0] < vision:
                    cell[0] = vision
                    cell[2] += math.pi
                elif cell[0] > SIZE - vision:
                    cell[0] = SIZE - vision
                    cell[2] += math.pi
                elif cell[1] < vision:
                    cell[1] = vision
                    cell[2] += math.pi
                elif cell[1] > SIZE - vision:
                    cell[1] = SIZE - vision
                    cell[2] += math.pi

                cell[2] += random.randrange(-22,22) * 0.0174532925
                cell[0] += int(math.cos(cell[2])*vel)
                cell[1] += int(math.sin(cell[2])*vel)

                if cell[0] < 0:
                    cell[0] = 0
                elif cell[0] > SIZE:
                    cell[0] = SIZE
                if cell[1] < 0:
                    cell[1] = 0
                elif cell[1] > SIZE:
                    cell[1] = SIZE

            redrawGameWindow()

    pygame.quit()

main()