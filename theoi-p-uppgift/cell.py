import math
import random

SIZE = 300
RADIUS = 7
NUMBER = 20
SEARCH_ANGLE = math.pi/8
DAY_LENGTH = 0
FPS = 27
VIS_TO_VEL_RATIO = 10

class Cell:
    """cells have a location self.coord, a velocity self.vel,
    a vision length self.vis, an angle (direction it is moving) self.angle,
    and number of foodBits it has eaten self.fed"""

    def __init__(self, vel, vis):
        """Creates a cell where self.coord is randomized, self.fed = 0 and
        self.angle depends on self.coord to face directly away from the nearest edge"""
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
        """Returns coordinate in food closest to self.coord if one
        exists within a radius of self.vis from the cell."""
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
        self.fed = 0