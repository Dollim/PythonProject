from Classes.domino import  Domino

class Plateau():

    def __init__(self):
        self.p=[]

    def placer(self,domino,coté="d"):       # coté peut prendre d (droite) ou g (gauche)
        if coté=="d":
            self.p.append(domino)
        elif coté=="g":
            self.p.insert(0,domino)

    def __str__(self):
        res=str(self.p[0])
        return res



if __name__=="__main__":
    p=Plateau()
    print(p.p)
    Plateau.placer(p,Domino(4,5))
    print(p)