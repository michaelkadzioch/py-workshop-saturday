class Rechteck:
    # Standartwerte setzen
    def __init__(self, a = 0, b = 0): 
        self.a = a
        self.b = b

    def umfang(self):
        return 2 * (self.a + self.b)

    def flaeche(self):
        return self.a * self.b



def main():
    object1 = Rechteck()

    print(object1.a)
    print(object1.b)

    # Werte im Objekt ändern
    object1.a = 5
    object1.b = 10

    print(object1.a)
    print(object1.b)


if __name__ == '__main__':
    main()