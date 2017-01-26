from world import World
from util import Stack
from util import Queue
from util import PriorityQueue
from node import Node
from copy import deepcopy


def HowToReturnPath(array2d, s, e, w, h):
    array2d[s] = [1, 1, 1, 1]
    array2d[e] = [1, 1, 1, 1]
    world = World(array2d, s, e, w, h)
    print world
    # path = depthFirstSearch(world)
    # path = breadthFirstSearch(world)
    # path = iterativeDeepeningSearch(world)
    path = uniformCostSearch(world)
    # path = aStarSearch(world)
    print 'path:', path
    ans = []
    for r,c,i in path:
        num=r*world.width()+c
        if(i == 0):
            ans.append((num, 2))
        elif (i == 2):
            ans.append((num, 0))
        else:
            ans.append((num , i))
    # print ans
    return ans


def depthFirstSearch(world):
    checked = [[False for _ in range(world.width())] for _ in range(world.height())]
    stack = Stack()
    node = Node(world, world.src[0], world.src[1], list(), 0, 0)
    stack.push(node)
    while not stack.isEmpty():
        node = stack.pop()
        block = deepcopy(world.block(node.row, node.col))
        # print 'rotate', node.rotate*90
        world.rotate_block(node.row, node.col, node.rotate*90)
        # print world
        # print node.row, node.col
        checked[node.row][node.col] = True
        if (node.row, node.col) == world.dst:
            node.parents.pop(0)
            return node.parents
        else:

            for i in range(4):
                if node.row - 1 >= 0:
                    child = Node(world, node.row - 1, node.col, node.parents, i, node.level+1)
                    if world.connect_up_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'up',(child.row, child.col, i)
                        stack.push(child)
                    world.rotate_block(child.row, child.col, 90)


            for i in range(4):
                if node.col + 1 < world.height():
                    child = Node(world, node.row, node.col + 1, node.parents, i, node.level+1)
                    if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'right', (child.row, child.col, i)
                        stack.push(child)
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.row + 1 < world.height():
                    child = Node(world, node.row + 1, node.col, node.parents, i, node.level+1)
                    if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'down', (child.row, child.col, i)
                        stack.push(child)
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col - 1 >= 0:
                    child = Node(world, node.row, node.col - 1, node.parents, i, node.level+1)
                    if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'left', (child.row, child.col, i)
                        stack.push(child)
                    world.rotate_block(child.row, child.col, 90)
        world.blocks[node.row][node.col] = block


def breadthFirstSearch(world):
    checked = [[False for _ in range(world.width())] for _ in range(world.height())]
    queue = Queue()
    node = Node(world, world.src[0], world.src[1], list(), 0, 0)
    queue.push(node)
    while not queue.isEmpty():

        node = queue.pop()
        block = deepcopy(world.block(node.row, node.col))
        # print 'rotate', node.rotate*90
        world.rotate_block(node.row, node.col, node.rotate * 90)
        # print world
        # print node.row, node.col
        checked[node.row][node.col] = True
        if (node.row, node.col) == world.dst:
            node.parents.pop(0)
            return node.parents
        else:

            for i in range(4):
                if node.row - 1 >= 0:
                    child = Node(world, node.row - 1, node.col, node.parents, i, node.level+1)
                    if world.connect_up_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'up',(child.row, child.col, i)
                        queue.push(child)
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col + 1 < 3:
                    child = Node(world, node.row, node.col + 1, node.parents, i, node.level+1)
                    if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'right', (child.row, child.col, i)
                        queue.push(child)
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.row + 1 < 3:
                    child = Node(world, node.row + 1, node.col, node.parents, i, node.level+1)
                    if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'down', (child.row, child.col, i)
                        queue.push(child)
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col - 1 >= 0:

                    child = Node(world, node.row, node.col - 1, node.parents, i, node.level+1)
                    if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'left', (child.row, child.col, i)
                        queue.push(child)
                    world.rotate_block(child.row, child.col, 90)
        world.blocks[node.row][node.col] = block
    return []


def IDS(world, limit):
    if limit <= 0:
        return []
    else:
        checked = [[False for _ in range(world.width())] for _ in range(world.height())]
        stack = Stack()
        node = Node(world, world.src[0], world.src[1], list(), 0, 0)
        stack.push(node)
        while not stack.isEmpty():
            node = stack.pop()
            block = deepcopy(world.block(node.row, node.col))
            # print 'rotate', node.rotate*90
            world.rotate_block(node.row, node.col, node.rotate * 90)
            # print world
            # print node.row, node.col
            checked[node.row][node.col] = True
            if (node.row, node.col) == world.dst:
                node.parents.pop(0)
                return node.parents
            else:
                if node.level+1 <= limit:
                    # print node.level+1
                    for i in range(4):
                        if node.row - 1 >= 0:
                            child = Node(world, node.row - 1, node.col, node.parents, i, node.level+1)
                            if world.connect_up_block(node.row, node.col) and not checked[child.row][child.col]:
                                child.parents.append((node.row, node.col, node.rotate))
                                # print 'up',(child.row, child.col, i)
                                stack.push(child)
                            world.rotate_block(child.row, child.col, 90)

                    for i in range(4):
                        if node.col + 1 < world.height():
                            child = Node(world, node.row, node.col + 1, node.parents, i, node.level+1)
                            if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                                child.parents.append((node.row, node.col, node.rotate))
                                # print 'right', (child.row, child.col, i)
                                stack.push(child)
                            world.rotate_block(child.row, child.col, 90)

                    for i in range(4):
                        if node.row + 1 < world.height():
                            child = Node(world, node.row + 1, node.col, node.parents, i, node.level+1)
                            if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                                child.parents.append((node.row, node.col, node.rotate))
                                # print 'down', (child.row, child.col, i)
                                stack.push(child)
                            world.rotate_block(child.row, child.col, 90)

                    for i in range(4):
                        if node.col - 1 >= 0:

                            child = Node(world, node.row, node.col - 1, node.parents, i, node.level+1)
                            if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                                child.parents.append((node.row, node.col, node.rotate))
                                # print 'left', (child.row, child.col, i)
                                stack.push(child)
                            world.rotate_block(child.row, child.col, 90)
            world.blocks[node.row][node.col] = block
        return[]


def iterativeDeepeningSearch(world):
    for i in range(1,5):
        p = IDS(world, i)
        if len(p):
           return p
    return []


def uniformCostSearch(world):
    checked = [[False for _ in range(world.width())] for _ in range(world.height())]
    Pqueue = PriorityQueue()
    node = Node(world, world.src[0], world.src[1], list(), 0, 0)
    Pqueue.push(node, 0)
    while not Pqueue.isEmpty():
        node = Pqueue.pop()
        block = deepcopy(world.block(node.row, node.col))
        # print 'rotate', node.rotate*90
        world.rotate_block(node.row, node.col, node.rotate * 90)
        # print world
        # print node.row, node.col
        checked[node.row][node.col] = True
        if (node.row, node.col) == world.dst:
            node.parents.pop(0)
            return node.parents
        else:

            for i in range(4):
                if node.row - 1 >= 0:
                    child = Node(world, node.row - 1, node.col, node.parents, i, node.level + 1)
                    if world.connect_up_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'up',(child.row, child.col, i)
                        Pqueue.push(child, child.level+i)
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col + 1 < 3:
                    child = Node(world, node.row, node.col + 1, node.parents, i, node.level + 1)
                    if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'right', (child.row, child.col, i)
                        Pqueue.push(child, child.level+i)
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.row + 1 < 3:
                    child = Node(world, node.row + 1, node.col, node.parents, i, node.level + 1)
                    if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'down', (child.row, child.col, i)
                        Pqueue.push(child, child.level+i)
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col - 1 >= 0:

                    child = Node(world, node.row, node.col - 1, node.parents, i, node.level + 1)
                    if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'left', (child.row, child.col, i)
                        Pqueue.push(child, child.level+i)
                    world.rotate_block(child.row, child.col, 90)
        world.blocks[node.row][node.col] = block
    return []


def manhattanHeuristicFunction(world, current_node):

    return (current_node.row - world.dst[0])+(current_node.col - world.dst[1])


def heuristicFunction(world, current_node):

    return current_node.col - world.dst[1]


# def aStarSearch(world):
#     Pqueue1 = PriorityQueue()
#     # Pqueue2 = PriorityQueue()
#     closedlist= list
#     node = Node(world, world.src[0], world.src[1], list(), 0, 0)
#     Pqueue1.push(node, 0)
#     while not Pqueue1.isEmpty():
#         node = Pqueue1.pop()
#         block = deepcopy(world.block(node.row, node.col))
#         world.rotate_block(node.row, node.col, node.rotate * 90)
#         for i in range(4):
#             if node.row - 1 >= 0:
#                 child = Node(world, node.row - 1, node.col, node.parents, i, node.level + 1)
#                 if world.connect_up_block(node.row, node.col):
#                     child.parents.append((node.row, node.col, node.rotate))
#                     # print 'up',(child.row, child.col, i)
#                     # queue.push(child)
#                     if (child.row, child.col) == world.dst:
#                         child.parents.pop(0)
#                         child.g = node.g + i
#                         child.h = manhattanHeuristicFunction(world, child)
#                         child.f = child.g + child.h
#                         return child.parents
#                     if():
#
#                     if():
#                 world.rotate_block(child.row, child.col, 90)
#
#         for i in range(4):
#             if node.col + 1 < 3:
#                 child = Node(world, node.row, node.col + 1, node.parents, i, node.level + 1)
#                 if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
#                     child.parents.append((node.row, node.col, node.rotate))
#                     if (child.row, child.col) == world.dst:
#                         child.parents.pop(0)
#                         child.g = node.g + i
#                         child.h = manhattanHeuristicFunction(world, child)
#                         child.f = child.g + child.h
#                         return child.parents
#                     if ():
#
#                     if ():
#                 world.rotate_block(child.row, child.col, 90)
#
#         for i in range(4):
#             if node.row + 1 < 3:
#                 child = Node(world, node.row + 1, node.col, node.parents, i, node.level + 1)
#                 if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
#                     child.parents.append((node.row, node.col, node.rotate))
#                     if (child.row, child.col) == world.dst:
#                         child.parents.pop(0)
#                         child.g = node.g + i
#                         child.h = manhattanHeuristicFunction(world, child)
#                         child.f = child.g + child.h
#                         return child.parents
#                     if ():
#
#                     if ():
#                 world.rotate_block(child.row, child.col, 90)
#
#         for i in range(4):
#             if node.col - 1 >= 0:
#                 child = Node(world, node.row, node.col - 1, node.parents, i, node.level + 1)
#                 if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
#                     child.parents.append((node.row, node.col, node.rotate))
#                     if (child.row, child.col) == world.dst:
#                         child.parents.pop(0)
#                         child.g = node.g + i
#                         child.h = manhattanHeuristicFunction(world, child)
#                         child.f = child.g + child.h
#                         return child.parents
#                     if ():
#
#                     if ():
#                 world.rotate_block(child.row, child.col, 90)
#         closedlist.append(node)
#         world.blocks[node.row][node.col] = block
#     return []
#
