'''
Theo's P-Uppgift
Källor:
Introduction to Programming in Python (Robert Sedgewick, Kevin Wayne, Robert Dondero)
Pygame webpage: https://www.pygame.org/
Pygame Programming Tutorials (Tech With Tim): https://www.youtube.com/playlist?list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
How to Create a Button in Pygame (Tech With Tim): https://www.youtube.com/watch?v=4_9twnEduFA
'''
import pygame
import math
import random

SIZE = 300 #Recommended 200 to 500
RADIUS = 7
NUMBER = 10
SEARCH_ANGLE = math.pi/8
FOOD_PER_DAY = 20
VIS_TO_VEL_RATIO = 10
FPS = 30
DAY_LENGTH = 5 * FPS
MUSIC = True
WHITE = (255,255,255)
BLACK = (0, 0, 0)



class Cell:
    """
    Cell objects represent small creatures that have the following factors:
    self.coord  : List coordinates representing position (coord[0] is the x coordinate and coord[1] is the y coordinate)
    self.vel    : An integer representing movement speed
    self.vis    : An integer representing a radius within their field of view
    self.angle  : A float representing the direction which the cell will move
    self.fed    : An integer representing how many foodBits the cell has consumed
    """

    def __init__(self, vel, vis):
        """
        Initiates cell object
        self.coord  : Randomized to a point on one of the four edges
        self.vel    : Initially set to value defined when calling on constructor (vel)
        self.vis    : Initially set to value defined when calling on constructor (vis)
        self.angle  : Initially set to face away from the edge the cell starts on
        self.fed    : Initially set to 0
        """
        self.vel = vel
        self.vis = vis
        self.fed = 0

        edgeChoice = random.randint(1,4)
        if edgeChoice == 1:
            self.coord = [0, random.randint(0, SIZE)]
            self.angle = 0
        elif edgeChoice == 2:
            self.coord = [SIZE, random.randint(0, SIZE)]
            self.angle = math.pi
        elif edgeChoice == 3:
            self.coord = [random.randint(0, SIZE), 0]
            self.angle = math.pi/2
        elif edgeChoice == 4:
            self.coord = [random.randint(0, SIZE), SIZE]
            self.angle = 3*math.pi/2

    def move(self):
        """Changes self.coord depending on self.angle and self.vel"""
        self.coord[0] += math.cos(self.angle) * self.vel/2
        self.coord[1] += math.sin(self.angle) * self.vel/2

        if self.coord[0] < 0:
            self.coord[0] = 0
        elif self.coord[0] > SIZE:
            self.coord[0] = SIZE
        if self.coord[1] < 0:
            self.coord[1] = 0
        elif self.coord[1] > SIZE:
            self.coord[1] = SIZE

    def checkFood(self, food):
        """Returns True if a coordinate in the list food is within
        a circle around the cell with the radius self.vis, otherwise
        returns False."""
        for foodBit in food:
            distanceToCoord = math.sqrt((foodBit[0] - self.coord[0])**2 + (foodBit[1]- self.coord[1])**2)
            if distanceToCoord < self.vis + RADIUS:
                return True
        return False

    def searchFood(self, food):
        """Returns coordinate in food list closest to self.coord."""
        currentClosestDist = SIZE
        for foodBit in food:
            distanceToCoord = math.sqrt((foodBit[0] - self.coord[0]) ** 2 + (foodBit[1] - self.coord[1]) ** 2)
            if distanceToCoord < currentClosestDist:
                currentClosestCoord = foodBit
                currentClosestDist = distanceToCoord
        return currentClosestCoord

    def angleChange(self, food, time):
        """Changes self.angle depending on time (how long until the end of the day),
        on checkFood and searchFood to point to nearest coordinate in the list food.
        If no coordinate in food is within range and time is not close to 0  self.angle
        will be randomized relative to the current angle."""

        #Go to edge when full or when not hungry and day is nearing its end
        if self.fed >= 2 or (self.fed > 0 and self.vel*(time-6) < SIZE/2):
            if self.coord[0] >= self.coord[1]:
                if self.coord[1] > SIZE - self.coord[0]:
                    self.angle = 0
                else:
                    self.angle = 3*math.pi/2
            else:
                if self.coord[1] > SIZE- self.coord[0]:
                    self.angle = math.pi/2
                else:
                    self.angle = math.pi
        #Search for nearby food and change angle towards it
        elif self.checkFood(food):
            nearestMeal = self.searchFood(food)
            if self.coord[0]-nearestMeal[0] == 0:
                if self.coord[1]-nearestMeal[1] > 0:
                    self.angle = math.pi/2
                else:
                    self.angle = math.pi*3/2
            else:
                if self.coord[0] < nearestMeal[0]:
                    self.angle = math.atan((self.coord[1]-nearestMeal[1])/(self.coord[0]-nearestMeal[0]))
                else:
                    self.angle = math.atan((self.coord[1] - nearestMeal[1]) / (self.coord[0] - nearestMeal[0])) + math.pi
        #Randomly move until food is found
        else:
            self.angle += random.uniform(-1*SEARCH_ANGLE, SEARCH_ANGLE)
            #Roomba instinct: When hitting a wall, turn around
            if self.coord[0] <= 0:
                self.angle = 0
            elif self.coord[0] >= SIZE:
                self.angle = math.pi
            elif self.coord[1] <= 0:
                self.angle = math.pi/2
            elif self.coord[1] >= SIZE:
                self.angle = math.pi * 3 / 2

    def eat(self, food):
        """Checks if any coordinate in the list food is located within the cell using
        self.coord and RADIUS, if so self.fed += 1 and the specific coordinate is removed
        from the food list)"""
        for foodBit in food:
            distanceToCoord = math.sqrt((foodBit[0] - self.coord[0]) ** 2 + (foodBit[1] - self.coord[1]) ** 2)
            if distanceToCoord < RADIUS:
                self.fed += 1
                del food[food.index(foodBit)]

    def clone(self):
        """Creates a new cell object similar to self but with possible slight changes to vis and vel"""
        mutation = random.randint(0, 20)
        mutationLvl = random.randint(1, 3)
        if mutation == 10 and self.vel + mutationLvl <= 30:
            vel = self.vel + mutationLvl
            vis = self.vis - VIS_TO_VEL_RATIO * mutationLvl
        elif mutation == 11 and self.vis + mutationLvl <= 30 * VIS_TO_VEL_RATIO:
            vel = self.vel - mutationLvl
            vis = self.vis + VIS_TO_VEL_RATIO * mutationLvl
        else:
            vel = self.vel
            vis = self.vis
        return Cell(vel, vis)

    def color(self):
        """Returns an RGB tuple representing the selfs color"""
        if self.fed == 0:
            return ((self.vel)*255/30, (self.vis)*255/(30 * VIS_TO_VEL_RATIO), 0)
        elif self.fed == 1:
            return (127, 127, 255)
        else:
            return (0, 0, 255)

    def x(self):
        """Returns x coordinate"""
        return int(self.coord[0])

    def y(self):
        """Returns y coordinate"""
        return int(self.coord[1])

    def resetFed(self):
        """Sets self.fed to 0"""
        self.fed = 0

# class from tutorial: https://www.youtube.com/watch?v=4_9twnEduFA
class Button():
    def __init__(self, color, x, y, width, height, text=''):
        '''Creates a button with a coordinate, height width and color and with text if wanted'''
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        '''Draws button on win canvas using pygame'''
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', SIZE//20)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        '''Returns true if mouse pointer is over the button on the canvas'''
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

    def number(self):
        '''Returns the number on the button, specific for this program as all text fields are integers'''
        return int(self.text)

def frame(win, inColor, frameColor, dimensions, frameThickness):
    """
    Draws a frame
    inColor : Color inside the frame
    frameColor : Color of frame
    dimensions : Location and dimensions of wanted frame
    frameThickness : Thickness of frame
    """
    pygame.draw.rect(win, inColor, dimensions)
    pygame.draw.rect(win, frameColor, dimensions, frameThickness)

def draw(win, cells, buttons, food, days):
    '''Draws the cells and food pellets (food coordinates) in a pygame window and a graph
    representing the current cell culture in the same window
    cells : List of cell objects to be drawn
    buttons : List of buttons to be drawn
    food : List of foodBits to be drawn
    days : Integer representing the number of days that has passed
    '''
    pygame.draw.rect(win, WHITE, (0,0, SIZE, SIZE))

    #Draws cells and food
    for blob in cells:
        pygame.draw.circle(win, blob.color(), (blob.x(), blob.y()), RADIUS)
    for foodBit in food:
        pygame.draw.rect(win, (0, 0, 255), (foodBit[0], foodBit[1], 2, 2))

    #Divide the window into portions
    frame(win, WHITE, BLACK, (0, SIZE, SIZE, SIZE*2//5), 3)
    frame(win, WHITE, BLACK, (SIZE, 0, SIZE * 2 // 5, SIZE), 3)
    frame(win, WHITE, BLACK, (SIZE, SIZE, SIZE * 2 // 5, SIZE * 2 // 5), 3)

    # Draw lables for table
    font = pygame.font.SysFont('comicsans', SIZE // 20)
    font2 = pygame.font.SysFont('comicsans', SIZE // 10)
    visLable = font.render("vis", 1, (0, 0, 0))
    velLable = font.render("vel", 1, (0, 0, 0))
    win.blit(visLable, (SIZE // 20, SIZE * 13 // 10))
    win.blit(velLable, (SIZE * 17 // 20, SIZE * 13 // 10))

    # Draw
    maxPop = 0
    # Find highest number of cells with the same velocity
    for i in range(0, 31):
        counter1 = 0
        for blob in cells:
            if blob.vel == i:
                counter1 += 1
        if counter1 > maxPop:
            maxPop = counter1
    # Draw table with max height of of bars to be 2/5 of the size of the cell area.
    for i in range(0, 31):
        counter2 = 0
        for blob in cells:
            if blob.vel == i:
                counter2 += 1
        red = i * 255 / 30
        green = 255 - red
        pygame.draw.rect(win, (red, green, 0), (SIZE // 5 + i * (SIZE * 4 // (6*31)), (SIZE * 13 // 10) - counter2 * SIZE // (5 * maxPop), 6, counter2 * SIZE // (5 * maxPop)))
    pygame.draw.rect(win, BLACK, (SIZE // 6, SIZE * 13 // 10, SIZE * 4 // 6, 2))

    # Draw day counter
    dayLable = font2.render("Days: " + str(days), 1, (0, 0, 0))
    win.blit(dayLable ,(SIZE + (SIZE * 1 // 5 - dayLable.get_width() // 2), SIZE + (SIZE * 1 // 5 - dayLable.get_height() // 2)))

    # Draw header for menu and buttons
    menuHeader = font2.render("# of days:", 1, (0, 0, 0))
    win.blit(menuHeader, (SIZE * 41 // 40 , SIZE // 40))
    for button in buttons:
        button.draw(win, BLACK)

    pygame.display.update()

def menu(event, buttons, standard):
    """Creates prints a menu window using pygame that lets the user select the
    number of cycles/days the program shall perform in a row."""
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        for button in buttons:
            if button.isOver(pos):
                return button.number()
    return standard

def main():
    """Main function which calls on all above functions and runs simulator"""

    # Initialize vital pygame factors
    pygame.init()
    win = pygame.display.set_mode((int(SIZE * 7 / 5), int(SIZE * 7 / 5)))
    pygame.display.set_caption("Simulator")
    clock = pygame.time.Clock()

    if MUSIC:
        pygame.mixer.music.load('old_song.mp3')
        pygame.mixer.music.play(-1)

    #Create buttons
    buttons = []
    for i in range(0, 4):
        buttons.append(Button((0, 255, 0), SIZE*11//10, (i+1)*SIZE//5, SIZE//5, SIZE//10, "1" + "0"*i))
    #Creation of cell objects
    cells = []
    for i in range(NUMBER):
        vel = random.randint(0, 30)
        vis = VIS_TO_VEL_RATIO * (30 - vel)
        cells.append(Cell(vel, vis))
    #Creation of first batch of food
    food = []
    for i in range(0, FOOD_PER_DAY):
        food.append((random.randint(10, SIZE - 10), random.randint(10, SIZE - 10)))

    #Initialize counter variables
    days = 0
    framesToPerform = 0
    wantedDays = 0

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            wantedDays = menu(event, buttons, wantedDays)
            # Closes window if x is pressed
            if event.type == pygame.QUIT:
                run = False

        if framesToPerform == 0:
            framesToPerform = wantedDays * DAY_LENGTH
            framesToNight = DAY_LENGTH
            wantedDays = 0

        #Repeats this step until wanted amount of frames (and therefore days) are performed
        if framesToPerform > 0:
            #Move cells and eat
            for blob in cells:
                blob.angleChange(food,framesToNight)
                blob.move()
                blob.eat(food)
            framesToPerform -= 1
            framesToNight -= 1
            if framesToNight == 0:
                cellsToRemove = [] # Keeps track of what cells to remove in next step
                # Adds hungry cells and cells who aren't on an edge to kill list
                for blob in cells:
                    if blob.fed == 0 or ((blob.y() != SIZE and blob.y() != 0) and (blob.x() != SIZE and blob.x() != 0)):
                        cellsToRemove.append(blob)
                #Kill cells
                for hungryCell in cellsToRemove:
                    cells.remove(hungryCell)
                #Reproduce and reset self.fed to 0 for all cells
                for blob in cells:
                    if blob.fed == 2:
                        cells.append(blob.clone())
                    blob.resetFed()
                #Add new food
                for i in range(0, FOOD_PER_DAY):
                    food.append((random.randint(10, SIZE-10), random.randint(10, SIZE-10)))
                #New day
                framesToNight = DAY_LENGTH
                days += 1
        draw(win, cells, buttons, food, days)
    pygame.quit()

if __name__ == '__main__':
    main()