import math

class Rechteck:
    error = False
    a = 0
    b = 0

    # Standartwerte setzen
    def __init__(self, a, b): 
        self.a = self.checkValues(a)
        self.b = self.checkValues(b)

    def __str__(self):
        return f'Rechteck-Objekt: \
            \na: {self.a} \
            \nb: {self.b} \
            \nFläche: {self.flaeche()} \
            \nUmfang: {self.umfang()} \
            \nFehler: {self.error}\n'

    def setA(self, a):
        self.a = self.checkValues(a)

    def setB(self, b):
        self.b = self.checkValues(b)

    def checkValues(self, value):
        try: 
            float(value)
        except ValueError:
            self.error = True
            return 0
        else:
            self.error = False
            return float(value)
        
    def getError(self):
        return self.error

    def umfang(self):
        return 2 * (self.a + self.b)

    def flaeche(self):
        return self.a * self.b


class Kreis:
    error = False
    radius = 0
    def __init__(self, r):
        self.radius = self.checkValues(r)

    def __str__(self):
        return f'Kreis-Objekt: \nr: {self.radius} \nFläche: {self.flaeche():.3f} \nUmfang: {self.umfang():.3f} \nFehler: {self.error}\n'
    
    def setRadius(self, r):
        self.radius = self.checkValues(r)
    
    def checkValues(self, value):
        try: 
            float(value)
        except ValueError:
            self.error = True
            return 0
        else:
            self.error = False
            return float(value)
        
    def getError(self):
        return self.error

    def umfang(self):
        return 2 * self.radius * math.pi 

    def flaeche(self):
        return math.pi * self.radius ** 2



def main():
    print('Python mit Klassen und Set-Methoden')

    rechteck1 = Rechteck(10, 4)
    rechteck2 = Rechteck(30, 5)
    kreis1 = Kreis(15)

    if not rechteck1.getError() and not rechteck2.getError():
        gesamtFlaeche = rechteck1.flaeche() + rechteck2.flaeche()
        print(f'Gesamtfläche der Rechtecke: {gesamtFlaeche:.3f}')

    else:
        print('Fehler: Eingaben sind keine gültige Zahlen.')


    if not rechteck2.getError() and not kreis1.getError():
        gesamtUmfang = rechteck2.umfang() + kreis1.umfang()
        print(f'Gesamtumfang der Rechteck und Kreis: {gesamtUmfang:.3f}')
    else:
        print('Fehler: Eingaben sind keine gültige Zahlen.')


if __name__ == '__main__':
    main()