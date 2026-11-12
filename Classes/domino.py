from Classes.plateau import Plateau

class Domino(object):

    def __init__(self, gauche, droit):
        self.g = gauche
        self.d = droit

    def __eq__(self, autre):
        if not isinstance(autre, Domino):
            return False
        return (self.g == autre.g and self.d == autre.d) or (self.g == autre.d and self.d == autre.g)

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

    def posable(self,plateau,cote):
        if self.g == plateau.p[-1].cote or self.d == plateau.p[-1].cote:
            return True
        return False

if __name__== "__main__":
    dr=Domino(3,7)
    de=Domino(6,3)
    dr.turn()
    print(dr)
    print(de.possible(dr))



