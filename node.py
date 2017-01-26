from copy import deepcopy

class Node:
    def __init__(self, world, row, col, parentlist, angle, level):
        self.row = row
        self.col = col
        #self.block = world.block(r, c)
        self.rotate = angle
        self.parents = deepcopy(parentlist)
        self.level = level
        self.f = 0
        self.g = 0
        self.h = 0
