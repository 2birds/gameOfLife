#!/usr/bin/python
from gameOfLifeClass import *
import pygame
import sys

if 3>=len(sys.argv)>1:
    for i in range(1, len(sys.argv)):
        if type(sys.argv[i])==int:
            boardWidth=sys.argv[i]

        elif type(sys.argv[i])==str:
            firstState=sys.argv[i]
            f=open(firstState,'r')
            firstState=[]
            while 1:
                coord=f.readline()
                if coord=='\n':
                    break
                else:
                    firstState.append(eval(coord.strip('\n')))
            print firstState
            f.close
            

elif len(sys.argv)>3:
    print """Game of Life takes up to 2 arguments (the size of the board 
and a file containing a list of tuples representing the co-ordinates
of live cells."""
    exit()

else:
    boardWidth=55
    firstState=[]

board=Board(55) # Number of cells = 55 to the power of 2. Alter to requirements.
cell_side=12 # If you change this, resize the images as well.
screen = pygame.display.set_mode((board.side*cell_side,board.side*cell_side))

deadSquare=pygame.image.load('golImages/deadSquare.gif').convert()
liveSquare=pygame.image.load('golImages/liveSquare.gif').convert()

def update(): # Updates and displays every cell.
    for cell in board.cells:
        cellPos = pygame.Rect(cell[0]*cell_side,cell[1]*cell_side, cell_side, cell_side)
        if board.cells[cell]==True:
            screen.blit(liveSquare, cellPos)
        else:
            screen.blit(deadSquare, cellPos)
    pygame.display.update()

for i in firstState:
    board.switchState(i)

update() # Displays initial state (all dead, Dave..)

breakOut=False # Condition for breaking out of the following loops.

while breakOut == False: # This loop is for setting the initial state.
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x=pos[0]/cell_side # Treats canvas as a grid of squares.
            y=pos[1]/cell_side
            board.switchState((x,y)) # Changes state of given cell
            update()
            
            print "(%s,%s)" %(x,y) 
	    # Just for debugging, but provides a record of initial state.
        elif event.type == pygame.KEYDOWN:
            print "Keydown"
            if event.key == pygame.K_s:
                print "s was pressed"
                breakOut=True

breakOut=False # Resets break condition.

while breakOut==False:
    board.step() # Determines next state.
    update()
    pygame.time.delay(150)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    breakOut=True

exit()
