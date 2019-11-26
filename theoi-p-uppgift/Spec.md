## Inledning
Programmet kommer simulera små Varelser som letar efter föda på ett 2d plan. Varelserna kommer att ha två genetiska variabler, hur långt runt om kring sig de kan se eller känna om det finns mat och hur snabbt de rör sig på planet. Om en varelse lyckas hitta 2 bitar föda på en cykel (framåt kallad en dag) kommer varelsen att klona sig själv med potentiell mutation där antingen rörelsehastighet går upp och syn går ner eller vice versa. Om en varelse inte hittar någon föda kommer varelsen dö. När dagen är slut kommer alla varelser som inte befiner sig på en kant av planet dö. Programmet ska därefter också presentera grafiskt vilken ratio av hastighet mot syn är det som funkar bäst för varelserna.


Svårigheter kommer ligga i att koda hur varelserna ska bete sig i vanliga röresler, vilken mat de ska prioritera och att presentera den resulterande varelsegruppen på ett grafiskt sätt.

## Användarscenarier
En användare kan starta programmet och kommer ges ett val på hur många dagar i taget användaren vill simulera: 1, 10, 100 eller 1000. När användaren har valt kommer önskat antal dagar att simuleras.

Varje dag består av att ett antal matbitar sprids ut på planet. Sedan kommer varelser gå från kanterna in i mitten och leta efter matbitarna, när en matbit kommer inom deras synfält kommer varelsen röra sig mot den och äta den. Om en varelse har ätit två matbitar kommer den återvända till närmsta kant. Om en varelse har ätit en bit men dagen nästan är över kommer den återvända till närmsta kant. De varelser som har återvänt till en kant och har ätit 1 matbit i slutet av dagen överlever, de som ätit två klonar sig, sedan börjar nästa dag.

Efter önskat antal dagar har löpt kommer användaren kunna se en tabell som visar hur många av varelserna har en viss hastighet (alternativt synlängd). Därefter kan användaren välja att simulera i fler dagar eller att stänga programmet.

Det användaren kan finna intressant är att se hur dessa små varelser muterar och dör ut i en förenklad simulation av evolution. Annars kan det också bara vara estetiskt underhållande att se små prickar springa runt i ett fönster på ens dator. Varelsernas färg kommer också ändras beroende på deras hastighet och synlängd, vilket också kan underhålla de som är lättroade.

## Programskellet
### Klass: Cell
En klass där varje objekt är en varelse med följande variabler: x och y koordinat(coord = [x,y]), hastighet (self.vel = int), synlängd (self.vis = int), vinkel cellen är riktad åt (self.angle = float), hur mycket cellen har ätit den dagen (self.fed = int)

```
import pygame
import math
import random

SIZE: The size of the plane that the cells can move in
RADIUS: Radius of the cells
NUMBER: Number of cells
SEARCH_ANGLE: How much an angle can change relative to to the objects current self.angle
DAY_LENGTH: The number of ticks per day
FPS: Ticks per second

class Cell:
    """cells have a location self.coord, a velocity self.vel, 
    a vision length self.vis, an angle (direction it is moving) self.angle, 
    and number of foodBits it has eaten self.fed"""

    def __init__(self, vel, vis):
        """Creates a cell where self.coord is randomized, self.fed = 0 and 
        self.angle depends on self.coord to face directly away from the nearest edge"""
        pass

    def move(self):
        """Changes self.coord depending on self.angle and self.vel"""
        pass

    def checkFood(self, food):
        """Returns True if a coordinate in the list food is within 
        a circle around the cell with the radius self.vis, otherwise 
        returns False."""
        pass

    def searchFood(self, food):
        """Returns coordinate in list closest to self.coord if one 
        exists within a radius of self.vis from the cell."""
        pass

    def angleChange(self, food, time):
        """Changes self.angle depending on time (how long until the end of the day), 
        on checkFood and searchFood to point to nearest coordinate in the list food. 
        If no coordinate in food is within range and time is not close to 0  self.angle 
        will be randomized relative to the current angle."""
        pass

    def eat(self, food):
        """Checks if any coordinate in the list food is located within the cell using 
        self.coord and RADIUS, if so self.fed += 1 and the specific coordinate is removed 
        from the food list)"""
        pass

    def clone(self):
        """Creates a new cell object similar to self but with possible slight changes to vis and vel"""
        pass

    def color(self):
        """Returns an RGB tuple representing the selfs color"""
        pass
       
    def x(self):
        """Returns x coordinate"""
        pass
        
    def y(self):
        """Returns y coordinate"""
        pass
    
    def velocity():
        """Returns self.vel"""
        pass
        
    def vision():
        """Returns self.vis"""
        pass

def draw(cells, food):
    """Draws the cells and food pellets (food coordinates) in a pygame window and a graph 
    representing the current cell culture in the same window"""
    pass

def menu():
    """Creates prints a menu window using pygame that lets the user select the 
    number of cycles/days the program shall perform in a row.""
    pass

def main():
    """Main function which calls on all above functions"""
    pass
```

## Programflöde och dataflöde

main() skapar först en lista med objekt från klassen "cell()" sedan (i en while True: loop) kallar den på menu() för att få intput på hur många "dagar" (cyklar) som ska köras. Sedan kör main() en loop som kör önskat antal cyklar, varje cykel börjar med att listan food blir appendad med nya koordinater för mat, en "nested for loop" kör sedan igenom följande för alla skapade celler ett antal gånger (en loop som kör DAY_LENGTH gånger):

1. kallar på cell.angle():

1.1 cell.angle() använder time variabeln och fed för att bestämma om self.angle ska riktas mot närmsta kant (säkerhet)

1.2 om inte kommer cell.angle() kalla på cell.checkFood() för att se om cellen har någon matbit inom sin syn

1.3 om cell.checkFood() returnerar True kommer cell.angle kalla på searchFood() för att hitta närmsta matbit och rikta self.angle() ditåt

1.4 om cell.checkFood() returnerar False kommer cell.angle att slumpa en vinkel inom intervallet [self.angle() - SEARCH_ANGLE, self.angle() + SEARCH_ANGLE]

2. main() kallar på cell.move() för att ändra self.coord relativt till self.angle() och self.vel()
3. main() kallar på cell.eat() för att cellen ska ""äta" de food koordinater den ligger på.
4. main() kallar på draw() funktionen när ovanstående har gjorts för alla celler för att rita resultatbilden efter det senaste tick:et.

När alla ticks har gjorts så tar main() bort alla celler vars self.fed = 0 eller om (x == 0 or x == SIZE or y == 0 or y == SIZE) är falskt. Sedan börjar nästa dag (loopar om).

När önskat antal dagar är gjorda pausar programmet och väntar på nästa input, programmet stängs genom att klicka på fönstrets x knapp (detta kodas också).
