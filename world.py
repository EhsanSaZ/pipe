from block import Block


class World:
    blocks = list(list())
    src = tuple()
    dst = tuple()

    def __init__(self, array2d, start, end, width, height):
        self.src = (start / width, start % width)  # (row, col)
        self.dst = (end / width, end % width)  # (row, col)

        i = 0
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(Block(array2d[i]))
                i += 1
            self.blocks.append(row)

    def __repr__(self):
        blks = []
        for row in self.blocks:
            blks.append('    '.join(map(str, row)))
        blks = '**           ' + ("\n**           ".join(blks))

        s = ""
        s += "******************** WORLD ********************\n"
        s += "**  source      = %s\n" % (self.src,)
        s += "**  destination = %s\n" % (self.dst,)
        s += "**  blocks =\n%s\n" % blks
        s += "***********************************************"
        return s

    def width(self):
        return len(self.blocks[0])

    def height(self):
        return len(self.blocks)

    def block(self, row, col):
        return self.blocks[row][col]

    def rotate_block(self, row, col, angle):
        action_id = self.blocks[row][col].rotate(angle)
        block_id = row * self.width() + col
        return (block_id, action_id)

    def neighbours(self, row, col):
        b = self.blocks
        w = self.width()
        h = self.height()

        return [
            b[row - 1][col].d == b[row][col].u == 1 if row - 1 >= 0 else False,
            b[row][col + 1].l == b[row][col].r == 1 if col + 1 < w  else False,
            b[row + 1][col].u == b[row][col].d == 1 if row + 1 < h  else False,
            b[row][col - 1].r == b[row][col].l == 1 if col - 1 >= 0 else False
        ]
    def connect_up_block(self, row, col):
        b = self.blocks
        return b[row - 1][col].d == b[row][col].u == 1 if row - 1 >= 0 else False

    def connect_right_block(self, row, col):
        b = self.blocks
        w = self.width()
        return b[row][col + 1].l == b[row][col].r == 1 if col + 1 < w else False

    def connect_down_block(self, row, col):
        b = self.blocks
        h = self.height()
        return b[row + 1][col].u == b[row][col].d == 1 if row + 1 < h  else False

    def connect_left_block(self, row, col):
        b = self.blocks
        return b[row][col - 1].r == b[row][col].l == 1 if col - 1 >= 0 else False