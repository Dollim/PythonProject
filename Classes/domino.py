class Domino(object):

    def __init__(self, gauche, droit):
        self.g = gauche
        self.d = droit

    def is_double(self):
        return self.g==self.d

    def turn(self):
        self.g=self.d
        self.d=self.g
        return self

    def score(self):
        return self.g+self.d

    def possible(self,domino):
        return self.d in (domino.g,domino.d )



