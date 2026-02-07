import math

class Rechteck:
    def __init__(self, a, b): 
        self.a = self.checkValues(a)
        self.b = self.checkValues(b)

    def __str__(self):
        return f'Rechteck-Objekt: \na: {self.a} \nb: {self.b} \nFläche: {self.flaeche()} \nUmfang: {self.umfang()}\n'

    def setA(self, a):
        self.a = self.checkValues(a)

    def setB(self, b):
        self.b = self.checkValues(b)

    def checkValues(self, value):
        try: 
            return float(value)
        except ValueError:
            return 0

    def umfang(self):
        return 2 * (self.a + self.b)

    def flaeche(self):
        return self.a * self.b


class Kreis:
    def __init__(self, r):
        self.radius = r

    def __str__(self):
        return f'Kreis-Objekt: \nr: {self.radius} \nFläche: {self.flaeche():.3f} \nUmfang: {self.umfang():.3f}\n'

    def umfang(self):
        return 2 * self.radius * math.pi 

    def flaeche(self):
        return math.pi * self.radius ** 2



def main():
    print('Python mit Klassen und Set-Methoden')

    rechteck1 = Rechteck(10, 'hugo')
    print(rechteck1)

    rechteck1.setA('hugo') 
    print(rechteck1)



if __name__ == '__main__':
    main()