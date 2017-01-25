from pygame import *
from pygame import gfxdraw
from random import sample, choice
import copy
from ai import HowToReturnPath

init()
FONT = font.Font(font.get_default_font(), 50)


class Case(Rect):
    ''
    CASE = Surface((61, 61))
    CASE.set_colorkey((1, 1, 1))
    CASERECT = CASE.get_rect()
    gfxdraw.filled_circle(CASE, 30, 30, 30, (200, 200, 200))
    gfxdraw.aacircle(CASE, 30, 30, 30, (200, 200, 200))

    def __init__(self, x, y, joncs):
        self.jonction = [0, 0, 0, 0]
        self.marqueur = False
        self.image = Case.CASE.copy()
        S = sample(((Case.CASERECT.midtop, 0), (Case.CASERECT.midright, 1), (Case.CASERECT.midbottom, 2),
                    (Case.CASERECT.midleft, 3)), 3)[:choice((2, 3))]
        if joncs[0] == 1:
            draw.line(self.image, (1, 1, 1), (30, 30), Case.CASERECT.midtop, 9)
            self.jonction[0] = 1
        if joncs[1] == 1:
            draw.line(self.image, (1, 1, 1), (30, 30), Case.CASERECT.midright, 9)
            self.jonction[1] = 1
        if joncs[2] == 1:
            draw.line(self.image, (1, 1, 1), (30, 30), Case.CASERECT.midbottom, 9)
            self.jonction[2] = 1
        if joncs[3] == 1:
            draw.line(self.image, (1, 1, 1), (30, 30), Case.CASERECT.midleft, 9)
            self.jonction[3] = 1

        Rect.__init__(self, SCREEN.blit(self.image, (x, y)))

    def rotate(self, dir):
        dir -= 2
        if dir == 1:
            self.jonction.insert(0, self.jonction.pop())
        else:
            self.jonction.append(self.jonction.pop(0))
        display.update(self)
        time.wait(40)
        self.image = transform.rotate(self.image, -90 * dir)


score = 0
x = 3 # Number of blocks in x
y = 3  # Number of blocks in y
# Each block is 61*61
SCREEN = display.set_mode((61 * x, 61 * y))
SRECT = SCREEN.get_rect()
with open('./input.dat') as file:
    array2d = [[int(digit) for digit in line.split()] for line in file]
ALLS = []
for i in range(x * y):
    ALLS.append(Case(61 * (i % x), 61 * (i / x), array2d[i]))
START = choice(range(x * y)[::x])
gfxdraw.filled_circle(ALLS[START].image, 30, 30, 30, (200, 0, 0))
gfxdraw.aacircle(ALLS[START].image, 30, 30, 30, (200, 0, 0))
SCREEN.blit(ALLS[START].image, ALLS[START])
ALLS[START].jonction = [1, 1, 1, 1]
END = choice(range(x * y)[x - 1::x])
gfxdraw.filled_circle(ALLS[END].image, 30, 30, 30, (0, 0, 200))
gfxdraw.aacircle(ALLS[END].image, 30, 30, 30, (0, 0, 200))
SCREEN.blit(ALLS[END].image, ALLS[END])
ALLS[END].jonction = [1, 1, 1, 1]
for i in sample(ALLS, x * y):  # Animation
    time.wait(10)
    display.update(i)

event.clear()
event.post(event.Event(MOUSEBUTTONDOWN, {'button': 1, 'pos': (0, 0)}))
coup = 0  # Number of iterations
display.set_caption('AI Project')
# time.wait(999)

path = HowToReturnPath(array2d, START, END, x, y);  # Your defined fnction
for c in path:
    coup += 1
    ALLS[c[0]].rotate(c[1])
    for i in ALLS:
        i.marqueur = False
        SCREEN.fill(0, i)
        SCREEN.blit(i.image, i)
    temp = [START]
    ALLS[START].marqueur = True
    while temp:
        for case in temp:
            for e, j in enumerate(ALLS[case].jonction):
                if j and SRECT.contains(ALLS[case].move(((0, -61), (61, 0), (0, 61), (-61, 0))[e])) \
                        and ALLS[case + (-x, 1, x, -1)[e]].marqueur == False \
                        and ALLS[case + (-x, 1, x, -1)[e]].jonction[e - 2] \
                        and case != END:
                    temp.append(case + (-x, 1, x, -1)[e])
                    ALLS[case + (-x, 1, x, -1)[e]].marqueur = True
                    SCREEN.fill(0xf00000, ALLS[case + (-x, 1, x, -1)[e]])
                    SCREEN.blit(ALLS[case + (-x, 1, x, -1)[e]].image, ALLS[case + (-x, 1, x, -1)[e]])
            temp.remove(case)
    display.update()
    time.wait(999)
print coup
# for i in sample(ALLS,len(ALLS)):
#     SCREEN.fill(0,i)
#     time.wait(10)
#     display.update(i)

while True:
    for e in event.get():
        if e.type == QUIT:
            exit(0)
