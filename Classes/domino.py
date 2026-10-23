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

if __name__== "__main__"():
    dr=Domino(3,7)
    de=Domino(6,3)
    dr.turn
    print(dr)



