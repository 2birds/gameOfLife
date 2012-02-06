#!/usr/bin/python
class Board(object):
    """Represents all the cells of a square game-of-life board"""
    def __init__(self, side_width):
        self.side=side_width
        self.cells={}
        self.nextCells={}
        for x in range(self.side):
            for y in range(self.side):
                self.cells[(x,y)]=False

    def __str__(self):
        b=''
        for i in self.cells:
            if self.cells[i] == True:
                alive="alive"
            else:
                alive="dead"
            b+="Cell "+str(i)+" is "+alive+".\n"
        return b

    def switchState(self, cell):
        """Changes the state of a give cell(x,y)"""
        if self.cells[cell]==True:
            self.cells[cell]=False
        else:
            self.cells[cell]=True

    def nextState(self, cell):
        """Determines and stores the next state of a given cell (x, y)"""
        count=0
        edge=0
        for x in range(cell[0]-1,cell[0]+2):
            for y in range(cell[1]-1,cell[1]+2):
                if not (x==cell[0] and y==cell[1]):
                    try: # This method will seek non-existant cells
                        if self.cells[(x,y)]==True:
                            count+=1
                    except:
                        edge+=1
        if self.cells[cell]==False: # Only one interesting case for dead cells
            if count==3:
                self.nextCells[cell]=True
        else: # For live cells
            if count<2 or count>3:
                self.nextCells[cell]=False

    def step(self):
        """Thin method for advancing the state of the board one step"""
        for x in range(self.side):
            for y in range(self.side):
                self.nextState((x,y))
        for i in self.nextCells:
            self.cells[i]=self.nextCells[i]
        
                            
