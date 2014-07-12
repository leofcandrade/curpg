#! usr/bin/python

class Person:
   'Common base class for all employees'
   perCount = 0

   def __init__(self, name):
      self.name = name
      self.x = 0
      self.y = 0
      self.backpack = []
      Person.perCount += 1
   

   def walk(self,direction):
     dirs = {'right':['x',+1],'left':['x',-1],
             'up':['y',-1],'down':['y',+1] }
     if dirs[direction][0] == 'x':
         self.x += dirs[direction][1]
     elif dirs[direction][0] == 'y':
         self.y += dirs[direction][1]

   def getPos(self):
       return {'x':self.x,'y':self.y}

class Scene:
    totScenes = 0
    def __init__(self, length,width):
        self.width = width
        self.length = length
        self.grid = [[0 for x in xrange(length)] for x in xrange(width)] 
        Scene.totScenes += 1
    def addTrap(self, xPos,yPos):
        self.grid[xPos][yPos] = -1
    def viewGrid(self):
        for i in range(self.length):
            for j in range(self.width):
                print self.grid[i][j]
            #print '\n'

def checkSituation(person,scene):
    if scene.grid[person.x][person.y] == -1:
        print 'You stepped on some serious shit dawg be careful yo'

'''class Controller:
    def __init__(self,person,scene):'''
        
