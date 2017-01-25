from copy import deepcopy

class Node:
    def __init__(self, world, r, c, p, i):
        self.row = r
        self.col = c
        #self.block = world.block(r, c)
        self.rotate = i
        self.parents = deepcopy(p)