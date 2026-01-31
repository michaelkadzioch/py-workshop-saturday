import math

class Rechteck:
    def __init__(self, a, b): 
        self.a = a
        self.b = b

    def umfang(self):
        return 2 * (self.a + self.b)

    def flaeche(self):
        return self.a * self.b


class Kreis:
    def __init__(self, r):
        self.radius = r

    def umfang(self):
        return 2 * self.radius * math.pi 

    def flaeche(self):
        return math.pi * self.radius ** 2



def main():
    print('Python mit Klassen und Objekten')

    object1 = Rechteck(10, 7)

    print(f'Umfang des Rechtecks: {object1.umfang()}')
    print(f'Fläche des Rechtecks: {object1.flaeche()}')

    object2 = Rechteck(5, 8)

    print(f'Umfang des Rechtecks: {object2.umfang()}')
    print(f'Fläche des Rechtecks: {object2.flaeche()}')

    gesamtFlaeche = object1.flaeche() + object2.flaeche()

    print(f'Gesamtfläche der beiden Rechtecke: {gesamtFlaeche}')

    object3 = Kreis(5)

    print(f'Umfang des Kreises: {object3.umfang():.3f}')
    print(f'Fläche des Kreises: {object3.flaeche():.3f}')



if __name__ == '__main__':
    main()