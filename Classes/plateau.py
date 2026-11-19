class Plateau():

    def __init__(self):
        self.p=[]

    def placer(self,domino,cote):       # coté peut prendre d (droite) ou g (gauche)
        if len(p)==0:
            self.p.append(domino)
        elif cote=="droite":
            if domino.d==self.p[-1].d:
                    self.p.append(domino.turn())
            else:
                self.p.append(domino)
        elif cote=="gauche":
            if domino.g==self.p[0].g:
                self.p.insert(0,domino.turn())
            else:
                self.p.insert(0,domino)

    def __str__(self):
        res=str(self.p)
        return res[1:-1].replace("'","")



from Classes.domino import  Domino
if __name__=="__main__":
    p=Plateau()
    Plateau.placer(p,Domino(4,5))
    Plateau.placer(p, Domino(3, 5))
    print(p)