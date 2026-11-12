class Domino(object):

    def __init__(self, gauche, droit):
        self.g = gauche
        self.d = droit

    def is_double(self):
        return self.g==self.d

    def turn(self):
        self.g , self.d = self.d,self.g
        return self

    def score(self):
        return self.g+self.d

    def possible(self,domino):
        return self.d in (domino.g,domino.d) or self.g in (domino.g,domino.d)

    def __repr__(self):
        return f"[{self.g} 〡 {self.d}]"

if __name__== "__main__":
    dr=Domino(3,7)
    de=Domino(6,3)
    dr.turn()
    print(dr)
    print(de.possible(dr))



