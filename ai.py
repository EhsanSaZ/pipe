from world import World
from util import Stack
from util import Queue
from util import PriorityQueue
from node import Node
from copy import deepcopy
import time

def HowToReturnPath(array2d, s, e, w, h):
    array2d[s] = [1, 1, 1, 1]
    array2d[e] = [1, 1, 1, 1]
    world = World(array2d, s, e, w, h)
    print world
    # path = depthFirstSearch(world)
    # path = breadthFirstSearch(world)
    # path = iterativeDeepeningSearch(world)
    # path = uniformCostSearch(world)
    # path = aStarSearch(world)
    path = aStarSearchMyHeuristic(world)
    print 'path:', path
    ans = []
    for r, c, i in path:
        num = r*world.width()+c
        if i == 0:
            ans.append((num, 2))
        elif i == 2:
            ans.append((num, 0))
        else:
            ans.append((num, i))
    # print ans
    return ans


def depthFirstSearch(world):
    counter = 0
    checked = [[False for _ in range(world.width())] for _ in range(world.height())]
    stack = Stack()
    node = Node(world, world.src[0], world.src[1], list(), 0, 0)
    t1 = time.time()
    stack.push(node)
    counter += 1
    whilenum = 0
    while not stack.isEmpty():
        node = stack.pop()
        block = deepcopy(world.block(node.row, node.col))
        # print 'rotate', node.rotate*90
        world.rotate_block(node.row, node.col, node.rotate*90)
        # print world
        # print node.row, node.col
        checked[node.row][node.col] = True
        if (node.row, node.col) == world.dst:
            t2 = time.time()
            node.parents.pop(0)
            print 'Effective branch factor :', float(counter/whilenum)
            print 'number of nodes in DFS: ', counter, 'TIME : ', t2-t1
            return node.parents
        else:

            for i in range(4):
                if node.row - 1 >= 0:
                    child = Node(world, node.row - 1, node.col, node.parents, i, node.level+1)
                    if world.connect_up_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'up',(child.row, child.col, i)
                        stack.push(child)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)


            for i in range(4):
                if node.col + 1 < world.height():
                    child = Node(world, node.row, node.col + 1, node.parents, i, node.level+1)
                    if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'right', (child.row, child.col, i)
                        stack.push(child)
                        counter +=1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.row + 1 < world.height():
                    child = Node(world, node.row + 1, node.col, node.parents, i, node.level+1)
                    if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'down', (child.row, child.col, i)
                        stack.push(child)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col - 1 >= 0:
                    child = Node(world, node.row, node.col - 1, node.parents, i, node.level+1)
                    if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'left', (child.row, child.col, i)
                        stack.push(child)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)
        world.blocks[node.row][node.col] = block
        whilenum += 1
    return []

def breadthFirstSearch(world):
    counter = 0
    checked = [[False for _ in range(world.width())] for _ in range(world.height())]
    queue = Queue()
    node = Node(world, world.src[0], world.src[1], list(), 0, 0)
    t1 = time.time()
    queue.push(node)
    counter += 1
    whilenum = 0
    while not queue.isEmpty():
        node = queue.pop()
        block = deepcopy(world.block(node.row, node.col))
        # print 'rotate', node.rotate*90
        world.rotate_block(node.row, node.col, node.rotate * 90)
        # print world
        # print node.row, node.col
        checked[node.row][node.col] = True
        if (node.row, node.col) == world.dst:
            t2 = time.time()
            node.parents.pop(0)
            print 'Effective branch factor :', float(counter / whilenum)
            print 'number of nodes In BFS:', counter, 'TIME', t2-t1
            return node.parents
        else:
            for i in range(4):
                if node.row - 1 >= 0:
                    child = Node(world, node.row - 1, node.col, node.parents, i, node.level+1)
                    if world.connect_up_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'up',(child.row, child.col, i)
                        queue.push(child)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col + 1 < world.height():
                    child = Node(world, node.row, node.col + 1, node.parents, i, node.level+1)
                    if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'right', (child.row, child.col, i)
                        queue.push(child)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.row + 1 < world.height():
                    child = Node(world, node.row + 1, node.col, node.parents, i, node.level+1)
                    if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'down', (child.row, child.col, i)
                        queue.push(child)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col - 1 >= 0:

                    child = Node(world, node.row, node.col - 1, node.parents, i, node.level+1)
                    if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'left', (child.row, child.col, i)
                        queue.push(child)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)
        world.blocks[node.row][node.col] = block
        whilenum += 1
    return []


def IDS(world, limit):
    if limit <= 0:
        return []
    else:
        counter = 0
        checked = [[False for _ in range(world.width())] for _ in range(world.height())]
        stack = Stack()
        node = Node(world, world.src[0], world.src[1], list(), 0, 0)
        t1 = time.time()
        stack.push(node)
        counter += 1
        whilenum = 0
        while not stack.isEmpty():
            node = stack.pop()
            block = deepcopy(world.block(node.row, node.col))
            # print 'rotate', node.rotate*90
            world.rotate_block(node.row, node.col, node.rotate * 90)
            # print world
            # print node.row, node.col
            checked[node.row][node.col] = True
            if (node.row, node.col) == world.dst:
                t2 = time.time()
                node.parents.pop(0)
                print 'Effective branch factor :', float(counter / whilenum)
                print 'number of nodes in IDS: ', counter, 'TIME',  t2-t1
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
                                counter += 1
                            world.rotate_block(child.row, child.col, 90)

                    for i in range(4):
                        if node.col + 1 < world.height():
                            child = Node(world, node.row, node.col + 1, node.parents, i, node.level+1)
                            if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                                child.parents.append((node.row, node.col, node.rotate))
                                # print 'right', (child.row, child.col, i)
                                stack.push(child)
                                counter += 1
                            world.rotate_block(child.row, child.col, 90)

                    for i in range(4):
                        if node.row + 1 < world.height():
                            child = Node(world, node.row + 1, node.col, node.parents, i, node.level+1)
                            if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                                child.parents.append((node.row, node.col, node.rotate))
                                # print 'down', (child.row, child.col, i)
                                stack.push(child)
                                counter += 1
                            world.rotate_block(child.row, child.col, 90)

                    for i in range(4):
                        if node.col - 1 >= 0:
                            child = Node(world, node.row, node.col - 1, node.parents, i, node.level+1)
                            if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                                child.parents.append((node.row, node.col, node.rotate))
                                # print 'left', (child.row, child.col, i)
                                stack.push(child)
                                counter += 1
                            world.rotate_block(child.row, child.col, 90)
            world.blocks[node.row][node.col] = block
            whilenum += 1
        return[]


def iterativeDeepeningSearch(world):
    for i in range(1, 9999):
        p = IDS(world, i)
        if len(p):
           return p
    return []


def uniformCostSearch(world):
    counter = 0
    checked = [[False for _ in range(world.width())] for _ in range(world.height())]
    Pqueue = PriorityQueue()
    node = Node(world, world.src[0], world.src[1], list(), 0, 0)
    node.priority = 0
    t1 = time.time()
    Pqueue.push(node, node.priority)
    counter += 1
    whilenum = 0
    while not Pqueue.isEmpty():
        node = Pqueue.pop()
        block = deepcopy(world.block(node.row, node.col))
        # print 'rotate', node.rotate*90
        world.rotate_block(node.row, node.col, node.rotate * 90)
        # print world
        # print node.row, node.col
        checked[node.row][node.col] = True
        if (node.row, node.col) == world.dst:
            t2 = time.time()
            node.parents.pop(0)
            print 'Effective branch factor :', float(counter / whilenum)
            print 'number of nodes in UCS: ', counter, 'TIME', t2-t1
            return node.parents
        else:
            for i in range(4):
                if node.row - 1 >= 0:
                    child = Node(world, node.row - 1, node.col, node.parents, i, node.level + 1)
                    child.priority = node.priority + i + 1
                    if world.connect_up_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'up',(child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col + 1 < world.height():
                    child = Node(world, node.row, node.col + 1, node.parents, i, node.level+1)
                    child.priority = node.priority + i + 1
                    if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'right', (child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.row + 1 < world.height():
                    child = Node(world, node.row + 1, node.col, node.parents, i, node.level + 1)
                    child.priority = node.priority + i + 1
                    if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'down', (child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col - 1 >= 0:
                    child = Node(world, node.row, node.col - 1, node.parents, i, node.level + 1)
                    child.priority = node.priority + i + 1
                    if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'left', (child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)
        world.blocks[node.row][node.col] = block
        whilenum += 1
    return []


def manhattanHeuristicFunction(world, current_node):

    return abs(current_node.row - world.dst[0]) + abs(current_node.col - world.dst[1])


def heuristicFunction(world, current_node):
    block = world.block(current_node.row, current_node.col)
    distance = abs(current_node.row - world.dst[0])+abs(current_node.col - world.dst[1])
    p = float(distance) / (block.d+block.u+block.r+block.l)
    return p


def aStarSearch(world):
    counter = 0
    checked = [[False for _ in range(world.width())] for _ in range(world.height())]
    Pqueue = PriorityQueue()
    root_priority = abs(world.dst[0]-world.src[0])+abs(world.dst[1]-world.src[1])
    node = Node(world, world.src[0], world.src[1], list(), 0, 0)
    t1 = time.time()
    Pqueue.push(node, root_priority)
    counter += 1
    whilenum =0
    while not Pqueue.isEmpty():
        node = Pqueue.pop()
        block = deepcopy(world.block(node.row, node.col))
        # print 'rotate', node.rotate*90
        world.rotate_block(node.row, node.col, node.rotate * 90)
        # print world
        # print node.row, node.col
        checked[node.row][node.col] = True
        if (node.row, node.col) == world.dst:
            t2 = time.time()
            node.parents.pop(0)
            print 'Effective branch factor :', float(counter / whilenum)
            print 'number of nodes in a*: ', counter, 'TIME', t2 - t1
            return node.parents
        else:
            for i in range(4):
                if node.row - 1 >= 0:
                    child = Node(world, node.row - 1, node.col, node.parents, i, node.level + 1)
                    child.priority = node.priority + i + 1+ manhattanHeuristicFunction(world, child)
                    if world.connect_up_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'up',(child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col + 1 < world.height():
                    child = Node(world, node.row, node.col + 1, node.parents, i, node.level+1)
                    child.priority = node.priority + i + 1 + manhattanHeuristicFunction(world, child)
                    if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'right', (child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.row + 1 < world.height():
                    child = Node(world, node.row + 1, node.col, node.parents, i, node.level + 1)
                    child.priority = node.priority + i + 1 + manhattanHeuristicFunction(world, child)
                    if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'down', (child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col - 1 >= 0:
                    child = Node(world, node.row, node.col - 1, node.parents, i, node.level + 1)
                    child.priority = node.priority + i + 1 + manhattanHeuristicFunction(world, child)
                    if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'left', (child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)
        world.blocks[node.row][node.col] = block
        whilenum += 1
    return []

def aStarSearchMyHeuristic(world):
    counter = 0
    checked = [[False for _ in range(world.width())] for _ in range(world.height())]
    Pqueue = PriorityQueue()
    node = Node(world, world.src[0], world.src[1], list(), 0, 0)
    block = world.block(node.row, node.col)
    root_priority = (abs(world.dst[0] - world.src[0]) + abs(world.dst[1] - world.src[1])) / (block.d+block.u+block.r+block.l)
    t1 = time.time()
    Pqueue.push(node, root_priority)
    counter += 1
    whilenum = 0
    while not Pqueue.isEmpty():
        node = Pqueue.pop()
        block = deepcopy(world.block(node.row, node.col))
        # print 'rotate', node.rotate*90
        world.rotate_block(node.row, node.col, node.rotate * 90)
        # print world
        # print node.row, node.col
        checked[node.row][node.col] = True
        if (node.row, node.col) == world.dst:
            t2 = time.time()
            node.parents.pop(0)
            print 'Effective branch factor :', float(counter / whilenum)
            print 'number of nodes in a*: ', counter, 'TIME', t2 - t1
            return node.parents
        else:
            for i in range(4):
                if node.row - 1 >= 0:
                    child = Node(world, node.row - 1, node.col, node.parents, i, node.level + 1)
                    child.priority = node.priority + i + 1 + heuristicFunction(world, child)
                    if world.connect_up_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'up',(child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col + 1 < world.height():
                    child = Node(world, node.row, node.col + 1, node.parents, i, node.level+1)
                    child.priority = node.priority + i + 1 + heuristicFunction(world, child)
                    if world.connect_right_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'right', (child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.row + 1 < world.height():
                    child = Node(world, node.row + 1, node.col, node.parents, i, node.level + 1)
                    child.priority = node.priority + i + 1 + heuristicFunction(world, child)
                    if world.connect_down_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'down', (child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)

            for i in range(4):
                if node.col - 1 >= 0:
                    child = Node(world, node.row, node.col - 1, node.parents, i, node.level + 1)
                    child.priority = node.priority + i + 1 + heuristicFunction(world, child)
                    if world.connect_left_block(node.row, node.col) and not checked[child.row][child.col]:
                        child.parents.append((node.row, node.col, node.rotate))
                        # print 'left', (child.row, child.col, i)
                        Pqueue.push(child, child.priority)
                        counter += 1
                    world.rotate_block(child.row, child.col, 90)
        world.blocks[node.row][node.col] = block
        whilenum += 1
    return []
