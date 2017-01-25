class Block:

    def __init__(self,array):
        self.u = array[0]
        self.r = array[1]
        self.d = array[2]
        self.l = array[3]

    def rotate(self, angle):  # rotate counterclockwise
        action_id = -1

        if angle == 0:
            action_id = 2
        elif angle == 90:
            self.u, self.r, self.d, self.l = self.r, self.d, self.l, self.u
            action_id = 1
        elif angle == 180:
            self.u, self.r, self.d, self.l = self.d, self.l, self.u, self.r
            action_id = 0
        elif angle == 270:
            self.u, self.r, self.d, self.l = self.l, self.u, self.r, self.d
            action_id = 3
        else:
            raise Exception("invalid angle")

        return action_id

    def to_array(self):
        return [self.u, self.r, self.d, self.l]

    def __repr__(self):
        return '-'.join(map(str, self.to_array()))
