class Domino(object):


    def __init__(self, gauche, droit):
        self.g = gauche
        self.d = droit

    def est_double(self):
        return self.g==self.d

    def sens(self):
        self.g=self.d
        self.d=self.g
        return self

    def








