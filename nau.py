from projectil import *


class Nau:
    def __init__(self, x, y, ample, alt, v=1):
        self.x, self.y, self.ample, self.alt, self.v = x, y, ample, alt, v

    def moure(self, direcció):
        self.x += direcció * self.v

    def pinta(self, w):
        w.create_rectangle(self.x, self.y, self.x + self.ample,
                           self.y + self.alt, fill='navy')
        w.create_line(self.x + self.ample * (1/2), self.y,
                      self.x + self.ample * (1/2), self.y - 10)

    def dispara(self, projectils):
        projectils.append(Projectil(self.x + self.ample/2, self.y - 10))
