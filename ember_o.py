import math

class Ember:
    def __init__(self, Eletkor = 0, magassag = 0, Tudasszint = 0, Nem = "", Csaladnev = "", Keresztnev = "", testsuly = ""):
        self.Eletkor = Eletkor
        self.magassag = magassag
        self.Tudasszint = Tudasszint
        self.Nem = Nem
        self.Csaladnev = Csaladnev
        self.Keresztnev = Keresztnev
        self.testsuly = testsuly

    def BMI(self):
        BMI = round(self.testsuly/((self.magassag/100)*(self.magassag/100)))
        return BMI

    def IQ(self):
        IQ = round((self.Eletkor/self.Tudasszint)*100)
        return IQ

    def Kiir(self):
        return print("Nemed:", self.Nem, ", Neved:", self.Csaladnev + " " + self.Keresztnev,
                     ", Életkorod:", self.Eletkor, "év, Testmagasságod: ", self.magassag,", testtömeged: ", self.testsuly,
                     "kg, A BMI indexed:", self.BMI(),
                     ", IQ-d:", self.IQ())

