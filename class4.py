import math

class Rechteck:
    def __init__(self, a, b): 
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rechteck-Objekt: \na: {self.a} \nb: {self.b} \nFläche: {self.flaeche()} \nUmfang: {self.umfang()}\n'

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
    print('Python mit Klassen und Objekten')

    object1 = Rechteck(10, 7)
    object2 = Rechteck(30, 17)
    object3 = Kreis(15)

    print(object1)
    print(object2)
    print(object3)



if __name__ == '__main__':
    main()