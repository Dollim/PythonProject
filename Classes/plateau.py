from Classes.domino import  Domino

class Plateau():

    def __init__(self):
        self.p=[]

    def placer(self,domino,cote="d"):       # coté peut prendre d (droite) ou g (gauche)
        if cote=="d":
            self.p.append(domino)
        elif cote=="g":
            self.p.insert(0,domino)

    def __str__(self):
        res=str(self.p)
        return res[1:-1].replace("'","")

    def posable(self,domino,cote):


if __name__=="__main__":
    p=Plateau()
    Plateau.placer(p,Domino(4,5))
    Plateau.placer(p, Domino(3, 5))
    print(p)