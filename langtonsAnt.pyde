'''Langton's ant
Jan. 30, 2018
with Jared'''

cols = 101 #set grid size
sz = 600 // cols #size of square
BLACK = color(0)
WHITE = color(255)
RED = color(255,0,0)

class Cell:
    def __init__(self,row,col):
        #location properties
        self.row = row 
        self.col = col
        #On or Off
        self.on = 0 #False #starts "off" = WHITE
        self.sz = sz #size
        
    def update(self):
        #if ant is on my location
        if ant.r == self.row and ant.c == self.col:
            self.on += 1
        #my color: If my "on" number is odd, black
        if self.on % 2 == 1:
            fill(BLACK)
        else: #even, white
            fill(WHITE)
        #draw the square
        rect(self.col*self.sz,self.row*self.sz,
             self.sz,self.sz)
        
class Ant:
    def __init__(self):
        self.sz = sz #size 
        self.dir = 2 # left
        #start in middle of grid
        self.r = cols//2
        self.c = cols//2
        
        
    def colorsquare(self):
        #check if off the grid
        if self.r == cols-1:
            self.r = 0
        if self.r < 0:
            self.r = cols
        if self.c == cols-1:
            self.c = 0
        if self.c < 0:
            self.c = cols
        #now color
        if cellList[cols*self.r+self.c].on % 2 == 1: #if it's on
            self.dir = (self.dir + 1) % 4 #turn right
            #cellList[cols*self.r+self.c].red == True
            #println("on!")
        else: #turn left
            self.dir = (self.dir - 1) % 4
        
        #0 is right, 1 is up, 2 is left, 3 is down
        if self.dir == 0: 
            self.c += 1 #right
        elif self.dir == 1:
            self.r -= 1 #up
        elif self.dir == 2: #left
            self.c -= 1
        else: #self.dir = 3
            self.r += 1 #down    
                
    def update(self):
        fill(255,0,0) #red
        #set x-y location according to row and column
        self.x = self.sz * self.c + self.sz/2.0
        self.y = self.sz * self.r + self.sz/2.0
        #finally, draw the ant. It could use a head.
        ellipse(self.x,self.y,
                self.sz,self.sz/10.0)
        
def setup():
    global cellList,ant
    ellipseMode(CENTER)
    size(600,600)
    noStroke() #no outline for squares
    cellList = [] #empty list to store cells in
    for r in range(cols): #for each row,...
        #cellList.append([])
        for c in range(cols): #put in "cols" Cells into the columns
            cellList.append(Cell(r,c))
    ant = Ant() #create the ant
        
    
def draw():
    frameRate(40) #slow down, speed up
    ant.colorsquare() #move the ant, check the color of the square
    for cell in cellList:
        cell.update() #update cell color
    ant.update() #draw the ant
    
    