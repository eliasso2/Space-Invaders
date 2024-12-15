class Projectil:
    def __init__(self, x, y, v=-5):
        self.x, self.y, self.v = x, y, v

    def moure(self):
        self.y += self.v

    def pinta(self, w):
        w.create_line(self.x, self.y, self.x, self.y-10)
