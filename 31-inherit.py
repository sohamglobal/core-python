class Ethan:
    def __init__(self):
        print("base class running")

    def showbase(self):
        print("welcome to base class")

class Praffull:
    def showmiddle(self):
        print("middle class")


class Soham(Ethan,Praffull):
    def __init__(self):
        Ethan.__init__(self)
        print("derived class running")
        

    def showderived(self):
        print("welcome to derived class")

s=Soham()
s.showderived()
s.showbase()
s.showmiddle()
