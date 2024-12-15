from projectil import *


class Enemic:
    def __init__(self, x, y, ample, alt, v=1):
        self.x, self.y, self.ample, self.alt, self.v = x, y, ample, alt, v

    def moure(self):
        self.x += self.v

    def pinta(self, w):
        w.create_rectangle(self.x, self.y, self.x +
                           self.ample, self.y + self.alt)
